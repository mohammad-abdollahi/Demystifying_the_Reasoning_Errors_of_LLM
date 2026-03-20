import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from src.agent import create_agent, SYSTEM_PROMPT

# Load environment variables
load_dotenv()

def main():
    # Sample inputs
    code_snippet = "\ndef special_factorial(n):\n    \"\"\"The Brazilian factorial is defined as:\n    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!\n    where n > 0\n\n    For example:\n    >>> special_factorial(4)\n    288\n\n    The function will receive an integer as input and should return the special\n    factorial of this integer.\n    \"\"\"\n\n\n    fac, ans = 1, 1\n    for i in range(2, n + 1):\n        fac *= i\n        ans *= fac\n    return ans\n\nprint(special_factorial(45))"
    
    print("--- Starting Agent Execution ---")
    print(f"Code:\n{code_snippet}")
    
    # Initialize the agent
    app = create_agent()
    
    # Prepare the initial state
    formatted_system_prompt = SYSTEM_PROMPT.format(
        code=code_snippet
    )
    
    initial_state = {
        "messages": [SystemMessage(content=formatted_system_prompt), HumanMessage(content="Start execution.")],
        "code": code_snippet,
        "variables": {}
    }
    
    # Run the graph
    # We use stream to see steps
    try:
        final_state = app.invoke(initial_state)
        
        print("\n--- Execution Trace ---")
        for msg in final_state['messages']:
            if msg.type == 'ai':
                 print(f"[Agent]: {msg.content}")
                 if hasattr(msg, 'tool_calls') and msg.tool_calls:
                     print(f"  [Tool Calls]: {msg.tool_calls}")
            elif msg.type == 'tool':
                 print(f"[Tool Output]: {msg.content}")
        
        print("\n--- Final Result ---")
        # The last message should contain the result
        print(final_state['messages'][-1].content)
        
    except Exception as e:
        print(f"Error during execution: {e}")
        # Check if it's an API key error
        if "api_key" in str(e).lower():
            print("\nPlease ensure OPENAI_API_KEY is set in your .env file or environment.")

if __name__ == "__main__":
    main()
