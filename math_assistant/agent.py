"""
Math Assistant Agent
Demonstrates ADK's Code Execution built-in tool for calculations
"""

from google.adk.agents.llm_agent import Agent
from google.adk.code_executors import BuiltInCodeExecutor # Import code executor 

# Create math assistant with code execution

root_agent = Agent(
    model='gemini-3-flash-preview',
    name='math_assistant',
    description='Helps users with mathematical calculations and analysis.',
    instruction="""You are a math assistant that helps users with calculations and mathematical analysis.
    
    Your capabilities:
    1. When users ask for calculations, use code execution for precision.
    2. Show your work by explaining the calculation steps.
    3. Verify results by running the code.
    4. Handle complex mathematical operations (statistics, algebra, etc.).
    """,
    code_executor=BuiltInCodeExecutor() # enable code execution
)
