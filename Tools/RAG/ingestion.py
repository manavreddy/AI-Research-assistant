import numpy as np
import Tools.RAG.storage as storage

from pypdf import PdfReader
from typing import List
from sentence_transformers import SentenceTransformer

# In-memory embedding store
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(chunks : List[str]) -> np.ndarray:

    embeddings = embedding_model.encode(chunks)

    return np.array(embeddings).astype('float32')

def store_embeddings(chunks : List[str], embeddings : np.ndarray):
    storage.documents = chunks
    storage.embeddings_list = embeddings

def chunk_text(text: str, chunk_size = 500) -> List[str]:
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks 


def ingest_document(pdf_path):
    """Load PDF and store embeddings."""
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

        chunks = chunk_text(text)
        embeddings = generate_embeddings(chunks)
        store_embeddings(chunks, embeddings)
        return {"success": True, "chunks_stored": len(chunks)}
    except Exception as e:
        return {"success": False, "error": str(e)}