




def retrieve_documents(vector_store, query: str, k: int = 5):

    # Search ChromaDB for the most similar documents
    results = vector_store.similarity_search(
        query,
        k=k
    )

    return results