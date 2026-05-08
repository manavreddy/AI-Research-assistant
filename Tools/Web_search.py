"""
Web Search Tool: Retrieves structured search data using DuckDuckGo free API.

Returns machine-readable structured data (not formatted text).
Formatting/presentation is handled by the reasoning layer.
"""

import requests
from typing import Dict, List, Optional
import json


def web_search(tool_input):
    """
    Performs web search and returns structured data.
    
    Args:
        tool_input: Dictionary containing "query" key with the search query
        
    Returns:
        Dictionary with structure:
        {
            "success": bool,
            "tool_output": {structured search results} or None,
            "error": error_message or None
        }
    """
    try:
        # Validate input type
        if not isinstance(tool_input, dict):
            return {
                "success": False,
                "tool_output": None,
                "error": "tool_input must be a dictionary"
            }
        
        query = tool_input.get("query")
        
        # Validate query is string
        if not isinstance(query, str):
            return {
                "success": False,
                "tool_output": None,
                "error": "query must be a string"
            }
        
        query = query.strip().lower()
        
        if not query:
            return {
                "success": False,
                "tool_output": None,
                "error": "No search query provided"
            }
        
        # Limit query length to avoid abuse
        if len(query) > 200:
            return {
                "success": False,
                "tool_output": None,
                "error": "Search query exceeds 200 character limit"
            }
        
        # Prepare request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        url = "https://api.duckduckgo.com/"
        params = {
            'q': query,
            'format': 'json',
            't': 'ai_research_assistant'
        }
        
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Extract structured data (no formatting)
        instant_answer = None
        if data.get('AbstractText'):
            instant_answer = {
                "title": data.get('AbstractTitle'),
                "text": data.get('AbstractText'),
                "source": data.get('AbstractSource')
            }
        
        # Extract related topics as raw data
        results = []
        for topic in data.get('RelatedTopics', [])[:10]:  # Keep raw, let reasoning layer decide limit
            if isinstance(topic, dict) and topic.get('Text'):
                results.append({
                    "title": topic.get('Text'),
                    "url": topic.get('FirstURL'),
                    "icon": topic.get('Icon')
                })
        
        # Return structured data
        tool_output = {
            "query": query,
            "instant_answer": instant_answer,
            "results": results,
            "total_results": len(results)
        }
        
        return {
            "success": True,
            "tool_output": tool_output,
            "error": None
        }
    
    except requests.exceptions.Timeout:
        return {
            "success": False,
            "tool_output": None,
            "error": "Search request timed out"
        }
    
    except requests.exceptions.ConnectionError:
        return {
            "success": False,
            "tool_output": None,
            "error": "Unable to connect to search service"
        }
    
    except requests.exceptions.HTTPError as e:
        return {
            "success": False,
            "tool_output": None,
            "error": f"HTTP error: {str(e)}"
        }
    
    except json.JSONDecodeError:
        return {
            "success": False,
            "tool_output": None,
            "error": "Invalid response format from search service"
        }
    
    except Exception as e:
        return {
            "success": False,
            "tool_output": None,
            "error": str(e)
        }
