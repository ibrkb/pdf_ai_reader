import chromadb
from embeddings import get_embedding
client = chromadb.PersistentClient(
    path="./chroma_db"
)
collection = client.get_or_create_collection(
    name = 'pdf_documents'
)


def add_chunks_to_database(chunks, source):
    ids = []
    embeddings = []
    metadatas = []

    for index, chunk in enumerate(chunks):

        chunk_id = f"{source}_chunk_{index}"
        if not chunk.strip() :
            continue
        embedding = get_embedding(chunk)

        ids.append(chunk_id)
        embeddings.append(embedding)

        metadatas.append({
            "source": source,
            "chunk_index": index
        })

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print(f"Saved {len(chunks)} chunks to ChromaDB")


def search_chunks(question,n_results=3):
    question_embedding = get_embedding(question)
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=n_results
    )
    documents = results["documents"][0]

    return documents