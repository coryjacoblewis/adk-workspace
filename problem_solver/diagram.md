# Strategic Problem Solver: Planning & Reasoning

This document details the planning capabilities and systematic reasoning process for the `problem_solver`.

## 1. Orchestration Sequence
The following sequence diagram illustrates how the agent uses the `BuiltInPlanner` to think through complex problems.

```mermaid
sequenceDiagram
    participant User
    participant Agent as Strategic Problem Solver
    participant Planner as BuiltInPlanner

    User->>Agent: "How should I approach [Complex Problem]?"
    Agent->>Planner: Request Thinking/Planning
    Note right of Planner: Multi-step reasoning<br/>Risk analysis<br/>Trade-off evaluation
    Planner-->>Agent: Detailed Plan & Thoughts
    Agent->>Agent: Finalize Recommendations
    Agent->>User: "Here is a strategic approach: 1. Understand... 2. Analyze..."
```

## 2. Decision Logic Flow
The flowchart below maps out the systematic 4-step problem-solving approach.

```mermaid
flowchart TD
    Start([Complex Problem]) --> Understand[1. Understand: Break down components]
    Understand --> Analyze[2. Analyze: Approaches & Trade-offs]
    Analyze --> Plan[3. Plan: Step-by-step strategy]
    Plan --> Execute[4. Execute: Clear recommendations]

    subgraph Thinking [Internal Reasoning]
        Direction[Consider Implications]
        Risks[Identify Risks]
        EdgeCases[Evaluate Edge Cases]
    end

    Analyze -.-> Thinking
    Thinking -.-> Plan

    Execute --> End([Final Strategy])

    %% Styling
    classDef process fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef thinking fill:#fff4dd,stroke:#d4a017,stroke-width:1px,stroke-dasharray: 5 5;
    classDef success fill:#d4edda,stroke:#28a745,stroke-width:2px;

    class Understand,Analyze,Plan process;
    class Thinking,Direction,Risks,EdgeCases thinking;
    class Execute success;
```

## 3. Communication Guidelines
*   **Systematic Approach**: Always follow the Understand-Analyze-Plan-Execute framework.
*   **Transparency**: Share the reasoning process and identified trade-offs.
*   **Risk Awareness**: Proactively identify potential risks and mitigation strategies.
*   **Actionable Advice**: Ensure recommendations are clear, thorough, and actionable.
