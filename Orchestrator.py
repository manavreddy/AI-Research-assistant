import json

from Query_understanding import understand_query
from Tools.Calculator import calculator
from Tools.Web_search import web_search

def process_query(query : str):
    structured_query = understand_query(query)

    if not structured_query["success"] : 
        return structured_query["error"]
    
    tools = {"web_search" : Web_search, "calculator" : Calculator}

       
    tool_outputs = []
    #tool calling
    for tool_info in structured_query["data"]["tools_required"]:
        if tool_info["tool_name"] not in tools:
            continue
        tool_function = tools[tool_info["tool_name"]]
        tool_input = tool_info["tool_input"]

        result = tool_function(tool_input)
        if not result["success"]:
            continue
        tool_outputs.append({
            "tool": tool_info["tool_name"],
            "output": result["tool_output"]
        })
    
    return generate_response(query, structured_query, tool_outputs)

