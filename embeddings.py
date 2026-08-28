import ollama

def get_embedding(text: str , model = "nomic-embed-text")-> list[float]:
    """Get an embedding vector for a piece of text using Ollama."""
    response = ollama.embeddings(model=model, prompt=text)
    return response["embedding"]
