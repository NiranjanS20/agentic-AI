from llm.groq_client import groq_generate
from llm.gemini_client import gemini_generate
from config.settings import DEFAULT_PROVIDER

def route_llm(prompt: str, provider: str = None) -> str:
    provider = provider or DEFAULT_PROVIDER
    if provider == "groq":
        return groq_generate(prompt)
    elif provider == "gemini":
        return gemini_generate(prompt)
    else:
        raise ValueError(f"Unsupported Provider! Use 'groq' or 'gemini'. Received: {provider}")
    
    