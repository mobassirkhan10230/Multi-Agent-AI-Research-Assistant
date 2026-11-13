from app.tools import load_pdf, chunk_documents
from app.embeddings import create_embeddings
from app.vector_store import create_vector_store, load_vector_store


path = "app/docs.pdf"

pdf_docs = load_pdf(path)

chunks = chunk_documents(pdf_docs)

model = create_embeddings()

vector_store = create_vector_store(
    documents = chunks,
    embedding_model = model
)

print("Documents stored successfully!")

query = input("you : ")

results = vector_store.similarity_search(
    query,
    k=3
)

# 6. Display results
for i, result in enumerate(results, start=1):

    print(f"\nResult {i}")

    print("Source:", result.metadata.get("source"))

    print("Page:", result.metadata.get("page"))

    print("Content:", result.page_content[:300])



