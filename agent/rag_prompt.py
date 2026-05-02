def build_rag_prompt(user_query, retrieved_context, memory_context):
    prompt = f"""
    You are an intelligent RAG assistant.

    Conversation History:
    {memory_context}

    Retrieved Document Context:
    {retrieved_context}

    User Question:
    {user_query}

    Instructions:
    - Answer primarily based on the retrieved context
    - If answer is missing, clearly say information not found in the documents
    - Be accurate
    - Be concise and structured
    - Use reasoning where useful and appropriate
    """
    return prompt.strip()
