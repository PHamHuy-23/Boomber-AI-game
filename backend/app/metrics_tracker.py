import time
import uuid
from typing import Dict, List, Any, Optional

class MetricsTracker:
    def __init__(self, agent_ids: List[str]):
        self.match_id = str(uuid.uuid4())
        self.agent_ids = agent_ids
        
        # Telemetry storage
        self.kills: Dict[str, int] = {aid: 0 for aid in agent_ids}
        self.suicides: Dict[str, int] = {aid: 0 for aid in agent_ids}
        self.bricks_destroyed: Dict[str, int] = {aid: 0 for aid in agent_ids}
        self.items_collected: Dict[str, int] = {aid: 0 for aid in agent_ids}
        self.survival_steps: Dict[str, int] = {aid: 0 for aid in agent_ids}
        self.latencies: Dict[str, List[float]] = {aid: [] for aid in agent_ids}

    def record_step_latency(self, agent_id: str, latency_ms: float):
        if agent_id in self.latencies:
            self.latencies[agent_id].append(latency_ms)

    def record_item_pickup(self, agent_id: str):
        if agent_id in self.items_collected:
            self.items_collected[agent_id] += 1

    def record_brick_destroyed(self, agent_id: str):
        if agent_id in self.bricks_destroyed:
            self.bricks_destroyed[agent_id] += 1

    def record_death(self, agent_id: str, killer_id: Optional[str], step: int):
        if agent_id in self.survival_steps:
            self.survival_steps[agent_id] = step
            if killer_id == agent_id:
                self.suicides[agent_id] += 1
            elif killer_id in self.kills:
                self.kills[killer_id] += 1

    def get_final_stats(self, total_steps: int, alive_agents: List[str]) -> List[Dict[str, Any]]:
        """
        Compiles the aggregated statistics for each agent at the end of a match.
        """
        # Determine rankings
        # Rank is based on whether they survived, then their remaining lives (if equal) or other criteria.
        # To keep it simple: any agent alive at the end is Rank 1.
        # Agents who died are ranked by survival_steps descending.
        sorted_agents = []
        for aid in self.agent_ids:
            is_alive = aid in alive_agents
            steps = total_steps if is_alive else self.survival_steps[aid]
            sorted_agents.append((aid, is_alive, steps))
            
        # Sort key: is_alive descending (True first), then survival_steps descending
        sorted_agents.sort(key=lambda x: (-1 if x[1] else 0, -x[2]))
        
        rankings = {}
        for rank_idx, (aid, _, _) in enumerate(sorted_agents):
            rankings[aid] = rank_idx + 1

        stats_list = []
        for aid in self.agent_ids:
            # If survived, survival steps is the total steps
            steps = total_steps if aid in alive_agents else self.survival_steps[aid]
            
            # Compute average decision latency (ms)
            lat_list = self.latencies.get(aid, [])
            avg_latency = sum(lat_list) / len(lat_list) if lat_list else 0.0
            
            stats_list.append({
                "agent_id": aid,
                "rank": rankings[aid],
                "survival_steps": steps,
                "kills": self.kills.get(aid, 0),
                "suicides": self.suicides.get(aid, 0),
                "bricks_destroyed": self.bricks_destroyed.get(aid, 0),
                "items_collected": self.items_collected.get(aid, 0),
                "avg_latency_ms": round(avg_latency, 2)
            })
            
        return stats_list
