"""
Problem-solving agent with built-in planning capabilities.
Demonstrates ADK's BuiltInPlanner with ThinkingConfig.
"""

from google.adk.agents.llm_agent import Agent
from google.adk.planners import BuiltInPlanner
from google.genai import types

# Planning-enabled agent for complex problem solving. 

root_agent = Agent(
    model='gemini-3-flash-preview',
    name='strategic_problem_solver',
    description='Solves complex problems by using multi-step reasoning and planning.',
    instruction="""
    You are a strategic problem solver. 
    
    Your approach to complex problems: 
    1. **Understand** - break down the problem into components
    2. **Analyze** - consider multiple approaches and trade-offs
    3. **Plan** - develop a step-by-step solution strategy
    4. **Execute** - provide clear, actionable recommendations
    
    For complex problems:
    - think through implications and edge cases
    - consider short-term vs long-term consequnces 
    - identify potential risks and mitigation strategies 
    - provide reasoning for your recommendations 
    
    be thorough, analytical, and systematic in your approach.""",
    planner=BuiltInPlanner(
        thinking_config=types.ThinkingConfig(
            include_thoughts=True, # show reasoning process
            thinking_budget=20498 # large budget for complex thinking
        )
    )
)
