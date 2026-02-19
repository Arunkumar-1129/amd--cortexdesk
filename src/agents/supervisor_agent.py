from .base_agent import BaseAgent, AgentRegistry
from typing import Dict, Any
import queue

class SupervisorAgent:
    def __init__(self, registry: AgentRegistry, event_bus):
        self.registry = registry
        self.event_bus = event_bus
        self.task_queue = queue.Queue()
        self.running = False
    
    def route_task(self, task: Dict[str, Any]):
        capability = task.get("capability")
        agent = self.registry.find_agent_for_capability(capability)
        
        if agent:
            agent.enqueue_task(task)
        else:
            print(f"No agent found for capability: {capability}")
    
    def start(self):
        self.running = True
        for agent in self.registry.get_all_agents():
            agent.start()
    
    def stop(self):
        self.running = False
        for agent in self.registry.get_all_agents():
            agent.stop()
    
    def get_agent_status(self) -> Dict[str, str]:
        return {
            agent_id: info["status"]
            for agent_id, info in self.registry.agents.items()
        }
