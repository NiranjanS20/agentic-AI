from groq import Groq
from config.settings import GROQ_API_KEY

client = Groq(api_key = GROQ_API_KEY)

def groq_generate(prompt: str) -> str:
    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content