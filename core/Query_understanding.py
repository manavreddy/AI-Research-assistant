import os
import json

from ollama import Client

def understand_query(query : str):
        # Example: "What does the document say about transformers?"
    prompt = '''You are a query understanding system. Return ONLY valid JSON (no extra text) following the exact schema below.

                Available tools (tool names are lowercase):

                1. calculator
                Use for:
                - mathematical calculations
                - arithmetic
                - equations

                Input schema:
                {
                    "expression": "<mathematical expression>"
                }

                2. web_search
                Use for:
                - recent information
                - public information
                - internet-based retrieval

                Input schema:
                {
                    "query": "<search query>"
                }

                3. rag_retriever
                Use for:
                - questions about uploaded/local documents
                - retrieving information from ingested PDFs
                - document-based answering

                Input schema:
                {
                    "query": "<document retrieval query>"
                }

                Respond with STRICT JSON ONLY using this exact top-level
                schema (no comments, no surrounding text):
                {
                    "task_type": "string",
                    "entities": ["string"],
                    "tools_required": [
                        {
                            "tool_name": "string",
                            "tool_input": {}
                        }
                    ]
                }

                Choose tools from the list above and populate `tool_input`
                to match each tool's input schema. Use `rag_retriever` when 
                the user's question requires information from uploaded or local documents.
                Use `web_search` for recent/public web info and `calculator` for math.'''

    client = Client(
        host='https://ollama.com',
        headers={'Authorization': 'Bearer ' + os.environ.get('OLLAMA_API_KEY')}
    )

    messages = [
        {'role': 'system', 'content' : prompt},
        {'role': 'user', 'content': query},
    ]

    try:
        response = client.chat(
            'gpt-oss:120b',
            messages=messages
        )
        final_query = response.message.content

    except Exception as e:
        return {
            "success": False,
            "error": f"LLM call failed: {str(e)}"
        }

    try:
        parsed_response = json.loads(final_query)

        return {
            "success": True,
            "data": parsed_response
        }

    except json.JSONDecodeError as e:
        return {
            "success": False,
            "error": f"Invalid JSON response from LLM: {str(e)}",
            "raw_response": final_query
        }