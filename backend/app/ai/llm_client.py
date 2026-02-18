"""
Local LLM client (Ollama).
"""
from typing import Optional
from app.core.config import settings
import yaml
from pathlib import Path


def load_model_config() -> dict:
    """Load model configuration from models.yaml."""
    config_path = Path(__file__).parent.parent.parent.parent / "config" / "models.yaml"
    if config_path.exists():
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
            return config.get('llm', {})
    return {}


async def generate(prompt: str, system_prompt: Optional[str] = None) -> str:
    """
    Generate text using local LLM (Ollama).
    
    Args:
        prompt: User prompt
        system_prompt: Optional system prompt
    
    Returns:
        Generated text
    """
    # TODO: Implement Ollama client
    # Example: import ollama; response = ollama.chat(model="llama3:8b", messages=[...])
    raise NotImplementedError("LLM client not yet implemented")


async def generate_streaming(prompt: str, system_prompt: Optional[str] = None):
    """
    Generate text with streaming response.
    """
    # TODO: Implement streaming
    raise NotImplementedError("Streaming LLM not yet implemented")

