# Math Assistant: Code Execution for Precision

This document details the code execution orchestration and verification logic for the `math_assistant`.

## 1. Orchestration Sequence
The following sequence diagram illustrates how the agent uses the built-in code executor to solve mathematical problems.

```mermaid
sequenceDiagram
    participant User
    participant Agent as Math Assistant
    participant Executor as BuiltInCodeExecutor (Python)

    User->>Agent: "What is 1234 * 5678?"
    Agent->>Agent: Break down problem
    Agent->>Executor: Execute: print(1234 * 5678)
    Executor-->>Agent: 7006652
    Agent->>Agent: Verify result
    Agent->>User: "1234 * 5678 is 7,006,652. (Steps: ...)"
```

## 2. Decision Logic Flow
The flowchart below maps out the calculation and explanation strategy.

```mermaid
flowchart TD
    Start([User Math Problem]) --> Analyze[Analyze Complexity]
    Analyze --> Choice{Needs Code?}

    Choice -- No --> SimpleAns[Provide Direct Answer]
    Choice -- Yes --> CallExecutor[[BuiltInCodeExecutor]]

    CallExecutor --> Verify[Verify & Format Results]
    Verify --> Explain[Explain Calculation Steps]

    SimpleAns --> End([Final Response])
    Explain --> End

    %% Styling
    classDef tool fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef success fill:#d4edda,stroke:#28a745,stroke-width:2px;
    classDef decision fill:#fff4dd,stroke:#d4a017,stroke-width:2px;

    class CallExecutor tool;
    class Choice decision;
    class Verify,Explain success;
```

## 3. Communication Guidelines
*   **Precision First**: Use code execution for complex calculations to ensure accuracy.
*   **Show Your Work**: Always explain the mathematical steps taken to arrive at the result.
*   **Verification**: Run code to verify results before presenting them to the user.
*   **Broad Capability**: Handle statistics, algebra, and other complex operations systematically.
