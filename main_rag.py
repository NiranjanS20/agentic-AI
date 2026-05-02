from rich.console import Console
from rag.document_loader import load_pdf
from rag.vector_store import vectorStore
from agent.rag_agent import RAGAgent
from utils.logger import log_message
from rag.embeddings import embed_chunks
from rag.text_chunker import chunk_text

console = Console()

def setup_vector_store(pdf_path):
    console.print(f"[yellow]Loading PDF from {pdf_path}...[/yellow]")
    text = load_pdf(pdf_path)

    console.print("[yellow]Chunking text...[/yellow]")
    chunks = chunk_text(text)

    console.print("[yellow]Embedding chunks...[/yellow]")
    embedded_chunks = embed_chunks(chunks)

    console.print("[yellow]Building vector datastore...[/yellow]")
    vector_store = vectorStore(len(embedded_chunks[0]))
    vector_store.add_embeddings(embedded_chunks, chunks)

    return vector_store

def main():
    console.print("[bold green]Agentic RAG system started[/bold green]")

    pdf_path = "data/documents/resume_3.0.pdf"
    vector_store = setup_vector_store(pdf_path)
    agent = RAGAgent(vector_store)
    provider = None

    console.print("Type 'groq' or 'gemini' to switch provider, or 'exit' to quit")

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

        console.print(f"[cyan]RAG Agent:[/cyan] {response}")

if __name__ == "__main__":
    main()
