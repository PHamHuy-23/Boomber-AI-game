const API_URL = 'http://127.0.0.1:8000';

// Global state
const state = {
    activeTab: 'game-tab',
    sidebarCollapsed: false,
    isConnected: false,
    
    // Module 1: Playground
    game: null,
    gameStatus: 'ready', // 'ready', 'running', 'paused', 'game_over'
    agentCount: 4,
    mapPreset: 'classic',
    seed: 42,
    speedMs: 300,
    intervalId: null,
    fowEnabled: false,
    fowRadius: 4,
    agentConfigs: {
        player_1: 'minimax',
        player_2: 'minimax',
        player_3: 'expectimax',
        player_4: 'astar'
    },
    
    // Module 2: Tactical Lab
    labScenario: 'hazard_escape',
    labAlgo: 'astar',
    labTick: 0,
    labHistory: [], // stores steps history for frame-by-frame scrubbing
    labPlaying: false,
    labIntervalId: null,
    labShowOverlay: true,
    
    // Module 3: Analytics Dashboard
    analyticsSource: 'csv',
    csvMatches: [],
    analyticsOverview: null,
    analyticsCompare: null,
    matches: [],
    selectedReplayMatch: null,
    replaySteps: [],
    replayTick: 0,
    replayPlaying: false,
    replayIntervalId: null,
    replayOverlayMode: 'normal' // 'normal', 'heatmap'
};

// UI Elements mapping
const el = {
    // Sidebar & layout
    sidebar: document.getElementById('app-sidebar'),
    collapseBtn: document.getElementById('collapse-btn'),
    collapseIcon: document.getElementById('collapse-icon'),
    pageTitle: document.getElementById('page-display-title'),
    connIndicator: document.getElementById('conn-indicator'),
    connText: document.getElementById('conn-text'),
    navItems: document.querySelectorAll('.nav-item'),
    sections: document.querySelectorAll('.dashboard-section'),
    
    // Module 1: Playground
    pgStart: document.getElementById('pg-start-btn'),
    pgPause: document.getElementById('pg-pause-btn'),
    pgReset: document.getElementById('pg-reset-btn'),
    pgStep: document.getElementById('pg-step-btn'),
    pgSpeedSlider: document.getElementById('pg-speed-slider'),
    pgSpeedVal: document.getElementById('pg-speed-val'),
    pgMapPreset: document.getElementById('pg-map-preset'),
    pgSeed: document.getElementById('pg-seed'),
    pgAgentCount: document.getElementById('pg-agent-count'),
    pgFowChk: document.getElementById('pg-fow-chk'),
    pgFowRadiusGroup: document.getElementById('pg-fow-radius-group'),
    pgFowRadius: document.getElementById('pg-fow-radius'),
    
    pgBoard: document.getElementById('game-playground-board'),
    pgFps: document.getElementById('board-fps'),
    pgTick: document.getElementById('board-tick'),
    pgTime: document.getElementById('board-time'),
    
    pgAlgoP1: document.getElementById('pg-algo-p1'),
    pgAlgoP2: document.getElementById('pg-algo-p2'),
    pgAlgoP3: document.getElementById('pg-algo-p3'),
    pgAlgoP4: document.getElementById('pg-algo-p4'),
    
    telP1: document.getElementById('tel-p1'),
    telP2: document.getElementById('tel-p2'),
    telP3: document.getElementById('tel-p3'),
    telP4: document.getElementById('tel-p4'),
    
    // Module 2: Tactical Lab
    scenarioItems: document.querySelectorAll('.scenario-item'),
    labSmallBoard: document.getElementById('lab-small-board'),
    labTickVal: document.getElementById('lab-tick'),
    labAlgorithm: document.getElementById('lab-algorithm'),
    labDecisionLog: document.getElementById('lab-decision-log'),
    labOverlayChk: document.getElementById('lab-overlay-chk'),
    
    labPlay: document.getElementById('lab-play-btn'),
    labPrev: document.getElementById('lab-prev-btn'),
    labNext: document.getElementById('lab-next-btn'),
    labReplay: document.getElementById('lab-replay-btn'),
    
    // Module 3: Analytics Dashboard
    btnAnalyticsCsv: document.getElementById('btn-analytics-csv'),
    btnAnalyticsDb: document.getElementById('btn-analytics-db'),
    cardTotalMatches: document.getElementById('card-total-matches'),
    cardAvgLatency: document.getElementById('card-avg-latency'),
    cardAvgScore: document.getElementById('card-avg-score'),
    cardResources: document.getElementById('card-resources'),
    
    replayMatchesList: document.getElementById('replay-matches-list'),
    repMatchDisplay: document.getElementById('rep-match-display'),
    repTickDisplay: document.getElementById('rep-tick-display'),
    replayBoard: document.getElementById('replay-board'),
    repEvents: document.getElementById('rep-events'),
    
    repPlay: document.getElementById('rep-play-btn'),
    repPrev: document.getElementById('rep-prev-btn'),
    repNext: document.getElementById('rep-next-btn'),
    repScrub: document.getElementById('rep-scrub'),
    
    exportCsvBtn: document.getElementById('export-csv'),
    exportJsonBtn: document.getElementById('export-json'),
    exportPngBtn: document.getElementById('export-png'),
};

// Chart instances
let chartWinrateInstance = null;
let chartNodesInstance = null;
let chartHorizonInstance = null;
let chartTacticalInstance = null;

// Initialization
document.addEventListener('DOMContentLoaded', () => {
    setupTabNavigation();
    setupSidebarCollapse();
    setupPlaygroundHandlers();
    setupLabHandlers();
    setupAnalyticsHandlers();
    
    // Initial health check and fetch database stats
    checkServerConnection();
    setInterval(checkServerConnection, 5000);
    
    // Start by initializing playground board visually
    initPlaygroundGame();
});

// Sidebar & Tabs Navigation
function setupTabNavigation() {
    el.navItems.forEach(item => {
        item.addEventListener('click', () => {
            el.navItems.forEach(i => i.classList.remove('active'));
            item.classList.add('active');
            
            const tabId = item.getAttribute('data-tab');
            state.activeTab = tabId;
            
            el.sections.forEach(section => {
                section.classList.remove('active');
                if (section.id === tabId) {
                    section.classList.add('active');
                }
            });
            
            // Set header title
            const labelText = item.querySelector('.nav-label').textContent;
            el.pageTitle.textContent = labelText;
            
            // If switched to analytics tab, refresh database data
            if (tabId === 'analytics-tab') {
                loadAnalyticsData();
            }
        });
    });
}

function setupSidebarCollapse() {
    el.collapseBtn.addEventListener('click', () => {
        state.sidebarCollapsed = !state.sidebarCollapsed;
        if (state.sidebarCollapsed) {
            el.sidebar.classList.add('collapsed');
            el.collapseIcon.innerHTML = `
                <polyline points="13 17 18 12 13 7"></polyline>
                <polyline points="6 17 11 12 6 7"></polyline>
            `;
        } else {
            el.sidebar.classList.remove('collapsed');
            el.collapseIcon.innerHTML = `
                <polyline points="11 17 6 12 11 7"></polyline>
                <polyline points="18 17 13 12 18 7"></polyline>
            `;
        }
    });
}

// Server Health Monitoring
async function checkServerConnection() {
    try {
        const res = await fetch(`${API_URL}/`);
        if (res.ok) {
            state.isConnected = true;
            el.connIndicator.className = 'status-indicator online';
            el.connText.textContent = 'FastAPI Server Connected';
        } else {
            throw new Error();
        }
    } catch (e) {
        state.isConnected = false;
        el.connIndicator.className = 'status-indicator offline';
        el.connText.textContent = 'Server Offline';
    }
}

// ----------------------------------------------------
// MODULE 1: GAME PLAYGROUND LOGIC
// ----------------------------------------------------
function setupPlaygroundHandlers() {
    el.pgStart.addEventListener('click', startPlaygroundGame);
    el.pgPause.addEventListener('click', pausePlaygroundGame);
    el.pgReset.addEventListener('click', initPlaygroundGame);
    el.pgStep.addEventListener('click', stepPlaygroundGame);
    
    // Sliders
    el.pgSpeedSlider.addEventListener('input', (e) => {
        state.speedMs = parseInt(e.target.value);
        el.pgSpeedVal.textContent = `${state.speedMs}ms`;
        if (state.gameStatus === 'running') {
            pausePlaygroundGame();
            startPlaygroundGame();
        }
    });
    
    // Checkboxes
    el.pgFowChk.addEventListener('change', (e) => {
        state.fowEnabled = e.target.checked;
        el.pgFowRadiusGroup.style.display = state.fowEnabled ? 'flex' : 'none';
        renderGameBoard(state.game, 'game-playground-board', 'player_1');
    });
    
    el.pgFowRadius.addEventListener('change', (e) => {
        state.fowRadius = parseInt(e.target.value) || 4;
        renderGameBoard(state.game, 'game-playground-board', 'player_1');
    });

    // Keyboard bindings for manual movement (player_1)
    window.addEventListener('keydown', (e) => {
        if (state.activeTab !== 'game-tab' || state.gameStatus !== 'running') return;
        
        let actionKey = null;
        if (e.key === 'ArrowUp' || e.key === 'w' || e.key === 'W') actionKey = 3; // UP
        if (e.key === 'ArrowDown' || e.key === 's' || e.key === 'S') actionKey = 4; // DOWN
        if (e.key === 'ArrowLeft' || e.key === 'a' || e.key === 'A') actionKey = 1; // LEFT
        if (e.key === 'ArrowRight' || e.key === 'd' || e.key === 'D') actionKey = 2; // RIGHT
        if (e.key === ' ' || e.key === 'Enter') actionKey = 5; // BOMB
        
        if (actionKey !== null && el.pgAlgoP1.value === 'manual') {
            e.preventDefault();
            // Trigger a game step immediately with user action
            stepPlaygroundGame(actionKey);
        }
    });
    
    // Hide / Show Config Blocks based on Player count selection
    el.pgAgentCount.addEventListener('change', (e) => {
        state.agentCount = parseInt(e.target.value);
        updateAgentConfigsUI();
        initPlaygroundGame();
    });
    
    updateAgentConfigsUI();
}

function updateAgentConfigsUI() {
    document.getElementById('block-p3').style.opacity = state.agentCount >= 3 ? '1' : '0.35';
    document.getElementById('pg-algo-p3').disabled = state.agentCount < 3;
    
    document.getElementById('block-p4').style.opacity = state.agentCount >= 4 ? '1' : '0.35';
    document.getElementById('pg-algo-p4').disabled = state.agentCount < 4;
}

async function initPlaygroundGame() {
    // Stop loop if running
    if (state.intervalId) {
        clearInterval(state.intervalId);
        state.intervalId = null;
    }
    
    state.gameStatus = 'ready';
    el.pgStart.disabled = false;
    el.pgStart.textContent = 'Start';
    el.pgPause.disabled = true;
    el.pgPause.textContent = 'Pause';
    el.pgStep.disabled = false;
    
    // Reset telemetry view
    for (let i = 1; i <= 4; i++) {
        document.getElementById(`tel-p${i}`).style.display = 'none';
    }
    
    if (!state.isConnected) {
        // Mock simple empty grid on server offline
        drawEmptyBoard('game-playground-board', 15, 13);
        return;
    }
    
    try {
        const configs = {
            player_1: el.pgAlgoP1.value,
            player_2: el.pgAlgoP2.value,
            player_3: el.pgAlgoP3.value,
            player_4: el.pgAlgoP4.value
        };
        
        const res = await fetch(`${API_URL}/api/init`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                agent_configs: configs,
                map_preset: el.pgMapPreset.value,
                seed: parseInt(el.pgSeed.value) || 42,
                agent_count: state.agentCount
            })
        });
        
        if (res.ok) {
            const data = await res.json();
            state.game = data.state;
            state.agentConfigs = data.agent_configs;
            
            // Show telemetry rows
            for (let i = 1; i <= state.agentCount; i++) {
                document.getElementById(`tel-p${i}`).style.display = 'grid';
            }
            
            updateTelemetry(state.game);
            renderGameBoard(state.game, 'game-playground-board', 'player_1');
            
            el.pgTick.textContent = '0';
            el.pgTime.textContent = '300s';
            el.pgFps.textContent = '0';
        }
    } catch (e) {
        console.error("Failed to initialize playground", e);
    }
}

function startPlaygroundGame() {
    if (state.gameStatus === 'game_over') return;
    
    state.gameStatus = 'running';
    el.pgStart.disabled = true;
    el.pgPause.disabled = false;
    el.pgPause.textContent = 'Pause';
    el.pgStep.disabled = true;
    
    state.intervalId = setInterval(() => {
        stepPlaygroundGame();
    }, state.speedMs);
}

function pausePlaygroundGame() {
    state.gameStatus = 'paused';
    el.pgStart.disabled = false;
    el.pgStart.textContent = 'Resume';
    el.pgPause.disabled = true;
    
    if (state.intervalId) {
        clearInterval(state.intervalId);
        state.intervalId = null;
    }
}

async function stepPlaygroundGame(userAction = 0) {
    if (!state.game || state.gameStatus === 'game_over') return;
    
    const actions = {};
    // If player_1 is manual, inject user keys action
    if (el.pgAlgoP1.value === 'manual') {
        actions['player_1'] = userAction;
    }
    
    const t0 = performance.now();
    try {
        const res = await fetch(`${API_URL}/api/step`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ actions })
        });
        
        if (res.ok) {
            const data = await res.json();
            state.game = data.state;
            
            const t1 = performance.now();
            const latency = Math.round(t1 - t0);
            el.pgFps.textContent = Math.min(60, Math.round(1000 / Math.max(1, latency)));
            
            updateTelemetry(state.game);
            renderGameBoard(state.game, 'game-playground-board', 'player_1');
            
            el.pgTick.textContent = state.game.step_count;
            el.pgTime.textContent = `${300 - state.game.step_count}s`;
            
            if (data.status === 'game_over' || !data.game_continue) {
                gamePlaygroundOver();
            }
        }
    } catch (e) {
        console.error("Step execution failed", e);
        pausePlaygroundGame();
    }
}

function gamePlaygroundOver() {
    state.gameStatus = 'game_over';
    el.pgStart.disabled = true;
    el.pgPause.disabled = true;
    el.pgStep.disabled = true;
    
    if (state.intervalId) {
        clearInterval(state.intervalId);
        state.intervalId = null;
    }
    
    alert("Match Completed! Replay and metrics saved directly to SQLite.");
}

function updateTelemetry(game) {
    if (!game || !game.agents) return;
    
    for (let i = 1; i <= state.agentCount; i++) {
        const aid = `player_${i}`;
        const agent = game.agents[aid];
        if (!agent) continue;
        
        // Calculate a score
        const score = state.agentConfigs[aid] === 'manual' ? 0 : 
            (agent.is_alive ? 500 : 0) + agent.bomb_range * 100 + agent.max_bombs * 50;
            
        document.getElementById(`tel-p${i}-hp`).textContent = `${agent.lives} / ${score}`;
        document.getElementById(`tel-p${i}-stats`).textContent = `${agent.bombs_left}/${agent.max_bombs} | range ${agent.bomb_range}`;
        document.getElementById(`tel-p${i}-pos`).textContent = `(${agent.x}, ${agent.y})`;
        
        const stateEl = document.getElementById(`tel-p${i}-state`);
        stateEl.textContent = agent.is_alive ? 'Alive' : 'Eliminated';
        stateEl.style.color = agent.is_alive ? 'var(--accent-green)' : 'var(--accent-pink)';
    }
}

// ----------------------------------------------------
// BOARD RENDERING COMMON ENGINE
// ----------------------------------------------------
function drawEmptyBoard(containerId, w, h) {
    const container = document.getElementById(containerId);
    if (!container) return;
    
    container.innerHTML = '';
    container.style.gridTemplateColumns = `repeat(${w}, 34px)`;
    container.style.gridTemplateRows = `repeat(${h}, 34px)`;
    
    for (let y = 0; y < h; y++) {
        for (let x = 0; x < w; x++) {
            const cell = document.createElement('div');
            cell.className = `board-cell ${(x + y) % 2 === 0 ? 'cell-ground-even' : 'cell-ground-odd'}`;
            container.appendChild(cell);
        }
    }
}

function renderGameBoard(game, containerId, focusAgentId = 'player_1', path = []) {
    const container = document.getElementById(containerId);
    if (!game || !container) return;
    
    const w = game.width;
    const h = game.height;
    
    container.innerHTML = '';
    
    // Adaptive cell size on smaller laptops
    const maxCellSize = containerId === 'lab-small-board' ? 32 : 34;
    container.style.gridTemplateColumns = `repeat(${w}, ${maxCellSize}px)`;
    container.style.gridTemplateRows = `repeat(${h}, ${maxCellSize}px)`;
    
    // Calculate visible cells for Fog of War
    const visibleSet = new Set();
    const hasFow = state.fowEnabled && containerId === 'game-playground-board';
    
    if (hasFow && game.agents[focusAgentId] && game.agents[focusAgentId].is_alive) {
        const focusAgent = game.agents[focusAgentId];
        // Chebyshev distance radius
        for (let dy = -state.fowRadius; dy <= state.fowRadius; dy++) {
            for (let dx = -state.fowRadius; dx <= state.fowRadius; dx++) {
                const tx = focusAgent.x + dx;
                const ty = focusAgent.y + dy;
                if (tx >= 0 && tx < w && ty >= 0 && ty < h) {
                    visibleSet.add(`${tx},${ty}`);
                }
            }
        }
    } else {
        // all visible
        for (let y = 0; y < h; y++) {
            for (let x = 0; x < w; x++) {
                visibleSet.add(`${x},${y}`);
            }
        }
    }
    
    for (let y = 0; y < h; y++) {
        for (let x = 0; x < w; x++) {
            const cell = document.createElement('div');
            cell.style.width = `${maxCellSize}px`;
            cell.style.height = `${maxCellSize}px`;
            
            const cellKey = `${x},${y}`;
            
            if (!visibleSet.has(cellKey)) {
                cell.className = 'board-cell cell-fog';
                container.appendChild(cell);
                continue;
            }
            
            const tile = game.grid[y][x];
            let cellClass = `board-cell ${(x + y) % 2 === 0 ? 'cell-ground-even' : 'cell-ground-odd'}`;
            
            if (tile === 1) cellClass += ' cell-wall';
            else if (tile === 2) cellClass += ' cell-brick';
            else if (tile === 3) cellClass += ' cell-bomb';
            else if (tile === 4) {
                const isOrigin = game.explosion_origins && game.explosion_origins.some(coord => coord[0] === x && coord[1] === y);
                if (isOrigin) {
                    cellClass += ' cell-explosion-center';
                } else {
                    const isUpExplosion = (y > 0 && game.grid[y-1][x] === 4);
                    const isDownExplosion = (y < h - 1 && game.grid[y+1][x] === 4);
                    if (isUpExplosion || isDownExplosion) {
                        cellClass += ' cell-explosion-vertical';
                    } else {
                        cellClass += ' cell-explosion-horizontal';
                    }
                }
            }
            else if (tile === 5) cellClass += ' cell-item-radius';
            else if (tile === 6) cellClass += ' cell-item-capacity';
            
            // Highlight path overlay if specified
            if (path && path.some(coord => coord[0] === x && coord[1] === y)) {
                cellClass += ' cell-path';
            }
            
            cell.className = cellClass;
            
            // Check for agents standing on this cell
            if (game.agents) {
                for (const aid in game.agents) {
                    const agent = game.agents[aid];
                    if (agent.x === x && agent.y === y) {
                        const avatar = document.createElement('div');
                        avatar.className = `cell-agent agent-${aid === 'player_1' ? 'p1' : aid === 'player_2' ? 'p2' : aid === 'player_3' ? 'p3' : 'p4'}`;
                        
                        const dir = (agent.direction || 'down').toLowerCase();
                        avatar.classList.add(`dir-${dir}`);
                        
                        if (!agent.is_alive) {
                            avatar.classList.add('agent-dead');
                        }
                        avatar.textContent = aid === 'player_1' ? '1' : aid === 'player_2' ? '2' : aid === 'player_3' ? '3' : '4';
                        cell.appendChild(avatar);
                    }
                }
            }
            
            container.appendChild(cell);
        }
    }
}

// ----------------------------------------------------
// MODULE 2: TACTICAL SCENARIO LABORATORY
// ----------------------------------------------------
function setupLabHandlers() {
    el.scenarioItems.forEach(item => {
        item.addEventListener('click', () => {
            el.scenarioItems.forEach(i => i.classList.remove('active'));
            item.classList.add('active');
            
            state.labScenario = item.getAttribute('data-scenario');
            initLabScenario();
        });
    });
    
    el.labAlgorithm.addEventListener('change', (e) => {
        state.labAlgo = e.target.value;
        initLabScenario();
    });
    
    el.labPlay.addEventListener('click', toggleLabPlayback);
    el.labPrev.addEventListener('click', prevLabTick);
    el.labNext.addEventListener('click', nextLabTick);
    el.labReplay.addEventListener('click', initLabScenario);
    el.labOverlayChk.addEventListener('change', (e) => {
        state.labShowOverlay = e.target.checked;
        renderLabSmallBoard();
    });
    
    // Initial load
    initLabScenario();
}

async function initLabScenario() {
    if (state.labIntervalId) {
        clearInterval(state.labIntervalId);
        state.labIntervalId = null;
    }
    state.labPlaying = false;
    el.labPlay.textContent = 'Play';
    
    state.labTick = 0;
    state.labHistory = [];
    
    if (!state.isConnected) {
        drawEmptyBoard('lab-small-board', 7, 7);
        el.labDecisionLog.innerHTML = 'Server disconnected. Run backend to demonstrate reasoning logic.';
        return;
    }
    
    try {
        const configs = {
            player_1: state.labAlgo, // Force player_1 to run the selected algorithm in Sandbox
            player_2: 'random',
            player_3: 'random',
            player_4: 'random'
        };
        
        const res = await fetch(`${API_URL}/api/init`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                agent_configs: configs,
                scenario: state.labScenario
            })
        });
        
        if (res.ok) {
            const data = await res.json();
            // Save initial state into history
            state.labHistory.push(data.state);
            renderLabSmallBoard();
            updateLabDecisionLog(data.state);
        }
    } catch (e) {
        console.error("Failed to load scenario", e);
    }
}

function renderLabSmallBoard() {
    const curState = state.labHistory[state.labTick];
    if (!curState) return;
    
    el.labTickVal.textContent = state.labTick;
    
    // Get search path from current agent trace if available
    let pathCoords = [];
    const trace = curState.traces?.['player_1'];
    if (state.labShowOverlay && trace && trace.path) {
        // Trace path is a sequence of actions like ['RIGHT', 'UP'].
        // Let's compute coordinates based on actions starting from player_1's current position!
        const px = curState.agents['player_1']?.x;
        const py = curState.agents['player_1']?.y;
        if (px !== undefined && py !== undefined) {
            let cx = px;
            let cy = py;
            pathCoords.push([cx, cy]);
            
            trace.path.forEach(act => {
                if (act === 'LEFT') cx -= 1;
                if (act === 'RIGHT') cx += 1;
                if (act === 'UP') cy -= 1;
                if (act === 'DOWN') cy += 1;
                pathCoords.push([cx, cy]);
            });
        }
    }
    
    renderGameBoard(curState, 'lab-small-board', 'player_1', pathCoords);
}

function updateLabDecisionLog(curState) {
    if (!curState) return;
    
    const trace = curState.traces?.['player_1'];
    const logBox = el.labDecisionLog;
    logBox.innerHTML = '';
    
    if (!trace) {
        logBox.innerHTML = '<div class="log-line">No trace telemetry collected.</div>';
        return;
    }
    
    const h1 = document.createElement('div');
    h1.className = 'log-header';
    h1.innerHTML = `TICK ${state.labTick} | MODEL: <span class="log-highlight-cyan">${trace.algorithm.toUpperCase()}</span>`;
    logBox.appendChild(h1);
    
    if (trace.reasoning && Array.isArray(trace.reasoning)) {
        trace.reasoning.forEach(line => {
            const row = document.createElement('div');
            row.className = 'log-line';
            
            // Format highlights
            let formatted = line
                .replace(/(astar|bfs|dfs|minimax|expectimax|greedy|hill climbing|simulated annealing)/gi, '<span class="log-highlight-cyan">$1</span>')
                .replace(/(expanded|evaluated|temperature|acceptance|worse)/gi, '<span class="log-highlight-yellow">$1</span>')
                .replace(/(chosen|choice|optimal|best)/gi, '<span class="log-highlight-green">$1</span>')
                .replace(/(died|danger|suicide|explosion)/gi, '<span class="log-highlight-pink">$1</span>');
                
            row.innerHTML = formatted;
            logBox.appendChild(row);
        });
    }
    
    // For minimax/expectimax evaluations list
    if (trace.evaluations) {
        const title = document.createElement('div');
        title.className = 'log-line log-highlight-yellow';
        title.style.marginTop = '12px';
        title.textContent = 'Evaluations breakdown:';
        logBox.appendChild(title);
        
        for (const action in trace.evaluations) {
            const score = trace.evaluations[action];
            const item = document.createElement('div');
            item.className = 'log-line';
            item.style.paddingLeft = '14px';
            item.innerHTML = `Action <span class="log-highlight-cyan">${action}</span>: expected utility = <span class="log-highlight-green">${score.toFixed(1)}</span>`;
            logBox.appendChild(item);
        }
    }
}

async function nextLabTick() {
    // Check if we already computed the next state in our history
    if (state.labTick + 1 < state.labHistory.length) {
        state.labTick += 1;
        renderLabSmallBoard();
        updateLabDecisionLog(state.labHistory[state.labTick]);
        return;
    }
    
    // Otherwise, query a step forward from backend
    if (!state.isConnected) return;
    
    try {
        const res = await fetch(`${API_URL}/api/step`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ actions: {} })
        });
        
        if (res.ok) {
            const data = await res.json();
            state.labHistory.push(data.state);
            state.labTick += 1;
            renderLabSmallBoard();
            updateLabDecisionLog(data.state);
            
            if (data.status === 'game_over' || !data.game_continue) {
                if (state.labIntervalId) {
                    clearInterval(state.labIntervalId);
                    state.labIntervalId = null;
                }
                state.labPlaying = false;
                el.labPlay.textContent = 'Play';
                alert("Scenario reached resolution terminal state.");
            }
        }
    } catch (e) {
        console.error(e);
    }
}

function prevLabTick() {
    if (state.labTick > 0) {
        state.labTick -= 1;
        renderLabSmallBoard();
        updateLabDecisionLog(state.labHistory[state.labTick]);
    }
}

function toggleLabPlayback() {
    state.labPlaying = !state.labPlaying;
    if (state.labPlaying) {
        el.labPlay.textContent = 'Pause';
        state.labIntervalId = setInterval(() => {
            nextLabTick();
        }, 600);
    } else {
        el.labPlay.textContent = 'Play';
        if (state.labIntervalId) {
            clearInterval(state.labIntervalId);
            state.labIntervalId = null;
        }
    }
}

// ----------------------------------------------------
// MODULE 3: RESEARCH ANALYTICS DASHBOARD
// ----------------------------------------------------
function setupAnalyticsHandlers() {
    // Replay controls
    el.repPlay.addEventListener('click', toggleReplayPlayback);
    el.repPrev.addEventListener('click', prevReplayTick);
    el.repNext.addEventListener('click', nextReplayTick);
    el.repScrub.addEventListener('input', scrubReplayTick);
    
    // Exports
    el.exportCsvBtn.addEventListener('click', exportMatchCSV);
    el.exportJsonBtn.addEventListener('click', exportMatchJSON);
    el.exportPngBtn.addEventListener('click', exportChartsPNG);
    
    // Heatmap / Normal radio buttons
    document.querySelectorAll('input[name="overlay-type"]').forEach(radio => {
        radio.addEventListener('change', (e) => {
            state.replayOverlayMode = e.target.value;
            renderReplayBoard();
        });
    });

    // CSV vs SQLite Toggle
    if (el.btnAnalyticsCsv && el.btnAnalyticsDb) {
        el.btnAnalyticsCsv.addEventListener('click', () => {
            el.btnAnalyticsCsv.classList.add('active');
            el.btnAnalyticsDb.classList.remove('active');
            state.analyticsSource = 'csv';
            loadAnalyticsData();
        });
        el.btnAnalyticsDb.addEventListener('click', () => {
            el.btnAnalyticsDb.classList.add('active');
            el.btnAnalyticsCsv.classList.remove('active');
            state.analyticsSource = 'db';
            loadAnalyticsData();
        });
    }
}

async function loadAnalyticsData() {
    if (!state.isConnected) return;
    
    if (state.analyticsSource === 'csv') {
        await loadCSVAnalyticsData();
    } else {
        await loadDBAnalyticsData();
    }
}

async function loadDBAnalyticsData() {
    try {
        // Clear potential CSV static rendering from replay board
        el.replayBoard.innerHTML = '';
        
        // 1. Fetch overview numbers
        const resOver = await fetch(`${API_URL}/api/analytics/overview`);
        if (resOver.ok) {
            const data = await resOver.json();
            state.analyticsOverview = data;
            
            el.cardTotalMatches.textContent = data.total_matches;
            el.cardAvgLatency.textContent = `${data.avg_latency_ms.toFixed(1)} ms`;
            el.cardAvgScore.textContent = Math.round(data.avg_score);
            el.cardResources.textContent = `${data.avg_cpu_usage.toFixed(1)}% / ${data.avg_memory_usage.toFixed(1)}MB`;
        }
        
        // 2. Fetch compare stats
        const resComp = await fetch(`${API_URL}/api/analytics/compare`);
        if (resComp.ok) {
            const data = await resComp.json();
            state.analyticsCompare = data.compare;
            
            // Redraw charts
            drawPerformanceCharts(data.compare);
        }
        
        // 3. Fetch matches history list for Replay selector
        const resMatches = await fetch(`${API_URL}/api/matches`);
        if (resMatches.ok) {
            const data = await resMatches.json();
            state.matches = data.matches;
            renderMatchesList(data.matches);
            
            // Auto-load first match if exists
            if (data.matches.length > 0) {
                loadReplayMatch(data.matches[0].id);
            }
        }
    } catch (e) {
        console.error("Failed to load DB analytics", e);
    }
}

async function loadCSVAnalyticsData() {
    try {
        // 1. Fetch comparison and summary data from folder
        const resComp = await fetch(`${API_URL}/api/csv/comparison`);
        const resFowSum = await fetch(`${API_URL}/api/csv/fow_summary`);
        const resNormSum = await fetch(`${API_URL}/api/csv/normal_summary`);
        
        if (!resComp.ok || !resFowSum.ok || !resNormSum.ok) return;
        
        const compData = await resComp.json();
        const fowSum = await resFowSum.json();
        const normSum = await resNormSum.json();
        
        // 2. Populate overview cards
        const totalMatches = fowSum[0] ? fowSum[0].matches_played * 2 : 440;
        el.cardTotalMatches.textContent = totalMatches;
        
        let totalLat = 0;
        fowSum.forEach(d => totalLat += d.average_latency_ms);
        normSum.forEach(d => totalLat += d.average_latency_ms);
        const avgLat = totalLat / (fowSum.length + normSum.length);
        el.cardAvgLatency.textContent = `${avgLat.toFixed(1)} ms`;
        
        let totalElo = 0;
        fowSum.forEach(d => totalElo += d.final_elo);
        normSum.forEach(d => totalElo += d.final_elo);
        const avgElo = totalElo / (fowSum.length + normSum.length);
        el.cardAvgScore.textContent = Math.round(avgElo);
        
        el.cardResources.textContent = "CSV File Logs";
        
        // 3. Draw CSV Charts
        drawCSVCharts(compData, normSum, fowSum);
        
        // 4. Fetch tournament matches (displaying normal mode as default tournament list)
        const resMatches = await fetch(`${API_URL}/api/csv/normal_tournament`);
        if (resMatches.ok) {
            const matchesData = await resMatches.json();
            
            // Group rows by match_id to form unique matches
            const matchGroups = {};
            matchesData.forEach(row => {
                if (!matchGroups[row.match_id]) {
                    matchGroups[row.match_id] = {
                        id: row.match_id,
                        map_preset: "Tournament Mode",
                        steps: row.steps,
                        seed: row.seed,
                        winner_name: row.winner_id,
                        created_at: new Date().toISOString(),
                        agents: []
                    };
                }
                matchGroups[row.match_id].agents.push(row);
            });
            
            const matchesList = Object.values(matchGroups);
            state.csvMatches = matchesList;
            state.matches = matchesList; // fallback
            renderCSVMatchesList(matchesList);
            
            if (matchesList.length > 0) {
                loadCSVReplayMatch(matchesList[0].id);
            }
        }
    } catch (e) {
        console.error("Failed to load CSV analytics", e);
    }
}

function renderCSVMatchesList(matches) {
    const list = el.replayMatchesList;
    list.innerHTML = '';
    
    matches.forEach((match) => {
        const item = document.createElement('div');
        item.className = 'scenario-item';
        if (state.selectedReplayMatch === match.id) {
            item.classList.add('active');
        }
        
        item.innerHTML = `
            <div class="scenario-name">Tournament Match: ${match.id.toUpperCase()}</div>
            <div class="scenario-desc">Steps: ${match.steps} | Seed: ${match.seed}</div>
            <div class="scenario-desc" style="color:var(--text-muted); margin-top:2px;">Winner: ${match.winner_name}</div>
        `;
        
        item.addEventListener('click', () => {
            document.querySelectorAll('#replay-matches-list .scenario-item').forEach(i => i.classList.remove('active'));
            item.classList.add('active');
            loadCSVReplayMatch(match.id);
        });
        
        list.appendChild(item);
    });
}

function loadCSVReplayMatch(matchId) {
    state.selectedReplayMatch = matchId;
    const match = state.csvMatches.find(m => m.id === matchId);
    if (!match) return;
    
    el.repMatchDisplay.textContent = `Match ID: ${match.id} (Seed ${match.seed})`;
    el.repTickDisplay.textContent = `CSV Static Match`;
    el.repScrub.max = 0;
    el.repScrub.value = 0;
    
    el.replayBoard.innerHTML = `
        <div style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:20px; box-sizing:border-box; overflow-y:auto; background: rgba(6, 11, 19, 0.4); border-radius: 8px;">
            <h3 style="margin-bottom:16px; color:var(--primary); font-family:system-ui; font-size:1.1rem; letter-spacing:0.05em;">TOURNAMENT MATCH RESULTS</h3>
            <table style="width:100%; border-collapse:collapse; text-align:left; font-size:0.8rem; color:var(--text-primary);">
                <thead>
                    <tr style="border-bottom: 2px solid var(--border-color); color:var(--text-secondary);">
                        <th style="padding:10px 4px;">Agent ID</th>
                        <th style="padding:10px 4px;">Rank</th>
                        <th style="padding:10px 4px;">Survival Steps</th>
                        <th style="padding:10px 4px;">Kills</th>
                        <th style="padding:10px 4px;">Suicides</th>
                        <th style="padding:10px 4px;">Bricks</th>
                        <th style="padding:10px 4px;">Items</th>
                        <th style="padding:10px 4px;">Avg Latency</th>
                        <th style="padding:10px 4px;">Elo After</th>
                    </tr>
                </thead>
                <tbody>
                    ${match.agents.map(a => `
                        <tr style="border-bottom: 1px solid var(--border-color); ${a.agent_id === match.winner_name ? 'background-color:rgba(16,185,129,0.08); color:var(--accent-green);' : ''}">
                            <td style="padding:10px 4px; font-weight:700;">${a.agent_id}</td>
                            <td style="padding:10px 4px;">${a.rank}</td>
                            <td style="padding:10px 4px;">${a.survival_steps}</td>
                            <td style="padding:10px 4px;">${a.kills}</td>
                            <td style="padding:10px 4px;">${a.suicides}</td>
                            <td style="padding:10px 4px;">${a.bricks_destroyed}</td>
                            <td style="padding:10px 4px;">${a.items_collected}</td>
                            <td style="padding:10px 4px;">${a.avg_latency_ms.toFixed(2)}ms</td>
                            <td style="padding:10px 4px; font-weight:600;">${a.elo_after_match.toFixed(1)}</td>
                        </tr>
                    `).join('')}
                </tbody>
            </table>
            <div style="margin-top:24px; color:var(--text-muted); font-size:0.75rem; text-align:center; max-width:80%;">
                ⚠️ This is a historical tournament match record from the CSV folder. <br>
                Replay frame-by-frame scrubbing is only available in <strong>Live Play Benchmarks (SQLite)</strong> mode.
            </div>
        </div>
    `;
    
    el.repEvents.innerHTML = `
        <div class="log-line log-highlight-green">Match winner: ${match.winner_name}</div>
        <div class="log-line">Match Seed: ${match.seed}</div>
        <div class="log-line">Total steps: ${match.steps}</div>
        <div class="log-line" style="margin-top:10px; color:var(--text-muted);">This match was played in the original tournament environment.</div>
    `;
}

function drawCSVCharts(comparisonData, normalSummary, fowSummary) {
    const algos = comparisonData.map(d => d.agent_id);
    
    if (chartWinrateInstance) chartWinrateInstance.destroy();
    const ctxWin = document.getElementById('chart-winrate').getContext('2d');
    chartWinrateInstance = new Chart(ctxWin, {
        type: 'bar',
        data: {
            labels: algos,
            datasets: [
                {
                    label: 'Normal Mode (%)',
                    data: comparisonData.map(d => d.win_rate_normal * 100),
                    backgroundColor: 'rgba(6, 182, 212, 0.65)',
                    borderColor: '#06b6d4',
                    borderWidth: 2,
                    borderRadius: 4
                },
                {
                    label: 'Fog of War (%)',
                    data: comparisonData.map(d => d.win_rate_fow * 100),
                    backgroundColor: 'rgba(236, 72, 153, 0.65)',
                    borderColor: '#ec4899',
                    borderWidth: 2,
                    borderRadius: 4
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: { min: 0, max: 100, grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#94a3b8' } },
                x: { grid: { display: false }, ticks: { color: '#94a3b8' } }
            },
            plugins: {
                legend: { labels: { color: '#e2e8f0' } }
            }
        }
    });

    if (chartNodesInstance) chartNodesInstance.destroy();
    const ctxNodes = document.getElementById('chart-nodes').getContext('2d');
    chartNodesInstance = new Chart(ctxNodes, {
        type: 'bar',
        data: {
            labels: algos,
            datasets: [
                {
                    label: 'Normal ELO',
                    data: comparisonData.map(d => d.final_elo_normal),
                    backgroundColor: 'rgba(139, 92, 246, 0.65)',
                    borderColor: '#8b5cf6',
                    borderWidth: 2,
                    borderRadius: 4
                },
                {
                    label: 'Fog of War ELO',
                    data: comparisonData.map(d => d.final_elo_fow),
                    backgroundColor: 'rgba(245, 158, 11, 0.65)',
                    borderColor: '#f59e0b',
                    borderWidth: 2,
                    borderRadius: 4
                }
            ]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#94a3b8' } },
                y: { grid: { display: false }, ticks: { color: '#94a3b8' } }
            },
            plugins: {
                legend: { labels: { color: '#e2e8f0' } }
            }
        }
    });

    if (chartHorizonInstance) chartHorizonInstance.destroy();
    const ctxHor = document.getElementById('chart-horizon').getContext('2d');
    
    const normalPoints = normalSummary.map(d => ({
        x: d.final_elo,
        y: d.average_latency_ms,
        label: `${d.agent_id} (Normal)`
    }));
    const fowPoints = fowSummary.map(d => ({
        x: d.final_elo,
        y: d.average_latency_ms,
        label: `${d.agent_id} (FOW)`
    }));

    chartHorizonInstance = new Chart(ctxHor, {
        type: 'scatter',
        data: {
            datasets: [
                {
                    label: 'Normal Mode',
                    data: normalPoints,
                    backgroundColor: '#06b6d4',
                    pointRadius: 6
                },
                {
                    label: 'Fog of War',
                    data: fowPoints,
                    backgroundColor: '#ec4899',
                    pointRadius: 6
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: { title: { display: true, text: 'Elo Rating', color: '#94a3b8' }, grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#94a3b8' } },
                y: { title: { display: true, text: 'Latency (ms)', color: '#94a3b8' }, grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#94a3b8' } }
            },
            plugins: {
                tooltip: {
                    callbacks: {
                        label: function(ctx) {
                            return `${ctx.raw.label}: ELO=${ctx.raw.x.toFixed(1)}, Latency=${ctx.raw.y.toFixed(2)} ms`;
                        }
                    }
                },
                legend: { labels: { color: '#e2e8f0' } }
            }
        }
    });

    if (chartTacticalInstance) chartTacticalInstance.destroy();
    const ctxTac = document.getElementById('chart-tactical').getContext('2d');
    chartTacticalInstance = new Chart(ctxTac, {
        type: 'bar',
        data: {
            labels: algos,
            datasets: [
                {
                    label: 'Avg Bricks Destroyed',
                    data: normalSummary.map(d => d.bricks_destroyed),
                    backgroundColor: 'rgba(16, 185, 129, 0.65)',
                    borderColor: '#10b981',
                    borderWidth: 2,
                    borderRadius: 4
                },
                {
                    label: 'Avg Items Collected',
                    data: normalSummary.map(d => d.items_collected),
                    backgroundColor: 'rgba(245, 158, 11, 0.65)',
                    borderColor: '#f59e0b',
                    borderWidth: 2,
                    borderRadius: 4
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#94a3b8' } },
                x: { grid: { display: false }, ticks: { color: '#94a3b8' } }
            },
            plugins: {
                legend: { labels: { color: '#e2e8f0' } }
            }
        }
    });
}

function renderMatchesList(matches) {
    const list = el.replayMatchesList;
    list.innerHTML = '';
    
    matches.forEach((match, index) => {
        const item = document.createElement('div');
        item.className = 'scenario-item';
        if (state.selectedReplayMatch === match.id) {
            item.classList.add('active');
        }
        
        const date = new Date(match.created_at).toLocaleDateString();
        const time = new Date(match.created_at).toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
        
        item.innerHTML = `
            <div class="scenario-name">Preset: ${match.map_preset.toUpperCase()}</div>
            <div class="scenario-desc">Steps: ${match.steps} | Seed: ${match.seed}</div>
            <div class="scenario-desc" style="color:var(--text-muted); margin-top:2px;">Winner: ${match.winner_name} | ${date} ${time}</div>
        `;
        
        item.addEventListener('click', () => {
            document.querySelectorAll('#replay-matches-list .scenario-item').forEach(i => i.classList.remove('active'));
            item.classList.add('active');
            loadReplayMatch(match.id);
        });
        
        list.appendChild(item);
    });
}

async function loadReplayMatch(matchId) {
    if (state.replayIntervalId) {
        clearInterval(state.replayIntervalId);
        state.replayIntervalId = null;
    }
    state.replayPlaying = false;
    el.repPlay.textContent = 'Play';
    
    state.selectedReplayMatch = matchId;
    
    try {
        const res = await fetch(`${API_URL}/api/matches/${matchId}/replay`);
        if (res.ok) {
            const data = await res.json();
            state.replaySteps = data.replay_steps;
            state.replayTick = 0;
            
            // Configure scrub slider
            el.repScrub.max = state.replaySteps.length - 1;
            el.repScrub.value = 0;
            
            const matchInfo = state.matches.find(m => m.id === matchId);
            el.repMatchDisplay.textContent = matchInfo ? `${matchInfo.map_preset.toUpperCase()} (Seed ${matchInfo.seed})` : matchId.substring(0, 8);
            el.repTickDisplay.textContent = `0/${state.replaySteps.length - 1}`;
            
            renderReplayBoard();
            renderReplayEvents();
        }
    } catch (e) {
        console.error(e);
    }
}

function renderReplayBoard() {
    const curStep = state.replaySteps[state.replayTick];
    if (!curStep) return;
    
    el.repTickDisplay.textContent = `${state.replayTick}/${state.replaySteps.length - 1}`;
    el.repScrub.value = state.replayTick;
    
    if (state.replayOverlayMode === 'heatmap') {
        // Calculate position frequencies of ALL agents up to current tick
        const frequencies = {};
        const width = curStep.grid[0].length;
        const height = curStep.grid.length;
        
        let maxFreq = 1;
        for (let i = 0; i <= state.replayTick; i++) {
            const step = state.replaySteps[i];
            for (const aid in step.agents) {
                const agent = step.agents[aid];
                if (agent.is_alive) {
                    const key = `${agent.x},${agent.y}`;
                    frequencies[key] = (frequencies[key] || 0) + 1;
                    if (frequencies[key] > maxFreq) {
                        maxFreq = frequencies[key];
                    }
                }
            }
        }
        
        // Render board but overlay heatmap background colors
        const container = el.replayBoard;
        container.innerHTML = '';
        container.style.gridTemplateColumns = `repeat(${width}, 34px)`;
        container.style.gridTemplateRows = `repeat(${height}, 34px)`;
        
        for (let y = 0; y < height; y++) {
            for (let x = 0; x < width; x++) {
                const cell = document.createElement('div');
                cell.style.width = '34px';
                cell.style.height = '34px';
                
                const tile = curStep.grid[y][x];
                let cellClass = `board-cell ${(x + y) % 2 === 0 ? 'cell-ground-even' : 'cell-ground-odd'}`;
                if (tile === 1) cellClass += ' cell-wall';
                else if (tile === 2) cellClass += ' cell-brick';
                
                cell.className = cellClass;
                
                // If it's a walk path, overlay HSL heat color
                const key = `${x},${y}`;
                if (frequencies[key] && tile !== 1 && tile !== 2) {
                    const density = frequencies[key] / maxFreq;
                    cell.style.backgroundColor = `rgba(244, 63, 94, ${0.15 + density * 0.7})`;
                    cell.style.boxShadow = `inset 0 0 8px rgba(244, 63, 94, ${density})`;
                }
                
                container.appendChild(cell);
            }
        }
    } else {
        renderGameBoard(curStep, 'replay-board');
    }
}

function renderReplayEvents() {
    const events = [];
    const stepCount = state.replaySteps.length;
    
    // Scan steps to find events
    let activeBombs = new Set();
    
    state.replaySteps.forEach((step, idx) => {
        // Look for new bomb placements
        step.bombs.forEach(b => {
            const key = `${b.x},${b.y}`;
            if (!activeBombs.has(key)) {
                activeBombs.add(key);
                events.push(`[Tick ${idx}] Agent ${b.owner_id.toUpperCase()} placed a bomb at (${b.x}, ${b.y})`);
            }
        });
        
        // Look for dead agents
        for (const aid in step.agents) {
            const agent = step.agents[aid];
            const prevAgent = idx > 0 ? state.replaySteps[idx - 1].agents[aid] : null;
            if (prevAgent && prevAgent.is_alive && !agent.is_alive) {
                events.push(`[Tick ${idx}] 💀 Agent ${aid.toUpperCase()} was eliminated!`);
            }
        }
    });
    
    const eventsBox = el.repEvents;
    eventsBox.innerHTML = '';
    
    if (events.length === 0) {
        eventsBox.innerHTML = '<div>No major events detected during this run.</div>';
        return;
    }
    
    events.forEach(ev => {
        const item = document.createElement('div');
        item.style.marginBottom = '6px';
        item.textContent = ev;
        eventsBox.appendChild(item);
    });
}

function nextReplayTick() {
    if (state.replayTick + 1 < state.replaySteps.length) {
        state.replayTick += 1;
        renderReplayBoard();
    } else {
        pauseReplayPlayback();
    }
}

function prevReplayTick() {
    if (state.replayTick > 0) {
        state.replayTick -= 1;
        renderReplayBoard();
    }
}

function scrubReplayTick(e) {
    state.replayTick = parseInt(e.target.value);
    renderReplayBoard();
}

function toggleReplayPlayback() {
    state.replayPlaying = !state.replayPlaying;
    if (state.replayPlaying) {
        el.repPlay.textContent = 'Pause';
        if (state.replayTick >= state.replaySteps.length - 1) {
            state.replayTick = 0;
        }
        state.replayIntervalId = setInterval(nextReplayTick, 250);
    } else {
        pauseReplayPlayback();
    }
}

function pauseReplayPlayback() {
    state.replayPlaying = false;
    el.repPlay.textContent = 'Play';
    if (state.replayIntervalId) {
        clearInterval(state.replayIntervalId);
        state.replayIntervalId = null;
    }
}

// ----------------------------------------------------
// EXPORTING UTILITIES
// ----------------------------------------------------
function exportMatchCSV() {
    if (!state.selectedReplayMatch || state.replaySteps.length === 0) return;
    
    const matchInfo = state.matches.find(m => m.id === state.selectedReplayMatch);
    if (!matchInfo) return;
    
    let csv = 'Tick,Agent,X,Y,Lives,BombsLeft,Range,Action,Reasoning\n';
    
    state.replaySteps.forEach(step => {
        for (const aid in step.agents) {
            const agent = step.agents[aid];
            const trace = step.traces?.[aid] || {};
            const action = step.actions?.[aid] || 'WAIT';
            const reasoning = trace.reasoning ? trace.reasoning.join(' | ').replace(/"/g, '""') : '';
            
            csv += `${step.tick},${aid},${agent.x},${agent.y},${agent.lives},${agent.bombs_left},${agent.bomb_range},"${action}","${reasoning}"\n`;
        }
    });
    
    triggerDownload(csv, `match_${state.selectedReplayMatch}_telemetry.csv`, 'text/csv');
}

function exportMatchJSON() {
    if (state.replaySteps.length === 0) return;
    const jsonStr = JSON.stringify(state.replaySteps, null, 2);
    triggerDownload(jsonStr, `match_${state.selectedReplayMatch}_replay.json`, 'application/json');
}

function exportChartsPNG() {
    const charts = [
        { id: 'chart-winrate', name: 'winrates.png' },
        { id: 'chart-nodes', name: 'heuristic_efficiency.png' },
        { id: 'chart-horizon', name: 'latency_horizon.png' },
        { id: 'chart-tactical', name: 'tactical_success_rates.png' }
    ];
    
    charts.forEach(c => {
        const canvas = document.getElementById(c.id);
        if (canvas) {
            const url = canvas.toDataURL('image/png');
            const link = document.createElement('a');
            link.download = c.name;
            link.href = url;
            link.click();
        }
    });
}

function triggerDownload(content, filename, mimeType) {
    const blob = new Blob([content], { type: mimeType });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    link.click();
    URL.revokeObjectURL(url);
}

// ----------------------------------------------------
// CHART.JS RENDER LOGIC
// ----------------------------------------------------
function drawPerformanceCharts(compareData) {
    const algos = compareData.map(d => d.algorithm.toUpperCase());
    const winRates = compareData.map(d => d.win_rate);
    const nodes = compareData.map(d => d.avg_nodes_expanded);
    const latencies = compareData.map(d => d.avg_latency_ms);
    const horizons = compareData.map(d => d.avg_planning_horizon);
    
    const escapeRates = compareData.map(d => d.avg_escape_success_rate);
    const bombAcc = compareData.map(d => d.avg_bomb_accuracy);
    
    // 1. Win Rate Bar Chart
    if (chartWinrateInstance) chartWinrateInstance.destroy();
    const ctxWin = document.getElementById('chart-winrate').getContext('2d');
    chartWinrateInstance = new Chart(ctxWin, {
        type: 'bar',
        data: {
            labels: algos,
            datasets: [{
                label: 'Win Rate (%)',
                data: winRates,
                backgroundColor: 'rgba(6, 182, 212, 0.65)',
                borderColor: '#06b6d4',
                borderWidth: 2,
                borderRadius: 6
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: { min: 0, max: 100, grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#94a3b8' } },
                x: { grid: { display: false }, ticks: { color: '#94a3b8' } }
            },
            plugins: {
                legend: { display: false }
            }
        }
    });

    // 2. Nodes Expanded Horizontal Bar
    if (chartNodesInstance) chartNodesInstance.destroy();
    const ctxNodes = document.getElementById('chart-nodes').getContext('2d');
    chartNodesInstance = new Chart(ctxNodes, {
        type: 'bar',
        data: {
            labels: algos,
            datasets: [{
                label: 'Avg Nodes Expanded',
                data: nodes,
                backgroundColor: 'rgba(139, 92, 246, 0.65)',
                borderColor: '#8b5cf6',
                borderWidth: 2,
                borderRadius: 6
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#94a3b8' } },
                y: { grid: { display: false }, ticks: { color: '#94a3b8' } }
            },
            plugins: {
                legend: { display: false }
            }
        }
    });

    // 3. Planning Horizon Scatter / Line Chart
    if (chartHorizonInstance) chartHorizonInstance.destroy();
    const ctxHor = document.getElementById('chart-horizon').getContext('2d');
    
    // Format scatter points
    const scatterPoints = compareData.map(d => ({
        x: d.avg_planning_horizon,
        y: d.avg_latency_ms,
        label: d.algorithm.toUpperCase()
    }));
    
    chartHorizonInstance = new Chart(ctxHor, {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'AI Algorithms',
                data: scatterPoints,
                backgroundColor: '#ec4899',
                pointRadius: 8,
                pointHoverRadius: 10
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: { 
                    title: { display: true, text: 'Search Horizon (Steps)', color: '#94a3b8' },
                    grid: { color: 'rgba(255,255,255,0.05)' }, 
                    ticks: { color: '#94a3b8' } 
                },
                y: { 
                    title: { display: true, text: 'Latency (ms)', color: '#94a3b8' },
                    grid: { color: 'rgba(255,255,255,0.05)' }, 
                    ticks: { color: '#94a3b8' } 
                }
            },
            plugins: {
                tooltip: {
                    callbacks: {
                        label: function(ctx) {
                            return `${ctx.raw.label}: Horizon=${ctx.raw.x} steps, Latency=${ctx.raw.y.toFixed(1)} ms`;
                        }
                    }
                }
            }
        }
    });

    // 4. Tactical Success rates comparison Grouped Bar
    if (chartTacticalInstance) chartTacticalInstance.destroy();
    const ctxTac = document.getElementById('chart-tactical').getContext('2d');
    chartTacticalInstance = new Chart(ctxTac, {
        type: 'bar',
        data: {
            labels: algos,
            datasets: [
                {
                    label: 'Escape Success (%)',
                    data: escapeRates,
                    backgroundColor: 'rgba(16, 185, 129, 0.65)',
                    borderColor: '#10b981',
                    borderWidth: 2,
                    borderRadius: 4
                },
                {
                    label: 'Bomb Accuracy (%)',
                    data: bombAcc,
                    backgroundColor: 'rgba(245, 158, 11, 0.65)',
                    borderColor: '#f59e0b',
                    borderWidth: 2,
                    borderRadius: 4
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: { min: 0, max: 100, grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#94a3b8' } },
                x: { grid: { display: false }, ticks: { color: '#94a3b8' } }
            },
            plugins: {
                legend: { labels: { color: '#94a3b8' } }
            }
        }
    });
}
