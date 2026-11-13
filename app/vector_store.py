from langchain_chroma import Chroma

# Create and store document embeddings
def create_vector_store(
    documents,
    embedding_model,
    persist_directory="chroma_db"
):

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embedding_model,
        persist_directory=persist_directory,
        collection_name="research_documents"
    )

    return vector_store


# Load an existing vector database
def load_vector_store(
    embedding_model,
    persist_directory="chroma_db"
):

    vector_store = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding_model,
        collection_name="research_documents"
    )

    return vector_store