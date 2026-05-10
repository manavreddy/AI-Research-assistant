from core.Orchestrator import process_query
from Tools.Rag_retriever import ingest_document

# print(ingest_document("Attention.pdf"))

query = "What does the document say about transformers?"

response = process_query(query)
print(response)