"""
Calculator Tool: Evaluates mathematical expressions safely.
"""
import math
import re


def calculator(tool_input):
    """
    Evaluates mathematical expressions.
    Args:
        tool_input: Dictionary containing "expression" key with the math expression to evaluate
    Returns:
        Dictionary with "success" (bool) and "tool_output" (result or error message)
    """
    try:
        # Validate input
        if not isinstance(tool_input, dict):
            return {"success": False, 
                    "tool_output": None,
                    "error": "tool_input must be a dictionary"}
        
        expression = tool_input.get("expression")

        if not isinstance(expression, str):
            return {
                "success": False,
                "tool_output": None,
                "error": "Expression must be a string"
            }

        expression = expression.strip().lower()
        
        if not expression:
            return {"success": False,
                    "tool_output": None, 
                    "error": "No expression provided. "
                    "Please provide a mathematical expression."}
        
        # Basic security check: only allow safe characters
        # Allow numbers, operators, math functions, parentheses, and whitespace
        allowed_pattern = r'^[0-9a-z+\-*/().,%\s]+$'
        if not re.fullmatch(allowed_pattern, expression, re.IGNORECASE):
            return {"success": False,
                    "tool_output": None,
                    "error": "Expression contains invalid characters."
                    " Only mathematical operations are allowed."}
        
        # Create a restricted namespace with math functions
        safe_dict = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'sqrt': math.sqrt,
            'log': math.log,
            'log10': math.log10,
            'exp': math.exp,
            'abs': abs,
            'pow': pow,
            'max': max,
            'min': min,
            'pi': math.pi,
            'e': math.e,
        }
        # Evaluate the expression
        result = eval(expression, {"__builtins__": None}, safe_dict)
        
        # Format the result
        if isinstance(result, float):
            # Round to 10 decimal places to avoid floating point precision issues
            result = round(result, 10)
        
        return {"success": True, "tool_output": result, "error" : None}
    
    except ZeroDivisionError:
        return {"success": False,
                "tool_output" : None, 
                "error": "Division by zero is not allowed"}
    
    except ValueError as e:
        return {"success": False, 
                "tool_output": None,
                "error": f"Error: Invalid mathematical value - {str(e)}"}
    
    except SyntaxError:
        return {"success": False, 
                "tool_output": None,
                "error" : "Invalid expression syntax. Please check your mathematical expression."}
    
    except Exception as e:
        return {"success": False, 
                "tool_output": None,
                "error": str(e)}
