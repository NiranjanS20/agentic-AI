class ConversationBuffer:
    def __init__(self):
        self.history = []
    
    def add(self, role: str, content: str):
        self.history.append({"role": role, "content": content})

    def get_context(self) -> str:
        formatted = []
        for msg in self.history:
            formatted.append(f"{msg['role'].upper()}: {msg['content']}")
        return "\n".join(formatted)
