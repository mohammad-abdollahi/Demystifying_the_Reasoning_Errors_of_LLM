from typing import TypedDict, Literal
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_fireworks import ChatFireworks
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END, START
from langgraph.prebuilt import ToolNode
from langchain_core.messages import SystemMessage, HumanMessage
from src.state import AgentState
from src.tools import calculator
import os

# Define the system prompt
SYSTEM_PROMPT = """You are a precise code execution agent.
You are given a Python code snippet.
Your goal is to simulate the execution of the code step-by-step.

Rules:
1. Maintain the state of all variables in your mind (or scratchpad).
2. When you encounter ANY arithmetic operation (e.g., +, -, *, /, %, **), you MUST use the `calculator` tool. Do not calculate it yourself.
3. Show your reasoning for each step. "Line 1: assigning x=5. Line 2: calculating x*2..."
4. When execution is complete, provide the final return value clearly.

Code:
{code}
"""

def create_agent(provider="openai", model="o4-mini-2025-04-16"):
    # check for api key
    if provider == "openai":
        if not os.environ.get("OPENAI_API_KEY"):
            print("WARNING: OPENAI_API_KEY not found in environment variables.")
        llm = ChatOpenAI(model=model)
    elif provider == "anthropic":
        if not os.environ.get("ANTHROPIC_API_KEY"):
            print("WARNING: ANTHROPIC_API_KEY not found in environment variables.")
        llm = ChatAnthropic(model=model)
    elif provider == "fireworks":
        if not os.environ.get("FIREWORKS_API_KEY"):
            print("WARNING: FIREWORKS_API_KEY not found in environment variables.")
        llm = ChatFireworks(model=model)
    elif provider == "gemini" or provider == "google":
        if not os.environ.get("GOOGLE_API_KEY"):
            print("WARNING: GOOGLE_API_KEY not found in environment variables.")
        llm = ChatGoogleGenerativeAI(model=model)
    else:
        raise ValueError(f"Unsupported provider: {provider}")

    tools = [calculator]
    llm_with_tools = llm.bind_tools(tools)

    def reasoner(state: AgentState):
        messages = state['messages']
        # If this is the first step, prepend the system prompt
        if len(messages) == 1 and isinstance(messages[0], HumanMessage):
             # We inject the system prompt logic here or assume it's set up before.
             # Better: We construct the system prompt based on state['code'] and state['input_values']
             # But 'messages' is strictly the chat history.
             # We can add a SystemMessage to the list if not present?
             # Or just pass it in the invoke.
             pass
        
        # We need to construct the context if it's the start
        if len(messages) == 0:
             # Should not happen if triggered correctly
             return {"messages": []}
        
        # Construct the full prompt context
        # Actually, simpler to just let the graph handle messages.
        # But we need to inject the initial prompt.
        # We'll do that in main.py when initializing the state.
        
        response = llm_with_tools.invoke(messages)
        return {"messages": [response]}

    def should_continue(state: AgentState) -> Literal["tools", END]:
        messages = state['messages']
        last_message = messages[-1]
        
        if last_message.tool_calls:
            return "tools"
        return END

    workflow = StateGraph(AgentState)
    
    workflow.add_node("reasoner", reasoner)
    workflow.add_node("tools", ToolNode(tools))
    
    workflow.add_edge(START, "reasoner")
    workflow.add_conditional_edges("reasoner", should_continue)
    workflow.add_edge("tools", "reasoner")
    
    app = workflow.compile()
    return app
