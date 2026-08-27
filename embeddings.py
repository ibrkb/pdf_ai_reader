import ollama
import numpy as np 

def get_embedding(text: str , model = "nomic-embed-text")-> list[float]:
    """Get an embedding vector for a piece of text using Ollama."""
    reponse = ollama.embeddings(model=model, prompt=text)
    return reponse["embedding"]

def cosine_similarity(vec1: list[float], vec2: list[float])-> float:
    vec1, vec2 = np.array(vec1), np.array(vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    if norm1 == 0 or norm2 == 0:
        return 0.0

    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
   
def find_relevant_chunks(question: str, chunks: list[str], top_n: int = 3) -> list[str]:
    """Return the top_n chunks most relevant to the question."""
    question_embedding = get_embedding(question)

    scored_chunks = []
    for chunk in chunks:
        chunk_embedding = get_embedding(chunk)
        score = cosine_similarity(question_embedding, chunk_embedding)
        scored_chunks.append((score, chunk))

    scored_chunks.sort(key=lambda x: x[0], reverse=True)

    return [chunk for score, chunk in scored_chunks[:top_n]]


