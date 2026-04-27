from rich.console import Console
from agent.core_agent import MultiLLMagent
from utils.logger import log_message

console = Console()
agent = MultiLLMagent()

def main():
    console.print("[bold green]Multi-LLM Agent Started (Groq + Gemini)[/bold green]")
    console.print("Type 'exit' to quit")
    console.print("Type 'use groq' or 'use gemini' to switch provider")
    console.print("Type 'calc: 25*8' for calculator")

    provider = None

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            break

        if user_input.lower().startswith("use "):
            provider = user_input.split("use ")[1].strip()
            console.print(f"[yellow]Switched to {provider}[/yellow]")
            continue

        response = agent.chat(user_input, provider)

        log_message("user", user_input)
        log_message("assistant", response)

        console.print(f"[cyan]Agent:[/cyan] {response}")

if __name__ == "__main__":
    main()