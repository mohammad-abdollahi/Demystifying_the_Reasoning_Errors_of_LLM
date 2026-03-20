from langchain_core.tools import tool

@tool
def calculator(a: float, b: float, operation: str) -> float:
    """
    Perform a basic arithmetic operation on two numbers.
    Supported operations: +, -, *, /, % (modulo), ** (power).
    """
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return float('inf') # Or raise an error
        return a / b
    elif operation == "**" or operation == "^":
        return a ** b
    elif operation == "%":
        return a % b
    else:
        raise ValueError(f"Unknown operation: {operation}")
