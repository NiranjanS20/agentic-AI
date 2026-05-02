from memory.conversation_buffer import ConversationBuffer
from llm.router import route_llm
from rag.retriever import retrieve_context
from agent.rag_prompt import build_rag_prompt

class RAGAgent:
    def __init__(self, vector_store):
        self.memory = ConversationBuffer()
        self.vector_store = vector_store

    def chat(self, user_input, provider=None):
        memory_context = self.memory.get_context()
        retrieved_context = retrieve_context(self.vector_store, user_input)

        prompt = build_rag_prompt(
            user_input,
            retrieved_context,
            memory_context
        )

        response = route_llm(prompt, provider=provider)

        self.memory.add("user", user_input)
        self.memory.add("assistant", response)

        return response
