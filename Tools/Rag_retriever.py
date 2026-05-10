import numpy as np

from RAG.retrieval import retrieve

documents = []
embeddings_list = []

def rag_retriever(tool_input):
    """RAG retriever tool - returns structured data."""
    try:
        if not isinstance(tool_input, dict):
            return {"success": False, "tool_output": None, "error": "tool_input must be a dictionary"}
        
        query = tool_input.get("query")
        if not isinstance(query, str):
            return {"success": False, "tool_output": None, "error": "query must be a string"}
        
        if not query.strip():
            return {"success": False, "tool_output": None, "error": "query cannot be empty"}
        
        retrieved_chunks = retrieve(query)
        
        return {
            "success": True,
            "tool_output": {
                "query": query,
                "chunks": retrieved_chunks,
                "count": len(retrieved_chunks)
            },
            "error": None
        }
    except Exception as e:
        return {"success": False, "tool_output": None, "error": str(e)}