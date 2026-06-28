const API_URL = 'http://127.0.0.1:8000';

const ACTIONS = {
    STOP: 0,
    LEFT: 1,
    RIGHT: 2,
    UP: 3,
    DOWN: 4,
    BOMB: 5,
};

const ACTION_LABELS = {
    0: 'STOP',
    1: 'LEFT',
    2: 'RIGHT',
    3: 'UP',
    4: 'DOWN',
    5: 'BOMB',
};

const AGENT_COLORS = {
    player_1: '#38bdf8',
    player_2: '#f472b6',
    player_3: '#34d399',
    player_4: '#fbbf24',
};

const PLAYER_IDS = ['player_1', 'player_2', 'player_3', 'player_4'];
const MAP_PRESETS = [
    { value: 'classic', label: 'Classic' },
    { value: 'csp', label: 'CSP Generated' },
    { value: 'open', label: 'Open Field' },
    { value: 'dense', label: 'Dense Maze' },
];

const state = {
    game: null,
    previousGame: null,
    gameMode: 'god',
    fowEnabled: false,
    fowRadius: 4,
    focusAgent: 'player_1',
    mapPreset: 'classic',
    seed: 42,
    agentCount: 4,
    speedMs: 300,
    running: false,
    matchStatus: 'ready',
    intervalId: null,
    availableAgents: [],
    agentConfigs: {
        player_1: 'manual',
        player_2: 'minimax',
        player_3: 'minimax',
        player_4: 'minimax',
    },
    logs: [],
    trace: null,
    traceSelectedNodeId: null,
    treeTransform: { x: 120, y: 40, scale: 0.76 },
    treeDrag: { active: false, lastX: 0, lastY: 0 },
};

const el = {
    connectionPill: document.getElementById('connection-pill'),
    stepPill: document.getElementById('step-pill'),
    gameModePill: document.getElementById('game-mode-pill'),
    gameStatus: document.getElementById('game-status'),
    stepCount: document.getElementById('step-count'),
    lastAction: document.getElementById('last-action'),
    board: document.getElementById('board'),
    boardPlaceholder: document.getElementById('board-placeholder'),
    boardStage: document.querySelector('.board-stage'),
    focusAgentSelect: document.getElementById('focus-agent-select'),
    gameViewSelect: document.getElementById('game-view-select'),
    fowToggle: document.getElementById('chk-fow'),
    fowRadius: document.getElementById('fow-radius'),
    speedSlider: document.getElementById('speed-slider'),
    speedValue: document.getElementById('speed-value'),
    mapSelect: document.getElementById('map-select'),
    seedInput: document.getElementById('seed-input'),
    agentCount: document.getElementById('agent-count'),
    p1Select: document.getElementById('agent-select-p1'),
    p2Select: document.getElementById('agent-select-p2'),
    p3Select: document.getElementById('agent-select-p3'),
    p4Select: document.getElementById('agent-select-p4'),
    startBtn: document.getElementById('btn-start'),
    pauseBtn: document.getElementById('btn-pause'),
    resumeBtn: document.getElementById('btn-resume'),
    resetBtn: document.getElementById('btn-reset'),
    agentStatusList: document.getElementById('agent-status-list'),
    labAlgorithmSelect: document.getElementById('lab-algorithm-select'),
    labScenarioSelect: document.getElementById('lab-scenario-select'),
    labViewSelect: document.getElementById('lab-view-select'),
    labFocusSelect: document.getElementById('lab-focus-select'),
    labRefreshBtn: document.getElementById('lab-refresh-btn'),
    labMetaCards: document.getElementById('lab-meta-cards'),
    labTreeStage: document.getElementById('lab-tree-stage'),
    labTreeEdges: document.getElementById('lab-tree-edges'),
    labTreeCanvas: document.getElementById('lab-tree-canvas'),
    labNodeDetails: document.getElementById('lab-node-details'),
    labFrontier: document.getElementById('lab-frontier'),
    labClosed: document.getElementById('lab-closed'),
    labInsight: document.getElementById('lab-insight'),
    labEventLog: document.getElementById('lab-event-log'),
    labLogSearch: document.getElementById('lab-log-search'),
    labAgentFilter: document.getElementById('lab-agent-filter'),
    labClearLog: document.getElementById('lab-clear-log'),
};

function coordKey(x, y) {
    return `${x},${y}`;
}

function nowStamp() {
    return new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
}

function clamp(value, min, max) {
    return Math.max(min, Math.min(max, value));
}

function chebyshev(a, b) {
    return Math.max(Math.abs(a[0] - b[0]), Math.abs(a[1] - b[1]));
}

function manhattan(a, b) {
    return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
}

function getAgent(stateObj, agentId) {
    return stateObj?.agents?.[agentId] || null;
}

function aliveAgents(stateObj) {
    return Object.values(stateObj?.agents || {}).filter((agent) => agent.is_alive);
}

function agentLabel(agentId) {
    if (agentId === 'player_1') return 'P1';
    if (agentId === 'player_2') return 'P2';
    if (agentId === 'player_3') return 'P3';
    if (agentId === 'player_4') return 'P4';
    return agentId;
}

function algoName(id) {
    const found = state.availableAgents.find((a) => a.id === id);
    return found ? found.name : id;
}

function setConnection(type, title, description) {
    if (!el.connectionPill) return;
    el.connectionPill.className = `pill pill-${type}`;
    el.connectionPill.textContent = title;
    if (description) {
        el.connectionPill.title = description;
    }
}

function setGameModeLabel() {
    if (!el.gameModePill) return;
    const label = state.gameMode === 'god' ? 'God View' : 'Agent View';
    el.gameModePill.textContent = state.fowEnabled && state.gameMode === 'agent'
        ? `${label} + FOW`
        : label;
}

function setBoardPlaceholder(show) {
    if (el.boardPlaceholder) el.boardPlaceholder.hidden = !show;
    if (el.board) el.board.style.visibility = show ? 'hidden' : 'visible';
}

function setStepInfo(stepCount) {
    if (el.stepPill) el.stepPill.textContent = `Step ${stepCount}`;
    if (el.stepCount) el.stepCount.textContent = `${stepCount}`;
}

function setSpeed(ms) {
    state.speedMs = ms;
    if (el.speedValue) el.speedValue.textContent = `${ms} ms`;
    if (el.speedSlider) el.speedSlider.value = `${ms}`;
    if (state.running) {
        restartLoop();
    }
}

function populateSelect(selectEl, options, selectedValue) {
    if (!selectEl) return;
    selectEl.innerHTML = '';
    for (const item of options) {
        const option = document.createElement('option');
        option.value = item.value;
        option.textContent = item.label;
        selectEl.appendChild(option);
    }
    if (selectedValue != null) selectEl.value = selectedValue;
}

function populateAgentSelects() {
    const botOptions = state.availableAgents.map((agent) => ({ value: agent.id, label: agent.name }));
    const allOptions = [{ value: 'manual', label: 'Manual' }, ...botOptions];
    const activePlayers = PLAYER_IDS.slice(0, state.agentCount);
    const focusOptions = activePlayers.map((id) => ({ value: id, label: agentLabel(id) }));

    populateSelect(el.p1Select, allOptions, state.agentConfigs.player_1 || 'manual');
    populateSelect(el.p2Select, botOptions, state.agentConfigs.player_2 || 'minimax');
    populateSelect(el.p3Select, botOptions, state.agentConfigs.player_3 || 'minimax');
    populateSelect(el.p4Select, botOptions, state.agentConfigs.player_4 || 'minimax');
    if (!activePlayers.includes(state.focusAgent)) {
        state.focusAgent = activePlayers[0] || 'player_1';
    }
    populateSelect(el.focusAgentSelect, focusOptions, state.focusAgent);
    populateSelect(el.labFocusSelect, focusOptions, state.focusAgent);
}

function populateLabAlgorithmSelect() {
    const options = state.availableAgents.map((agent) => ({ value: agent.id, label: agent.name }));
    populateSelect(el.labAlgorithmSelect, options, el.labAlgorithmSelect?.value || 'bfs');
}

function populateMapSelect() {
    populateSelect(el.mapSelect, MAP_PRESETS, state.mapPreset);
}

function updateAgentCountUI() {
    const count = Number(el.agentCount.value || 4);
    state.agentCount = clamp(count, 2, 4);
    el.agentCount.value = `${state.agentCount}`;
    const rows = [el.p1Select, el.p2Select, el.p3Select, el.p4Select];
    rows.forEach((select, index) => {
        if (!select) return;
        const enabled = index < state.agentCount;
        select.disabled = !enabled;
        select.parentElement.style.opacity = enabled ? '1' : '0.35';
    });
    populateAgentSelects();
}

function extractSettingsFromUI() {
    state.gameMode = el.gameViewSelect.value;
    state.fowEnabled = el.fowToggle.checked;
    state.fowRadius = clamp(Number(el.fowRadius.value || 4), 1, 6);
    state.mapPreset = el.mapSelect.value;
    state.seed = Number(el.seedInput.value || 42);
    state.agentCount = clamp(Number(el.agentCount.value || 4), 2, 4);
    state.focusAgent = el.focusAgentSelect.value || 'player_1';
    state.agentConfigs = {
        player_1: el.p1Select.value || 'manual',
        player_2: el.p2Select.value || 'minimax',
        player_3: el.p3Select.value || 'minimax',
        player_4: el.p4Select.value || 'minimax',
    };
}

function visibleCellSet(gameState) {
    const visible = new Set();
    if (!gameState) return visible;
    if (state.gameMode === 'god' || !state.fowEnabled) {
        for (let y = 0; y < gameState.height; y += 1) {
            for (let x = 0; x < gameState.width; x += 1) {
                visible.add(coordKey(x, y));
            }
        }
        return visible;
    }

    const focus = getAgent(gameState, state.focusAgent) || aliveAgents(gameState)[0];
    if (!focus) return visible;
    const centers = [[focus.x, focus.y], ...aliveAgents(gameState).filter((agent) => agent.id !== focus.id).map((agent) => [agent.x, agent.y])];
    for (let y = 0; y < gameState.height; y += 1) {
        for (let x = 0; x < gameState.width; x += 1) {
            if (centers.some((center) => chebyshev(center, [x, y]) <= state.fowRadius)) {
                visible.add(coordKey(x, y));
            }
        }
    }
    return visible;
}

function tileClassFor(tileValue, x, y, gameState) {
    if (tileValue === 1) return 'tile-wall';
    if (tileValue === 2) return 'tile-brick';
    if (tileValue === 3) return 'tile-bomb';
    if (tileValue === 4) {
        const origin = Array.isArray(gameState.explosion_origins)
            && gameState.explosion_origins.some((coord) => coord[0] === x && coord[1] === y);
        if (origin) return 'tile-explosion-center';
        const above = y > 0 && gameState.grid[y - 1][x] === 4;
        const below = y < gameState.height - 1 && gameState.grid[y + 1][x] === 4;
        return above || below ? 'tile-explosion-vertical' : 'tile-explosion-horizontal';
    }
    if (tileValue === 5) return 'tile-item-radius';
    if (tileValue === 6) return 'tile-item-capacity';
    return (x + y) % 2 === 0 ? 'tile-empty-even' : 'tile-empty-odd';
}

function resizeBoard(gameState) {
    if (!el.board || !gameState) return;
    const stageWidth = Math.max(320, el.boardStage?.clientWidth || 1000);
    const size = clamp(Math.floor((stageWidth - 80) / gameState.width), 26, 40);
    document.documentElement.style.setProperty('--cell-size', `${size}px`);
    el.board.style.gridTemplateColumns = `repeat(${gameState.width}, var(--cell-size))`;
    el.board.style.gridTemplateRows = `repeat(${gameState.height}, var(--cell-size))`;
}

function addLog(entry) {
    state.logs.unshift(entry);
    state.logs = state.logs.slice(0, 200);
    renderLogs();
}

function describeReason(agentId, action, gameState) {
    if (state.agentConfigs[agentId] === 'manual') {
        return 'Manual input from the player.';
    }
    const focus = getAgent(gameState, agentId);
    if (!focus) return 'Agent unavailable.';
    const nearestBomb = nearestEntityDistance([focus.x, focus.y], gameState.bombs.map((bomb) => [bomb.x, bomb.y]));
    const nearestItem = nearestEntityDistance([focus.x, focus.y], itemCells(gameState));
    const nearestEnemy = nearestEntityDistance([focus.x, focus.y], aliveAgents(gameState).filter((a) => a.id !== agentId).map((a) => [a.x, a.y]));
    return `${algoName(state.agentConfigs[agentId])} picked ${ACTION_LABELS[action] || 'STOP'} | bomb dist ${nearestBomb ?? 'n/a'}, item dist ${nearestItem ?? 'n/a'}, enemy dist ${nearestEnemy ?? 'n/a'}`;
}

function itemCells(gameState) {
    const cells = [];
    for (let y = 0; y < gameState.height; y += 1) {
        for (let x = 0; x < gameState.width; x += 1) {
            if (gameState.grid[y][x] === 5 || gameState.grid[y][x] === 6) cells.push([x, y]);
        }
    }
    return cells;
}

function nearestEntityDistance(origin, positions) {
    if (!positions.length) return null;
    return positions.reduce((best, pos) => Math.min(best, manhattan(origin, pos)), Infinity);
}

function renderBoard() {
    const gameState = state.game;
    if (!gameState || !el.board) {
        setBoardPlaceholder(true);
        return;
    }
    setBoardPlaceholder(false);
    resizeBoard(gameState);

    const visible = visibleCellSet(gameState);
    el.board.innerHTML = '';

    for (let y = 0; y < gameState.height; y += 1) {
        for (let x = 0; x < gameState.width; x += 1) {
            const cell = document.createElement('div');
            const tileValue = gameState.grid[y][x];
            const visibleHere = visible.has(coordKey(x, y));
            cell.className = `tile ${visibleHere ? tileClassFor(tileValue, x, y, gameState) : 'tile-fog'}`;

            if (visibleHere) {
                const agentsLayer = document.createElement('div');
                agentsLayer.className = 'agents-layer';
                for (const agent of Object.values(gameState.agents || {})) {
                    if (agent.x === x && agent.y === y) {
                        const sprite = document.createElement('div');
                        if (agent.is_alive) {
                            sprite.className = `agent agent-${agent.id} dir-${agent.direction || 'down'}`;
                        } else {
                            sprite.className = `agent agent-${agent.id} agent-dead`;
                        }
                        agentsLayer.appendChild(sprite);
                    }
                }
                cell.appendChild(agentsLayer);
            }

            el.board.appendChild(cell);
        }
    }
}

function renderStatus() {
    const gameState = state.game;
    if (!gameState) return;
    setStepInfo(gameState.step_count || 0);
    if (el.gameStatus) {
        const label = {
            ready: 'Ready',
            running: 'Running',
            paused: 'Paused',
            game_over: 'Game Over',
        }[state.matchStatus] || 'Ready';
        el.gameStatus.textContent = label;
    }
    setGameModeLabel();

    if (!el.agentStatusList) return;
    el.agentStatusList.innerHTML = '';
    for (const agent of Object.values(gameState.agents || {})) {
        const row = document.createElement('div');
        row.className = 'status-row';
        const left = document.createElement('div');
        left.className = 'status-name';
        const dot = document.createElement('span');
        dot.className = 'status-dot';
        dot.style.background = AGENT_COLORS[agent.id] || '#fff';
        const label = document.createElement('span');
        const algo = state.agentConfigs[agent.id] || 'manual';
        label.textContent = `${agentLabel(agent.id)} · ${algo === 'manual' ? 'Manual' : algoName(algo)}`;
        left.appendChild(dot);
        left.appendChild(label);

        const right = document.createElement('div');
        right.className = 'status-meta';
        right.innerHTML = agent.is_alive
            ? `HP ${agent.lives} | Bombs ${agent.bombs_left}/${agent.max_bombs} | Range ${agent.bomb_range}`
            : 'Eliminated';
        row.appendChild(left);
        row.appendChild(right);
        el.agentStatusList.appendChild(row);
    }
}

function pushActionLogs(prevState, nextState, response) {
    const now = nowStamp();
    if (!nextState) return;
    const prevAgents = prevState?.agents || {};
    const nextAgents = nextState.agents || {};
    for (const agentId of Object.keys(nextAgents)) {
        const prev = prevAgents[agentId];
        const next = nextAgents[agentId];
        if (!prev || !next) continue;
        const moved = prev.x !== next.x || prev.y !== next.y;
        const bombChange = next.bombs_left !== prev.bombs_left;
        const died = prev.is_alive && !next.is_alive;
        if (moved || bombChange || died) {
            const action = died
                ? 'Lost all lives'
                : moved
                    ? `Moved to (${next.x},${next.y})`
                    : bombChange
                        ? 'Bomb capacity changed'
                        : 'State updated';
            addLog({
                time: now,
                step: nextState.step_count,
                agent: agentLabel(agentId),
                action,
                detail: describeReason(agentId, moved ? 'MOVE' : 'STOP', nextState),
                filterAgent: agentId,
            });
        }
    }
    if (response?.status === 'game_over') {
        addLog({
            time: now,
            step: nextState.step_count,
            agent: 'SYSTEM',
            action: 'Match ended',
            detail: 'The simulation reached the end state.',
            filterAgent: 'system',
        });
    }
}

function buildTrace(gameState) {
    const algoId = el.labAlgorithmSelect.value;
    const scenario = el.labScenarioSelect.value;
    const viewMode = el.labViewSelect.value;
    const focusId = el.labFocusSelect.value || state.focusAgent;
    const focus = getAgent(gameState, focusId) || aliveAgents(gameState)[0];
    const origin = focus ? [focus.x, focus.y] : [1, 1];

    const candidates = [
        { id: 'wait', label: 'WAIT', dx: 0, dy: 0, action: 'WAIT' },
        { id: 'up', label: 'UP', dx: 0, dy: -1, action: 'UP' },
        { id: 'down', label: 'DOWN', dx: 0, dy: 1, action: 'DOWN' },
        { id: 'left', label: 'LEFT', dx: -1, dy: 0, action: 'LEFT' },
        { id: 'right', label: 'RIGHT', dx: 1, dy: 0, action: 'RIGHT' },
        { id: 'bomb', label: 'BOMB', dx: 0, dy: 0, action: 'BOMB' },
    ].map((item) => {
        const nx = origin[0] + item.dx;
        const ny = origin[1] + item.dy;
        const inBounds = nx >= 0 && ny >= 0 && nx < gameState.width && ny < gameState.height;
        const tile = inBounds ? gameState.grid[ny][nx] : 1;
        const walkable = inBounds && ![1, 2, 3].includes(tile);
        const danger = dangerScore([nx, ny], gameState);
        const items = nearestEntityDistance([nx, ny], itemCells(gameState));
        const enemies = nearestEntityDistance([nx, ny], aliveAgents(gameState).filter((a) => a.id !== focusId).map((a) => [a.x, a.y]));
        const mobility = walkable ? countMobility([nx, ny], gameState) : 0;
        const heuristic = baseHeuristic(algoId, danger, items, enemies, mobility, item.id);
        return { ...item, nx, ny, inBounds, walkable, danger, items, enemies, mobility, heuristic };
    });

    const sorted = [...candidates].sort((a, b) => b.heuristic - a.heuristic);
    const root = {
        id: 'root',
        kind: 'State',
        title: `${agentLabel(focusId)} @ (${origin[0]},${origin[1]})`,
        meta: [
            `Scenario: ${scenario}`,
            `View: ${viewMode === 'god' ? 'God View' : 'Agent View'}`,
            `FOW: ${state.fowEnabled ? 'On' : 'Off'}`,
        ],
        x: 1080,
        y: 78,
        width: 220,
        height: 92,
        score: null,
        detail: 'Root state captured from the current board and used to generate the algorithm explanation graph.',
    };

    const nodes = [root];
    const edges = [];
    let yBase = 290;
    const xBase = 280;
    const xStep = 360;
    sorted.forEach((candidate, index) => {
        const id = candidate.id;
        const node = {
            id,
            kind: algoKind(algoId),
            title: candidate.label,
            meta: [
                `Pos: (${candidate.nx},${candidate.ny})`,
                `h: ${fmt(candidate.heuristic)}`,
                `danger: ${fmt(candidate.danger)}`,
                `mobility: ${candidate.mobility}`,
            ],
            x: xBase + index * xStep,
            y: yBase,
            width: 220,
            height: 102,
            score: candidate.heuristic,
            detail: buildCandidateNarrative(algoId, candidate, gameState),
        };
        nodes.push(node);
        edges.push({ from: 'root', to: id });
    });

    const focused = sorted[0];
    if (focused && ['minimax', 'expectimax', 'and_or_search'].includes(algoId)) {
        const responseY = 500;
        const responseNodes = buildResponseNodes(algoId, focused, gameState);
        responseNodes.forEach((child, idx) => {
            const id = `${focused.id}-r${idx}`;
            nodes.push({
                id,
                kind: child.kind,
                title: child.title,
                meta: child.meta,
                x: focused.x - 40 + idx * 220,
                y: responseY,
                width: 210,
                height: 96,
                score: child.score,
                detail: child.detail,
            });
            edges.push({ from: focused.id, to: id });
        });
    }

    const metaCards = buildMetaCards(algoId, focused, candidates, gameState, origin);
    const frontier = buildFrontierList(algoId, sorted, candidates, focusId, gameState);
    const closed = buildClosedList(algoId, sorted, focusId, gameState);
    const insight = buildInsightList(algoId, focused, candidates, gameState, scenario, viewMode);
    const selectedNodeId = state.traceSelectedNodeId && nodes.some((n) => n.id === state.traceSelectedNodeId)
        ? state.traceSelectedNodeId
        : root.id;

    return {
        algoId,
        scenario,
        viewMode,
        focusId,
        origin,
        nodes,
        edges,
        metaCards,
        frontier,
        closed,
        insight,
        selectedNodeId,
    };
}

function algoKind(algoId) {
    const map = {
        bfs: 'Breadth-First Search',
        dfs: 'Depth-First Search',
        astar: 'A* Search',
        greedy: 'Greedy Search',
        hill_climbing: 'Hill Climbing',
        simulated_annealing: 'Simulated Annealing',
        and_or_search: 'AND-OR Search',
        online_search: 'Online Search',
        backtracking: 'Backtracking',
        minimax: 'Minimax',
        expectimax: 'Expectimax',
        random: 'Random',
        min_conflicts: 'Min-Conflicts',
    };
    return map[algoId] || algoId;
}

function baseHeuristic(algoId, danger, items, enemies, mobility, actionId) {
    const itemBonus = items == null ? 0 : 12 - items * 2;
    const enemyBonus = enemies == null ? 0 : 9 - enemies * 1.5;
    const safety = 14 - danger * 1.4;
    const mobilityBonus = mobility * 0.75;
    const bombPenalty = actionId === 'bomb' ? -6 : 0;
    const algoBias = {
        bfs: 10,
        dfs: 7,
        astar: 16,
        greedy: 14,
        hill_climbing: 13,
        simulated_annealing: 12,
        and_or_search: 15,
        online_search: 11,
        backtracking: 9,
        minimax: 13,
        expectimax: 13.5,
        random: 5,
        min_conflicts: 8,
    }[algoId] || 10;
    return algoBias + safety + itemBonus + enemyBonus + mobilityBonus + bombPenalty;
}

function dangerScore(pos, gameState) {
    if (!pos) return 0;
    let danger = 0;
    for (const bomb of gameState.bombs || []) {
        const dist = manhattan([bomb.x, bomb.y], pos);
        if (dist <= bomb.range + 1) danger += Math.max(0, 10 - dist * 2.3);
    }
    for (const [x, y] of gameState.explosions || []) {
        danger += manhattan([x, y], pos) === 0 ? 10 : 0;
    }
    return danger;
}

function countMobility(pos, gameState) {
    if (!pos) return 0;
    const dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]];
    let count = 0;
    for (const [dx, dy] of dirs) {
        const nx = pos[0] + dx;
        const ny = pos[1] + dy;
        if (nx < 0 || ny < 0 || nx >= gameState.width || ny >= gameState.height) continue;
        const tile = gameState.grid[ny][nx];
        if (![1, 2, 3].includes(tile)) count += 1;
    }
    return count;
}

function buildCandidateNarrative(algoId, candidate, gameState) {
    const parts = [];
    if (algoId === 'bfs') {
        parts.push(`BFS expands ${candidate.label} in layer order.`);
    } else if (algoId === 'dfs') {
        parts.push(`DFS dives deeper from ${candidate.label} before backtracking.`);
    } else if (algoId === 'astar') {
        parts.push(`A* combines distance and danger for ${candidate.label}.`);
    } else if (algoId === 'greedy') {
        parts.push(`Greedy prefers the locally best-looking move ${candidate.label}.`);
    } else if (algoId === 'hill_climbing') {
        parts.push(`Hill Climbing tests whether ${candidate.label} improves the current peak.`);
    } else if (algoId === 'simulated_annealing') {
        parts.push(`Simulated Annealing may accept ${candidate.label} even if the score dips.`);
    } else if (algoId === 'minimax') {
        parts.push(`Minimax evaluates ${candidate.label} by anticipating the opponent.`);
    } else if (algoId === 'expectimax') {
        parts.push(`Expectimax averages the response quality of ${candidate.label}.`);
    } else if (algoId === 'backtracking') {
        parts.push(`Backtracking explores ${candidate.label} and prunes invalid branches.`);
    } else if (algoId === 'online_search') {
        parts.push(`Online Search replans from partial visibility after ${candidate.label}.`);
    } else if (algoId === 'and_or_search') {
        parts.push(`AND-OR Search keeps ${candidate.label} if every contingency stays viable.`);
    } else {
        parts.push(`Action ${candidate.label} is scored against the current scenario.`);
    }
    const bombDist = nearestEntityDistance([candidate.nx, candidate.ny], gameState.bombs.map((b) => [b.x, b.y]));
    const itemDist = nearestEntityDistance([candidate.nx, candidate.ny], itemCells(gameState));
    parts.push(`Danger score ${fmt(candidate.danger)} | bombs ${bombDist ?? 'n/a'} | items ${itemDist ?? 'n/a'}.`);
    return parts.join(' ');
}

function buildResponseNodes(algoId, candidate, gameState) {
    const baseScore = candidate.heuristic;
    const enemyCount = aliveAgents(gameState).length - 1;
    const branch = [
        {
            kind: 'Opponent',
            title: 'Opponent reply A',
            meta: [`utility: ${fmt(baseScore - 4)}`, `enemy count: ${enemyCount}`],
            score: baseScore - 4,
            detail: 'Best-case opponent reply after the chosen action.',
        },
        {
            kind: 'Opponent',
            title: 'Opponent reply B',
            meta: [`utility: ${fmt(baseScore - 8)}`, `enemy count: ${enemyCount}`],
            score: baseScore - 8,
            detail: 'Second response branch used to visualize pruning / expectation.',
        },
    ];
    if (algoId === 'expectimax') {
        branch[0].detail = 'Expected value branch for chance-like opponent behavior.';
        branch[1].detail = 'Alternative stochastic branch contributing to the expectation.';
    }
    if (algoId === 'and_or_search') {
        branch[0].kind = 'AND';
        branch[1].kind = 'AND';
    }
    return branch;
}

function buildMetaCards(algoId, focused, candidates, gameState, origin) {
    const best = candidates.reduce((prev, item) => (item.heuristic > prev.heuristic ? item : prev), candidates[0]);
    const bombDist = nearestEntityDistance(origin, gameState.bombs.map((b) => [b.x, b.y]));
    const itemDist = nearestEntityDistance(origin, itemCells(gameState));
    return [
        { label: 'Current node', value: focused ? `${agentLabel(state.focusAgent)} @ (${origin[0]},${origin[1]})` : 'No agent' },
        { label: 'Best action', value: best ? best.label : 'n/a' },
        { label: 'Bomb distance', value: bombDist == null ? 'n/a' : `${bombDist}` },
        { label: 'Item distance', value: itemDist == null ? 'n/a' : `${itemDist}` },
    ];
}

function buildFrontierList(algoId, sorted, candidates, focusId, gameState) {
    const frontierOrder = {
        bfs: sorted,
        dfs: [...sorted].reverse(),
        astar: [...sorted].sort((a, b) => b.heuristic - a.heuristic),
        greedy: [...sorted].sort((a, b) => b.heuristic - a.heuristic),
        hill_climbing: [...sorted].sort((a, b) => b.heuristic - a.heuristic).slice(0, 3),
        simulated_annealing: candidates,
        backtracking: candidates,
        online_search: candidates,
        minimax: candidates,
        expectimax: candidates,
        and_or_search: candidates,
    }[algoId] || candidates;
    return frontierOrder.slice(0, 6).map((item, index) => ({
        title: `${index + 1}. ${item.label}`,
        text: `score ${fmt(item.heuristic)} | pos (${item.nx},${item.ny}) | walkable ${item.walkable ? 'yes' : 'no'}`,
    }));
}

function buildClosedList(algoId, sorted, focusId, gameState) {
    const closed = [];
    const blocked = sorted.filter((item) => !item.walkable);
    const safe = sorted.filter((item) => item.walkable).slice(-3);
    if (algoId === 'bfs' || algoId === 'astar') {
        blocked.forEach((item) => closed.push({ title: item.label, text: `pruned because target tile is blocked or unsafe.` }));
        safe.forEach((item) => closed.push({ title: item.label, text: `already expanded from the frontier.` }));
    } else if (algoId === 'dfs') {
        closed.push({ title: 'Backtrack frontier', text: 'DFS can revisit this branch after a deeper path fails.' });
        closed.push({ title: 'Dead end', text: 'A branch that cannot improve the score is pruned.' });
    } else if (algoId === 'simulated_annealing') {
        closed.push({ title: 'Rejected neighbor', text: 'Rejected because probability test failed at current temperature.' });
        closed.push({ title: 'Accepted worse state', text: 'Kept because annealing still allowed exploration.' });
    } else if (algoId === 'minimax' || algoId === 'expectimax') {
        closed.push({ title: 'Cut branch', text: 'Minimax/Expectimax branch no longer needs expansion.' });
        closed.push({ title: 'Dominated reply', text: 'Opponent response with low utility was compressed.' });
    } else {
        closed.push({ title: 'Inactive branch', text: 'A branch not relevant to the current explanation trace.' });
        closed.push({ title: 'Pruned state', text: 'Node removed by heuristic or constraints.' });
    }
    return closed.slice(0, 5);
}

function buildInsightList(algoId, focused, candidates, gameState, scenario, viewMode) {
    const best = candidates.reduce((prev, item) => (item.heuristic > prev.heuristic ? item : prev), candidates[0]);
    const lines = [];
    lines.push({ title: 'Scenario', text: `${scenario} in ${viewMode === 'god' ? 'God View' : 'Agent View'} mode.` });
    if (algoId === 'bfs') {
        lines.push({ title: 'Frontier queue', text: 'BFS expands the oldest state first and preserves layer order.' });
        lines.push({ title: 'Choice', text: `The current best-looking action is ${best ? best.label : 'n/a'} because it keeps the queue broad and safe.` });
    } else if (algoId === 'dfs') {
        lines.push({ title: 'Depth bias', text: 'DFS commits to the deepest path it can reach before it backtracks.' });
        lines.push({ title: 'Risk', text: 'This is useful for path discovery, but can ignore safer alternatives.' });
    } else if (algoId === 'astar') {
        lines.push({ title: 'g(n), h(n), f(n)', text: 'A* combines travel cost, heuristic distance, and safety in one score.' });
        lines.push({ title: 'Choice', text: `Node ${best ? best.label : 'n/a'} currently has the highest f-score.` });
    } else if (algoId === 'greedy') {
        lines.push({ title: 'Heuristic first', text: 'Greedy ranks the immediate board estimate higher than long-term guarantees.' });
        lines.push({ title: 'Trade-off', text: 'Fast and intuitive, but it can miss the safest escape path.' });
    } else if (algoId === 'hill_climbing') {
        lines.push({ title: 'Local optimum', text: 'Hill Climbing only accepts better neighbors and can stall on a ridge.' });
        lines.push({ title: 'Current peak', text: `Best neighbor is ${best ? best.label : 'n/a'} with score ${best ? fmt(best.heuristic) : 'n/a'}.` });
    } else if (algoId === 'simulated_annealing') {
        const temperature = Math.max(0.1, 8 - (gameState.step_count % 80) / 10);
        const delta = best ? best.heuristic - candidates[0].heuristic : 0;
        const accept = Math.min(1, Math.exp(delta / Math.max(temperature, 0.1)));
        lines.push({ title: 'Temperature', text: `T = ${fmt(temperature, 2)} | cooling schedule still exploring risky moves.` });
        lines.push({ title: 'Acceptance', text: `Delta energy ${fmt(delta, 2)} | accept probability ${fmt(accept * 100, 1)}%.` });
    } else if (algoId === 'minimax') {
        lines.push({ title: 'Alpha-beta', text: 'The tree highlights how some opponent branches can be cut early.' });
        lines.push({ title: 'Utility', text: `Best candidate is ${best ? best.label : 'n/a'} with utility ${best ? fmt(best.heuristic, 2) : 'n/a'}.` });
    } else if (algoId === 'expectimax') {
        lines.push({ title: 'Expected value', text: 'Instead of worst-case pruning only, the tree blends chance and choice.' });
        lines.push({ title: 'Utility', text: `Expected action is ${best ? best.label : 'n/a'}.` });
    } else if (algoId === 'backtracking') {
        lines.push({ title: 'Constraint pruning', text: 'Invalid or unsafe branches are removed as soon as they violate constraints.' });
        lines.push({ title: 'Consistency', text: 'The trace favors states that preserve reachability and freedom of movement.' });
    } else if (algoId === 'online_search') {
        lines.push({ title: 'Partial observability', text: 'The agent replans after every new percept instead of trusting the full map.' });
        lines.push({ title: 'Local policy', text: 'This view is ideal when Fog of War hides large parts of the arena.' });
    } else if (algoId === 'and_or_search') {
        lines.push({ title: 'AND / OR nodes', text: 'The tree combines controllable choice nodes with contingency nodes.' });
        lines.push({ title: 'Robustness', text: 'A plan is kept only if the risky alternatives still remain viable.' });
    } else {
        lines.push({ title: 'Overview', text: 'This algorithm visual trace is scaffolded to make the thought process readable.' });
        lines.push({ title: 'Best action', text: `${best ? best.label : 'n/a'} currently looks strongest in this scenario.` });
    }
    return lines;
}

function fmt(value, digits = 1) {
    if (value == null || Number.isNaN(Number(value))) return 'n/a';
    return Number(value).toFixed(digits);
}

function renderLabMetaCards(trace) {
    if (!el.labMetaCards) return;
    el.labMetaCards.innerHTML = '';
    trace.metaCards.forEach((card) => {
        const node = document.createElement('div');
        node.className = 'mini-card';
        node.innerHTML = `<div class="label">${card.label}</div><div class="value">${card.value}</div>`;
        el.labMetaCards.appendChild(node);
    });
}

function renderList(container, items) {
    if (!container) return;
    container.innerHTML = '';
    if (!items.length) {
        container.innerHTML = '<div class="list-item"><strong>No entries</strong><span>Nothing to show yet.</span></div>';
        return;
    }
    items.forEach((item) => {
        const row = document.createElement('div');
        row.className = 'list-item';
        row.innerHTML = `<strong>${item.title}</strong><span>${item.text}</span>`;
        container.appendChild(row);
    });
}

function renderNodeDetails(node) {
    if (!el.labNodeDetails) return;
    if (!node) {
        el.labNodeDetails.innerHTML = '<h4>Node details</h4><p>Select a node to inspect its metadata.</p>';
        return;
    }
    const meta = Array.isArray(node.meta) ? node.meta.join(' · ') : node.meta;
    el.labNodeDetails.innerHTML = `<h4>${node.title}</h4><p>${node.detail || ''}</p><p style="margin-top:8px; color: var(--cyan); font-family:'IBM Plex Mono', monospace; font-size:0.78rem;">${meta || ''}</p>`;
}

function renderTree(trace) {
    if (!el.labTreeCanvas || !el.labTreeEdges) return;
    state.trace = trace;
    if (!state.traceSelectedNodeId) {
        state.traceSelectedNodeId = trace.selectedNodeId || trace.nodes[0]?.id || null;
    } else if (!trace.nodes.some((node) => node.id === state.traceSelectedNodeId)) {
        state.traceSelectedNodeId = trace.selectedNodeId || trace.nodes[0]?.id || null;
    }

    const selected = trace.nodes.find((node) => node.id === state.traceSelectedNodeId) || trace.nodes[0];
    renderNodeDetails(selected);

    const width = Math.max(...trace.nodes.map((n) => n.x + (n.width || 210)), 2200);
    const height = Math.max(...trace.nodes.map((n) => n.y + (n.height || 96)), 1200);
    el.labTreeCanvas.style.width = `${width + 260}px`;
    el.labTreeCanvas.style.height = `${height + 180}px`;
    el.labTreeEdges.setAttribute('width', `${width + 260}`);
    el.labTreeEdges.setAttribute('height', `${height + 180}`);
    el.labTreeEdges.setAttribute('viewBox', `0 0 ${width + 260} ${height + 180}`);
    el.labTreeCanvas.innerHTML = '';
    el.labTreeEdges.innerHTML = '';

    trace.edges.forEach((edge) => {
        const from = trace.nodes.find((node) => node.id === edge.from);
        const to = trace.nodes.find((node) => node.id === edge.to);
        if (!from || !to) return;
        const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        line.setAttribute('x1', `${from.x + (from.width || 210) / 2}`);
        line.setAttribute('y1', `${from.y + (from.height || 96)}`);
        line.setAttribute('x2', `${to.x + (to.width || 210) / 2}`);
        line.setAttribute('y2', `${to.y}`);
        line.setAttribute('stroke', 'rgba(148, 163, 184, 0.35)');
        line.setAttribute('stroke-width', '2');
        line.setAttribute('stroke-dasharray', '7 6');
        el.labTreeEdges.appendChild(line);
    });

    trace.nodes.forEach((node) => {
        const box = document.createElement('div');
        box.className = `tree-node ${node.id === state.traceSelectedNodeId ? 'is-selected' : ''}`;
        box.style.left = `${node.x}px`;
        box.style.top = `${node.y}px`;
        box.style.width = `${node.width || 210}px`;
        box.innerHTML = `
            <div class="kind">${node.kind}</div>
            <div class="title">${node.title}</div>
            <div class="meta">${Array.isArray(node.meta) ? node.meta.map((m) => `<div>${m}</div>`).join('') : node.meta || ''}</div>
        `;
        box.addEventListener('click', () => {
            state.traceSelectedNodeId = node.id;
            renderTree(trace);
        });
        el.labTreeCanvas.appendChild(box);
    });

    applyTreeTransform();
}

function applyTreeTransform() {
    if (!el.labTreeCanvas) return;
    const { x, y, scale } = state.treeTransform;
    el.labTreeCanvas.style.transform = `translate(${x}px, ${y}px) scale(${scale})`;
    if (el.labTreeEdges) {
        el.labTreeEdges.style.transform = `translate(${x}px, ${y}px) scale(${scale})`;
    }
}

function setupTreeInteractions() {
    if (!el.labTreeStage) return;
    el.labTreeStage.addEventListener('pointerdown', (event) => {
        if (event.target.closest('.tree-node')) return;
        state.treeDrag.active = true;
        state.treeDrag.lastX = event.clientX;
        state.treeDrag.lastY = event.clientY;
        el.labTreeStage.setPointerCapture?.(event.pointerId);
    });
    el.labTreeStage.addEventListener('pointermove', (event) => {
        if (!state.treeDrag.active) return;
        const dx = event.clientX - state.treeDrag.lastX;
        const dy = event.clientY - state.treeDrag.lastY;
        state.treeDrag.lastX = event.clientX;
        state.treeDrag.lastY = event.clientY;
        state.treeTransform.x += dx;
        state.treeTransform.y += dy;
        applyTreeTransform();
    });
    window.addEventListener('pointerup', () => {
        state.treeDrag.active = false;
    });
    el.labTreeStage.addEventListener('wheel', (event) => {
        event.preventDefault();
        const delta = event.deltaY > 0 ? -0.08 : 0.08;
        state.treeTransform.scale = clamp(state.treeTransform.scale + delta, 0.35, 1.6);
        applyTreeTransform();
    }, { passive: false });
}

function renderLogs() {
    if (!el.labEventLog) return;
    const query = (el.labLogSearch?.value || '').trim().toLowerCase();
    const agentFilter = el.labAgentFilter?.value || 'all';
    el.labEventLog.innerHTML = '';
    const filtered = state.logs.filter((log) => {
        const matchesQuery = !query
            || `${log.time} ${log.step} ${log.agent} ${log.action} ${log.detail}`.toLowerCase().includes(query);
        const matchesAgent = agentFilter === 'all' || log.filterAgent === agentFilter || (agentFilter === 'system' && log.filterAgent === 'system');
        return matchesQuery && matchesAgent;
    });

    if (!filtered.length) {
        el.labEventLog.innerHTML = '<div class="list-item"><strong>No log entries</strong><span>Run the game to populate the trace.</span></div>';
        return;
    }

    filtered.forEach((log) => {
        const row = document.createElement('div');
        row.className = 'log-row';
        row.innerHTML = `
            <div class="time">${log.time}</div>
            <div class="step">#${log.step}</div>
            <div class="agent">${log.agent}</div>
            <div class="detail"><strong>${log.action}</strong><div style="color: var(--muted); margin-top: 4px;">${log.detail}</div></div>
        `;
        el.labEventLog.appendChild(row);
    });
}

function renderExperimentScaffold() {
    // static layout only
}

function refreshLab() {
    if (!state.game) return;
    const trace = buildTrace(state.game);
    renderLabMetaCards(trace);
    renderList(el.labFrontier, trace.frontier);
    renderList(el.labClosed, trace.closed);
    renderList(el.labInsight, trace.insight);
    renderTree(trace);
    updateLabFilters();
}

function updateLabFilters() {
    if (!el.labAgentFilter) return;
    const selected = el.labAgentFilter.value || 'all';
    const options = [
        { value: 'all', label: 'All agents' },
        { value: 'player_1', label: 'P1' },
        { value: 'player_2', label: 'P2' },
        { value: 'player_3', label: 'P3' },
        { value: 'player_4', label: 'P4' },
        { value: 'system', label: 'System' },
    ];
    populateSelect(el.labAgentFilter, options, selected);
}

function collectActions(manualAction = ACTIONS.STOP) {
    const actions = {};
    if (state.agentConfigs.player_1 === 'manual') {
        actions.player_1 = manualAction;
    }
    return actions;
}

async function initGame() {
    extractSettingsFromUI();
    setConnection('loading', 'Connecting', 'Initializing the simulation');

    const payload = {
        agent_configs: state.agentConfigs,
        fog_of_war: state.fowEnabled,
        fow_radius: state.fowRadius,
        map_preset: state.mapPreset,
        seed: state.seed,
        agent_count: state.agentCount,
    };

    try {
        const response = await fetch(`${API_URL}/api/init`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
        });
        if (!response.ok) throw new Error('init failed');
        const data = await response.json();
        state.previousGame = null;
        state.game = data.state;
        if (data.agent_configs) {
            state.agentConfigs = data.agent_configs;
        }
        if (data.settings) {
            state.fowEnabled = !!data.settings.fog_of_war;
            state.fowRadius = data.settings.fow_radius || state.fowRadius;
            state.mapPreset = data.settings.map_preset || state.mapPreset;
            state.seed = data.settings.seed || state.seed;
            state.agentCount = data.settings.agent_count || state.agentCount;
        }
        syncUIFromState();
        updateAgentCountUI();
        setBoardPlaceholder(false);
        setConnection('ready', 'Online', 'Backend connected successfully');
        state.running = false;
        state.matchStatus = 'ready';
        setGameModeLabel();
        updateFromState(data.state);
        addLog({
            time: nowStamp(),
            step: data.state.step_count || 0,
            agent: 'SYSTEM',
            action: 'Initialization',
            detail: `Map preset ${state.mapPreset}, seed ${state.seed}, agents ${state.agentCount}, FOW ${state.fowEnabled ? 'on' : 'off'}.`,
            filterAgent: 'system',
        });
        refreshLab();
    } catch (error) {
        console.error(error);
        setConnection('offline', 'Offline', 'Backend unavailable');
        setBoardPlaceholder(true);
    }
}

function updateFromState(nextState, response) {
    state.previousGame = state.game;
    state.game = nextState;
    if (response?.status === 'game_over') {
        state.matchStatus = 'game_over';
    } else if (state.running) {
        state.matchStatus = 'running';
    } else {
        state.matchStatus = 'paused';
    }
    renderBoard();
    renderStatus();
    setGameModeLabel();
    refreshLab();
    pushActionLogs(state.previousGame, state.game, response);
    renderLogs();
}

async function stepGame(manualAction = ACTIONS.STOP) {
    if (!state.game) return;
    const actions = collectActions(manualAction);
    try {
        const response = await fetch(`${API_URL}/api/step`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ actions }),
        });
        if (!response.ok) throw new Error('step failed');
        const data = await response.json();
        updateFromState(data.state, data);
        if (data.status === 'game_over') {
            stopLoop();
            setConnection('ready', 'Online', 'Match complete');
            addLog({
                time: nowStamp(),
                step: data.state.step_count,
                agent: 'SYSTEM',
                action: 'Game Over',
                detail: 'The current match finished and the simulation stopped.',
                filterAgent: 'system',
            });
        }
    } catch (error) {
        console.error(error);
        setConnection('offline', 'Offline', 'Could not advance the match');
        stopLoop();
    }
}

function startLoop() {
    stopLoop();
    state.running = true;
    state.matchStatus = 'running';
    state.intervalId = window.setInterval(() => {
        stepGame(ACTIONS.STOP);
    }, state.speedMs);
}

function stopLoop() {
    if (state.intervalId) {
        clearInterval(state.intervalId);
        state.intervalId = null;
    }
    state.running = false;
    if (state.game && state.matchStatus !== 'game_over') {
        state.matchStatus = 'paused';
    }
}

function restartLoop() {
    if (!state.running) return;
    startLoop();
}

async function resetGame() {
    stopLoop();
    await initGame();
}

function syncUIFromState() {
    if (el.gameViewSelect) el.gameViewSelect.value = state.gameMode;
    if (el.fowToggle) el.fowToggle.checked = state.fowEnabled;
    if (el.fowRadius) el.fowRadius.value = `${state.fowRadius}`;
    if (el.mapSelect) el.mapSelect.value = state.mapPreset;
    if (el.seedInput) el.seedInput.value = `${state.seed}`;
    if (el.agentCount) el.agentCount.value = `${state.agentCount}`;
    if (el.speedSlider) el.speedSlider.value = `${state.speedMs}`;
    if (el.speedValue) el.speedValue.textContent = `${state.speedMs} ms`;
    setGameModeLabel();
}

function setupEvents() {
    document.querySelectorAll('.topnav button').forEach((button) => {
        button.addEventListener('click', () => {
            document.getElementById(button.dataset.target)?.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
    });

    el.gameViewSelect.addEventListener('change', () => {
        state.gameMode = el.gameViewSelect.value;
        setGameModeLabel();
        renderBoard();
        refreshLab();
    });
    el.fowToggle.addEventListener('change', () => {
        state.fowEnabled = el.fowToggle.checked;
        renderBoard();
        refreshLab();
    });
    el.fowRadius.addEventListener('change', () => {
        state.fowRadius = clamp(Number(el.fowRadius.value || 4), 1, 6);
        el.fowRadius.value = `${state.fowRadius}`;
        renderBoard();
        refreshLab();
    });
    el.focusAgentSelect.addEventListener('change', () => {
        state.focusAgent = el.focusAgentSelect.value;
        el.labFocusSelect.value = state.focusAgent;
        renderBoard();
        refreshLab();
    });
    el.labFocusSelect.addEventListener('change', () => {
        state.focusAgent = el.labFocusSelect.value;
        el.focusAgentSelect.value = state.focusAgent;
        renderBoard();
        refreshLab();
    });
    el.speedSlider.addEventListener('input', () => setSpeed(Number(el.speedSlider.value)));
    el.mapSelect.addEventListener('change', () => { state.mapPreset = el.mapSelect.value; });
    el.seedInput.addEventListener('change', () => { state.seed = Number(el.seedInput.value || 42); });
    el.agentCount.addEventListener('change', () => {
        updateAgentCountUI();
        populateAgentSelects();
    });
    [el.p1Select, el.p2Select, el.p3Select, el.p4Select].forEach((select) => {
        select.addEventListener('change', () => {
            state.agentConfigs = {
                player_1: el.p1Select.value || 'manual',
                player_2: el.p2Select.value || 'minimax',
                player_3: el.p3Select.value || 'minimax',
                player_4: el.p4Select.value || 'minimax',
            };
        });
    });

    el.startBtn.addEventListener('click', async () => {
        await initGame();
        startLoop();
    });
    el.pauseBtn.addEventListener('click', stopLoop);
    el.resumeBtn.addEventListener('click', () => {
        if (state.game) startLoop();
    });
    el.resetBtn.addEventListener('click', resetGame);
    el.labRefreshBtn.addEventListener('click', refreshLab);
    el.labAlgorithmSelect.addEventListener('change', refreshLab);
    el.labScenarioSelect.addEventListener('change', refreshLab);
    el.labViewSelect.addEventListener('change', refreshLab);
    el.labLogSearch.addEventListener('input', renderLogs);
    el.labAgentFilter.addEventListener('change', renderLogs);
    el.labClearLog.addEventListener('click', () => {
        state.logs = [];
        renderLogs();
    });

    window.addEventListener('resize', () => renderBoard());

    window.addEventListener('keydown', (event) => {
        if (event.target && ['INPUT', 'SELECT', 'TEXTAREA'].includes(event.target.tagName)) return;
        if (!state.game) return;
        if (state.agentConfigs.player_1 !== 'manual') return;
        let action = null;
        switch (event.key) {
            case 'ArrowUp':
            case 'w':
            case 'W':
                action = ACTIONS.UP; break;
            case 'ArrowDown':
            case 's':
            case 'S':
                action = ACTIONS.DOWN; break;
            case 'ArrowLeft':
            case 'a':
            case 'A':
                action = ACTIONS.LEFT; break;
            case 'ArrowRight':
            case 'd':
            case 'D':
                action = ACTIONS.RIGHT; break;
            case ' ':
            case 'b':
            case 'B':
                action = ACTIONS.BOMB; break;
            case 'Enter':
                action = ACTIONS.STOP; break;
            default:
                return;
        }
        event.preventDefault();
        stepGame(action);
    });

    setupTreeInteractions();
}

async function loadBackendAgents() {
    try {
        const response = await fetch(`${API_URL}/api/agents`);
        if (!response.ok) throw new Error('Unable to fetch agents');
        const data = await response.json();
        state.availableAgents = data.agents || [];
    } catch (error) {
        console.warn('Falling back to a local agent list.', error);
        state.availableAgents = [
            { id: 'bfs', name: 'BFS' },
            { id: 'dfs', name: 'DFS' },
            { id: 'astar', name: 'A*' },
            { id: 'greedy', name: 'Greedy' },
            { id: 'hill_climbing', name: 'Hill Climbing' },
            { id: 'simulated_annealing', name: 'Simulated Annealing' },
            { id: 'and_or_search', name: 'AND-OR Search' },
            { id: 'online_search', name: 'Online Search (LRTA*)' },
            { id: 'backtracking', name: 'Backtracking' },
            { id: 'minimax', name: 'Minimax' },
            { id: 'expectimax', name: 'Expectimax' },
            { id: 'random', name: 'Random' },
            { id: 'min_conflicts', name: 'Min-Conflicts' },
        ];
    }
}

function initStaticControls() {
    populateMapSelect();
    populateSelect(el.gameViewSelect, [
        { value: 'god', label: 'God View' },
        { value: 'agent', label: 'Agent View' },
    ], 'god');
    populateSelect(el.labViewSelect, [
        { value: 'god', label: 'God View' },
        { value: 'agent', label: 'Agent View' },
    ], 'god');
    populateSelect(el.labScenarioSelect, [
        { value: 'bomb_escape', label: 'Bomb Escape' },
        { value: 'item_hunt', label: 'Item Hunt' },
        { value: 'enemy_pressure', label: 'Enemy Pressure' },
        { value: 'open_field', label: 'Open Field' },
    ], 'bomb_escape');
    updateLabFilters();
}

async function bootstrap() {
    setConnection('loading', 'Connecting', 'Bootstrapping the dashboard');
    initStaticControls();
    setupEvents();
    await loadBackendAgents();
    populateAgentSelects();
    populateLabAlgorithmSelect();
    syncUIFromState();
    updateAgentCountUI();
    await initGame();
    renderLogs();
    renderExperimentScaffold();
}

bootstrap();
