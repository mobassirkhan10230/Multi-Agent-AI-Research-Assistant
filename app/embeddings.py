from sentence_transformers import SentenceTransformer
from langchain_core.embeddings import Embeddings


class LocalEmbeddings(Embeddings):

    def __init__(self):
        # Load the local embedding model
        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2",
            local_files_only=True
        )

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        # Generate embeddings for multiple document chunks
        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True
        )

        return embeddings.tolist()

    def embed_query(self, text: str) -> list[float]:
        # Generate embedding for a single search query
        embedding = self.model.encode(
            text,
            convert_to_numpy=True
        )

        return embedding.tolist()


def create_embeddings():
    return LocalEmbeddings()