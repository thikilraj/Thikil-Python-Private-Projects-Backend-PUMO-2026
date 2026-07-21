import chromadb

# Create a local vector database
client = chromadb.PersistentClient(path="./rag_database")

# Create a collection
collection = client.get_or_create_collection(
    name="knowledge_base"
)

# Add knowledge documents
documents = [
    "Python is a popular programming language used for web development, AI, and data science.",
    "Machine learning allows computers to learn patterns from data.",
    "RAG combines document retrieval with language generation to answer questions using external knowledge.",
    "Vector databases store documents as numerical representations called embeddings."
]

collection.add(
    documents=documents,
    ids=["doc1", "doc2", "doc3", "doc4"]
)

# Ask a question
question = input("Ask a question: ")

# Retrieve relevant documents
results = collection.query(
    query_texts=[question],
    n_results=2
)

retrieved_documents = results["documents"][0]

# Simple answer generation
answer = "Based on the retrieved information:\n\n"

for document in retrieved_documents:
    answer += "- " + document + "\n"

# Display results
print("\n----- RETRIEVED DOCUMENTS -----")

for document in retrieved_documents:
    print(document)

print("\n----- GENERATED ANSWER -----")
print(answer)