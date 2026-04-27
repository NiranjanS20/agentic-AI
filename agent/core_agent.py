from memory.conversation_buffer import ConversationBuffer
from tools.tool_registry import detect_tool
from agent.prompt_template import build_prompt
from llm.router import route_llm 

class MultiLLMagent:
    def __init__(self):
        self.memory = ConversationBuffer()
    
    def chat(self, user_input: str, provider: str = None) -> str:
        tool_result = detect_tool(user_input)

        if tool_result:
            self.memory.add("user", user_input)
            self.memory.add("assistant", tool_result)
            return tool_result
        
        memory_context = self.memory.get_context()
        prompt = build_prompt(user_input, memory_context)

        response = route_llm(prompt, provider)

        self.memory.add("user", user_input)
        self.memory.add("assistant", response)
        return response