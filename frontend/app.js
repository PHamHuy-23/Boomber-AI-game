const API_URL = 'http://127.0.0.1:8000';
let gameState = null;
let oldGameState = null;
let autoplayInterval = null;

// Tile mapping for Bomb It style elements
const TILE_CLASSES = {
    0: 'tile-empty',
    1: 'tile-wall',
    2: 'tile-brick',
    3: 'tile-bomb',
    4: 'tile-explosion',
    5: 'tile-item-radius',
    6: 'tile-item-capacity'
};

const AGENT_COLORS = {
    'player_1': '#00f0ff', // Neon Cyan
    'player_2': '#ff007f', // Neon Pink
    'player_3': '#39ff14', // Neon Green
    'player_4': '#fff000'  // Neon Yellow
};

// Bomb It 7 Avatar names
const AGENT_NAMES = {
    'player_1': 'P1 (Bạn) 👾',
    'player_2': 'Bot 2 🤖',
    'player_3': 'Bot 3 👽',
    'player_4': 'Bot 4 🦊'
};

const AGENT_EMOJIS = {
    'player_1': '👾',
    'player_2': '🤖',
    'player_3': '👽',
    'player_4': '🦊'
};

// Actions mapping
const ACTION_UP = 3;
const ACTION_DOWN = 4;
const ACTION_LEFT = 1;
const ACTION_RIGHT = 2;
const ACTION_BOMB = 5;
const ACTION_STOP = 0;

// DOM Elements
const boardEl = document.getElementById('board');
const btnInit = document.getElementById('btn-init');
const btnStep = document.getElementById('btn-step');
const chkAutoplay = document.getElementById('chk-autoplay');
const chkSound = document.getElementById('chk-sound');
const stepCountEl = document.getElementById('step-count');
const agentStatusListEl = document.getElementById('agent-status-list');
const gameStatusEl = document.getElementById('game-status');
const dbTotalMatchesEl = document.getElementById('db-total-matches');
const dbAvgStepsEl = document.getElementById('db-avg-steps');
const dbLeaderboardBodyEl = document.getElementById('db-leaderboard-body');
const btnRefreshDb = document.getElementById('btn-refresh-db');

// --- RETRO SOUND SYNTHESIZER (WEB AUDIO API) ---
class RetroAudioSynth {
    constructor() {
        this.ctx = null;
    }
    init() {
        if (!this.ctx) {
            this.ctx = new (window.AudioContext || window.webkitAudioContext)();
        }
        if (this.ctx.state === 'suspended') {
            this.ctx.resume();
        }
    }
    play(type) {
        if (!chkSound || !chkSound.checked) return;
        try {
            this.init();
            if (!this.ctx) return;
            const now = this.ctx.currentTime;
            
            if (type === 'place') {
                // Quick cute retro bubble pop
                let osc = this.ctx.createOscillator();
                let gain = this.ctx.createGain();
                osc.connect(gain); gain.connect(this.ctx.destination);
                osc.type = 'sine';
                osc.frequency.setValueAtTime(150, now);
                osc.frequency.exponentialRampToValueAtTime(30, now + 0.12);
                gain.gain.setValueAtTime(0.2, now);
                gain.gain.linearRampToValueAtTime(0, now + 0.12);
                osc.start(); osc.stop(now + 0.12);
            } 
            else if (type === 'explosion') {
                // Retro white noise explosion
                let bufferSize = this.ctx.sampleRate * 0.35;
                let buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
                let data = buffer.getChannelData(0);
                for (let i = 0; i < bufferSize; i++) {
                    data[i] = Math.random() * 2 - 1;
                }
                let noise = this.ctx.createBufferSource();
                noise.buffer = buffer;
                let filter = this.ctx.createBiquadFilter();
                filter.type = 'lowpass';
                filter.frequency.setValueAtTime(380, now);
                filter.frequency.exponentialRampToValueAtTime(10, now + 0.35);
                let gain = this.ctx.createGain();
                gain.gain.setValueAtTime(0.4, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.35);
                noise.connect(filter); filter.connect(gain); gain.connect(this.ctx.destination);
                noise.start(); noise.stop(now + 0.35);
            } 
            else if (type === 'pickup') {
                // Fast arcade chip-tune scale
                [523.25, 659.25, 783.99, 1046.5].forEach((f, i) => {
                    let osc = this.ctx.createOscillator();
                    let gain = this.ctx.createGain();
                    osc.connect(gain); gain.connect(this.ctx.destination);
                    osc.type = 'triangle';
                    osc.frequency.setValueAtTime(f, now + i * 0.05);
                    gain.gain.setValueAtTime(0.08, now + i * 0.05);
                    gain.gain.linearRampToValueAtTime(0, now + i * 0.05 + 0.08);
                    osc.start(now + i * 0.05); osc.stop(now + i * 0.05 + 0.08);
                });
            } 
            else if (type === 'death') {
                // Descending retro defeat sound
                let notes = [392, 349.23, 311.13, 261.63];
                notes.forEach((f, i) => {
                    let osc = this.ctx.createOscillator();
                    let gain = this.ctx.createGain();
                    osc.connect(gain); gain.connect(this.ctx.destination);
                    osc.type = 'sawtooth';
                    osc.frequency.setValueAtTime(f, now + i * 0.12);
                    gain.gain.setValueAtTime(0.12, now + i * 0.12);
                    gain.gain.exponentialRampToValueAtTime(0.01, now + i * 0.12 + 0.3);
                    osc.start(now + i * 0.12); osc.stop(now + i * 0.12 + 0.3);
                });
            }
        } catch (e) {
            console.warn("Synth play error:", e);
        }
    }
}
const synth = new RetroAudioSynth();

function playSound(type) {
    synth.play(type);
}

// Check state changes to play sounds
function triggerStateSounds(oldState, newState) {
    if (!oldState || !newState) return;
    
    // 1. Bomb placed
    const oldBombsCount = oldState.bombs ? oldState.bombs.length : 0;
    const newBombsCount = newState.bombs ? newState.bombs.length : 0;
    if (newBombsCount > oldBombsCount) {
        playSound('place');
    }
    
    // 2. Bomb detonated
    const detonatedCount = newState.explosion_origins ? newState.explosion_origins.length : 0;
    if (detonatedCount > 0) {
        playSound('explosion');
    }
    
    // 3. Item pickup & Death
    let itemPickedUp = false;
    let playerDied = false;
    
    Object.keys(newState.agents).forEach(id => {
        const oldAgent = oldState.agents[id];
        const newAgent = newState.agents[id];
        if (oldAgent && newAgent) {
            if (newAgent.max_bombs > oldAgent.max_bombs || newAgent.bomb_range > oldAgent.bomb_range) {
                itemPickedUp = true;
            }
            if (oldAgent.is_alive && !newAgent.is_alive) {
                playerDied = true;
            }
        }
    });
    
    if (itemPickedUp) {
        playSound('pickup');
    }
    if (playerDied) {
        playSound('death');
    }
}

// Floating Death Ghost 👻 Animation Spawner
function spawnDeathGhost(x, y) {
    if (!gameState) return;
    const index = y * gameState.width + x;
    const cellEl = boardEl.children[index];
    if (cellEl) {
        const ghost = document.createElement('div');
        ghost.className = 'ghost-dead';
        ghost.innerText = '👻';
        cellEl.appendChild(ghost);
        setTimeout(() => {
            ghost.remove();
        }, 1400); // Clean up element after animation finishes
    }
}

// Initialize Game
async function initGame() {
    try {
        const response = await fetch(`${API_URL}/api/init`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });
        if (!response.ok) throw new Error('API initialization failed');
        const data = await response.json();
        oldGameState = null;
        gameState = data.state;
        updateUI(data);
        loadDbStats();
    } catch (err) {
        console.error(err);
        showErrorAlert();
    }
}

// Tick Simulation Step
async function tickStep(player1Action = ACTION_STOP) {
    if (!gameState) return;

    try {
        const actions = { "player_1": player1Action };
        
        const response = await fetch(`${API_URL}/api/step`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ actions })
        });
        
        if (!response.ok) throw new Error('API step failed');
        const data = await response.json();
        
        oldGameState = gameState;
        gameState = data.state;
        
        // Spawn death ghosts by comparing alive states
        if (oldGameState && oldGameState.agents) {
            Object.keys(gameState.agents).forEach(id => {
                const oldAgent = oldGameState.agents[id];
                const newAgent = gameState.agents[id];
                if (oldAgent && oldAgent.is_alive && !newAgent.is_alive) {
                    spawnDeathGhost(oldAgent.x, oldAgent.y);
                }
            });
        }

        triggerStateSounds(oldGameState, gameState);
        updateUI(data);
        
        if (data.status === 'game_over') {
            stopAutoplay();
            loadDbStats();
        }
    } catch (err) {
        console.error(err);
        showErrorAlert();
    }
}

// Render Board & Status
function updateUI(data) {
    const state = data.state;
    
    // Clear board
    boardEl.innerHTML = '';
    
    // Render cells
    const width = state.width;
    const height = state.height;
    
    // Resize grid columns dynamic setup
    boardEl.style.gridTemplateColumns = `repeat(${width}, 40px)`;
    boardEl.style.gridTemplateRows = `repeat(${height}, 40px)`;

    for (let y = 0; y < height; y++) {
        for (let x = 0; x < width; x++) {
            const tileVal = state.grid[y][x];
            
            const cellEl = document.createElement('div');
            let tileClass = TILE_CLASSES[tileVal] || 'tile-empty';
            
            // Empty grid styling (checkerboard pattern)
            if (tileVal === 0) {
                const isEven = (x + y) % 2 === 0;
                tileClass = isEven ? 'tile-empty-even' : 'tile-empty-odd';
            }
            
            // Explosion patterns mapping
            if (tileVal === 4) {
                const isOrigin = state.explosion_origins && state.explosion_origins.some(coord => coord[0] === x && coord[1] === y);
                if (isOrigin) {
                    tileClass = 'tile-explosion-center';
                } else {
                    const isUpExplosion = (y > 0 && state.grid[y-1][x] === 4);
                    const isDownExplosion = (y < height - 1 && state.grid[y+1][x] === 4);
                    if (isUpExplosion || isDownExplosion) {
                        tileClass = 'tile-explosion-vertical';
                    } else {
                        tileClass = 'tile-explosion-horizontal';
                    }
                }
            }
            cellEl.className = `tile ${tileClass}`;
            
            // Add agents layer
            const agentsLayer = document.createElement('div');
            agentsLayer.className = 'agents-layer';
            
            // Look for agents on this tile
            Object.values(state.agents).forEach(agent => {
                if (agent.x === x && agent.y === y) {
                    const agentEl = document.createElement('div');
                    const dir = agent.direction || 'down';
                    agentEl.className = `agent agent-${agent.id} dir-${dir}`;
                    
                    if (!agent.is_alive) {
                        agentEl.classList.add('agent-dead');
                        agentEl.style.display = 'none'; // Replaced by ghost
                    }
                    agentsLayer.appendChild(agentEl);
                }
            });
            
            cellEl.appendChild(agentsLayer);
            boardEl.appendChild(cellEl);
        }
    }
    
    // Update step counter
    stepCountEl.innerText = `Step: ${state.step_count}`;
    
    // Update Game Over status message
    if (data.status === 'game_over') {
        gameStatusEl.innerText = 'GAME OVER';
        gameStatusEl.className = 'game-status-msg status-game_over';
    } else {
        gameStatusEl.innerText = 'RUNNING';
        gameStatusEl.className = 'game-status-msg status-running';
    }
    
    // Render Agent statuses
    agentStatusListEl.innerHTML = '';
    Object.values(state.agents).forEach(agent => {
        const row = document.createElement('div');
        row.className = `agent-status-row ${!agent.is_alive ? 'agent-dead-row' : ''}`;
        
        const badge = document.createElement('div');
        badge.className = 'agent-badge';
        
        const dot = document.createElement('div');
        dot.className = 'badge-dot';
        dot.style.backgroundColor = AGENT_COLORS[agent.id] || '#ffffff';
        
        const nameText = document.createTextNode(AGENT_NAMES[agent.id] || agent.id);
        badge.appendChild(dot);
        badge.appendChild(nameText);
        
        const stats = document.createElement('div');
        stats.className = 'agent-stats';
        if (agent.is_alive) {
            stats.innerHTML = `❤️ ${agent.lives} | 💣 ${agent.bombs_left}/${agent.max_bombs} | 🔥 ${agent.bomb_range}`;
        } else {
            stats.innerHTML = '💀 GONE';
        }
        
        row.appendChild(badge);
        row.appendChild(stats);
        agentStatusListEl.appendChild(row);
    });
}

// Autoplay Logic
function startAutoplay() {
    if (autoplayInterval) return;
    chkAutoplay.checked = true;
    autoplayInterval = setInterval(() => {
        tickStep(ACTION_STOP);
    }, 300);
}

function stopAutoplay() {
    if (autoplayInterval) {
        clearInterval(autoplayInterval);
        autoplayInterval = null;
    }
    chkAutoplay.checked = false;
}

// Show alert if backend server is offline
function showErrorAlert() {
    stopAutoplay();
    alert(`Không thể kết nối với máy chủ FastAPI tại ${API_URL}.\nVui lòng chạy lệnh sau để bật máy chủ:\nuvicorn app.main:app --reload`);
}

// Event Listeners
btnInit.addEventListener('click', initGame);
btnStep.addEventListener('click', () => tickStep(ACTION_STOP));

chkAutoplay.addEventListener('change', (e) => {
    if (e.target.checked) {
        startAutoplay();
    } else {
        stopAutoplay();
    }
});

// Keyboard Listeners
window.addEventListener('keydown', (e) => {
    if (!gameState) return;
    
    let action = null;
    switch (e.key) {
        case 'ArrowUp':
        case 'w':
        case 'W':
            action = ACTION_UP;
            break;
        case 'ArrowDown':
        case 's':
        case 'S':
            action = ACTION_DOWN;
            break;
        case 'ArrowLeft':
        case 'a':
        case 'A':
            action = ACTION_LEFT;
            break;
        case 'ArrowRight':
        case 'd':
        case 'D':
            action = ACTION_RIGHT;
            break;
        case ' ':
        case 'b':
        case 'B':
            action = ACTION_BOMB;
            break;
        case 'Enter':
            action = ACTION_STOP;
            break;
        default:
            return;
    }
    
    e.preventDefault();
    tickStep(action);
});

// Fetch stats from SQLite Database and render Leaderboard (Arcade Cabinet Screen)
async function loadDbStats() {
    try {
        const response = await fetch(`${API_URL}/api/benchmark/db-stats`);
        if (!response.ok) throw new Error('Failed to fetch DB stats');
        const data = await response.json();
        
        dbTotalMatchesEl.innerText = data.total_matches;
        dbAvgStepsEl.innerText = data.avg_steps;
        
        dbLeaderboardBodyEl.innerHTML = '';
        if (data.leaderboard.length === 0) {
            dbLeaderboardBodyEl.innerHTML = '<tr><td colspan="5" style="padding: 12px 0; text-align: center; color: #64748b;">No high scores saved</td></tr>';
            return;
        }
        
        data.leaderboard.forEach((agent, index) => {
            const tr = document.createElement('tr');
            tr.style.borderBottom = '1px dashed rgba(255, 255, 255, 0.06)';
            
            // Name
            const tdName = document.createElement('td');
            tdName.style.padding = '8px 0';
            tdName.style.fontWeight = 'bold';
            tdName.style.color = AGENT_COLORS[agent.agent_id] || '#ffffff';
            // Show rank prefix
            const rank = index + 1;
            tdName.innerText = `${rank}. ${agent.agent_id === 'player_1' ? 'P1' : agent.agent_id.replace('player_', 'P')}`;
            
            // Wins
            const tdWins = document.createElement('td');
            tdWins.style.padding = '8px 0';
            tdWins.style.textAlign = 'right';
            tdWins.style.color = 'var(--border-yellow)';
            tdWins.innerText = `${agent.wins} (${Math.round(agent.win_rate)}%)`;
            
            // Kills
            const tdKills = document.createElement('td');
            tdKills.style.padding = '8px 0';
            tdKills.style.textAlign = 'right';
            tdKills.style.color = 'var(--border-green)';
            tdKills.innerText = agent.total_kills;
            
            // Suicides
            const tdSuicides = document.createElement('td');
            tdSuicides.style.padding = '8px 0';
            tdSuicides.style.textAlign = 'right';
            tdSuicides.style.color = agent.total_suicides > 0 ? '#ff007f' : '#94a3b8';
            tdSuicides.innerText = agent.total_suicides;
            
            // Latency
            const tdLat = document.createElement('td');
            tdLat.style.padding = '8px 0';
            tdLat.style.textAlign = 'right';
            tdLat.style.color = 'var(--border-cyan)';
            tdLat.innerText = `${Math.round(agent.avg_latency_ms)}ms`;
            
            tr.appendChild(tdName);
            tr.appendChild(tdWins);
            tr.appendChild(tdKills);
            tr.appendChild(tdSuicides);
            tr.appendChild(tdLat);
            dbLeaderboardBodyEl.appendChild(tr);
        });
    } catch (err) {
        console.error('Error loading DB stats:', err);
    }
}

btnRefreshDb.addEventListener('click', loadDbStats);

// Load Game and DB stats on start
initGame();
loadDbStats();
