import numpy as np
import Tools.RAG.storage as storage

from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def similarity_search(query_embedding, k=3):
    """Search for k most similar documents using cosine similarity."""
    if len(storage.embeddings_list) == 0 or len(storage.documents) == 0:
        return []
    
    # Calculate cosine similarities
    similarities = cosine_similarity([query_embedding], storage.embeddings_list)[0]
    
    # Get indices of top-k most similar
    top_indices = np.argsort(similarities)[::-1][:k]
    
    # Return the most similar chunks
    results = []
    for idx in top_indices:
        if idx < len(storage.documents):
            results.append(storage.documents[idx])
    
    return results

def retrieve(query: str, k=3):
    """Retrieve relevant chunks for a query."""
    if not query.strip():
        return []
    
    query_embedding = embedding_model.encode([query])[0]
    relevant_chunks = similarity_search(query_embedding, k)
    
    return relevant_chunks