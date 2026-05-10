import os
import json


from ollama import Client

def generate_response(query : str, structured_query : dict, tool_outputs : list):
    system_prompt = '''Use the provided tool outputs to answer the user query.
                    Base your response only on available information.
                    Structure response clearly.'''
    
    client = Client(
        host='https://ollama.com',
        headers={'Authorization': 'Bearer ' + os.environ.get('OLLAMA_API_KEY')}
    )
    # print(f''' tool_outputs : {tool_outputs}''')
    if not tool_outputs:
        return{
            "success" : False,
            "response" : None,
            "error" : "No tool outputs provided to summarize."
        }
    messages = [
        {'role': 'system', 'content' : system_prompt},
        {'role': 'user', 'content': 
         f'''query : {query}
        structured_query : {json.dumps(structured_query, indent=2)}
        tool_outputs : {json.dumps(tool_outputs, indent=2)}''' },
    ]

    try:
        response = client.chat(
            'gpt-oss:120b',
            messages=messages
        )
        final_response = response.message.content

    except Exception as e:
        return {
            "success": False,
            "response": None,
             "error": f"LLM call failed: {str(e)}"
        }
    return{
        "success": True,
        "response" : final_response,
        "error" : None
    }