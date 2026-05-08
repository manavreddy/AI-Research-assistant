import os
import json

from ollama import Client
# from ollama import chat

def understand_query(query : str):
    prompt = ''' You are a query understanding system.
                Return ONLY valid JSON in this schema:
                {
                "task_type": "",
                "entities": [],
                "tools_required": [
                    "tool_name": []
                    "tool_input": []
                ]
                }'''

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