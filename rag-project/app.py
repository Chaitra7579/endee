from vector_store import store_documents, search

documents = [
    "Endee is a vector database for AI applications",
    "Semantic search retrieves results based on meaning",
    "Retrieval Augmented Generation combines search with generation"
]

store_documents(documents)

query = "What is semantic search?"
results = search(query)

print("Search Results:")
for r in results:
    print("-", r)
