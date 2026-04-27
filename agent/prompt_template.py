def build_prompt (user_input: str, memory_context: str) -> str:
    return f"""
You are an intelligent assistant. Use the following conversation history and user input to generate a helpful response.

Conversation History:
{memory_context}

User Input:
{user_input}

Instructions:
- Provide a clear and concise answer to the user's query.
- Be accurate
- Be concise but helpful
- Use reasoning
- If math, solve step-by-step
"""