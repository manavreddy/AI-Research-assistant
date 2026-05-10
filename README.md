# AI Research Assistant

An AI-powered research and decision assistant that uses Large Language Models (LLMs), tool orchestration, and Retrieval-Augmented Generation (RAG) to retrieve, reason over, and synthesize information from web sources and uploaded documents.

The system is designed as a modular agent architecture rather than a traditional chatbot. It can understand user intent, select appropriate tools, retrieve relevant context, and generate structured responses.

---

## Features

- Query understanding using LLMs
- Tool orchestration pipeline
- Web search integration
- Calculator tool for mathematical operations
- Retrieval-Augmented Generation (RAG)
- Semantic document retrieval using embeddings
- PDF ingestion and chunking
- Structured reasoning and response generation
- Modular AI agent architecture

---

## Architecture

```text
User Query
    ↓
Query Understanding Layer
    ↓
Orchestrator
    ↓
Tools
 ├── Calculator
 ├── Web Search
 └── RAG Retriever
    ↓
Reasoning Layer
    ↓
Final Response
```

---

## Project Structure

```text
AI-Research-Assistant/
│
├── core/
│   ├── orchestrator.py
│   ├── query_understanding.py
│   └── response_generation.py
│
├── tools/
│   ├── calculator.py
│   ├── web_search.py
│   └── rag_retriever.py
│
├── rag/
│   ├── ingestion.py
│   ├── retrieval.py
│   └── storage.py
│
├── data/
│   └── documents/
│
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

## Tech Stack

* Python
* Ollama
* Sentence Transformers
* Scikit-learn
* NumPy
* PyPDF
* Requests

---

## Environment Variables

Create a `.env` file in the root directory:

```env
OLLAMA_API_KEY=your_api_key
```

---

## Example Queries

```text
What is 25 * 12?

What does the document say about transformers?

Summarize the uploaded research paper

Search recent information about LLM agents
```

---

## RAG Pipeline

```text
PDF Document
    ↓
Text Extraction
    ↓
Chunking
    ↓
Embedding Generation
    ↓
Semantic Similarity Search
    ↓
Relevant Context Retrieval
    ↓
LLM Reasoning
```

---

## Current Capabilities

* Semantic retrieval from uploaded PDFs
* Tool-based reasoning workflow
* Multi-step orchestration pipeline
* Structured JSON-based intermediate state
* Modular and extensible architecture

---

## Future Improvements

* Persistent vector database
* FastAPI backend
* Streaming responses
* Better retrieval ranking
* Conversation memory
* Hybrid search (RAG + Web)
* Multi-document retrieval
* Frontend UI
