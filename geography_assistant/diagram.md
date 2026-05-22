# Geography Assistant: Knowledge & Education

This document details the tool orchestration and educational strategy for the `geography_assistant`.

## 1. Orchestration Sequence
The following sequence diagram illustrates how the agent retrieves capital city information using its dedicated tool.

```mermaid
sequenceDiagram
    participant User
    participant Agent as Geography Assistant
    participant Tool as get_capital_city

    User->>Agent: "What is the capital of France?"
    Agent->>Tool: get_capital_city(country="france")
    Tool-->>Agent: "Paris"
    Agent->>Agent: Add educational context/facts
    Agent->>User: "The capital of France is Paris..."
```

## 2. Decision Logic Flow
The flowchart below maps out the lookup process and error handling.

```mermaid
flowchart TD
    Start([User Question]) --> Intent{Is it about a Capital?}
    Intent -- No --> FriendlyResp[Friendly Educational Response]
    Intent -- Yes --> CallTool[[get_capital_city]]

    CallTool --> Result{Found?}
    Result -- Yes --> ProvideInfo[Provide Capital + Fun Facts]
    Result -- No --> Apologize[Politely state info unavailable]

    FriendlyResp --> End([Final Response])
    ProvideInfo --> End
    Apologize --> End

    %% Styling
    classDef tool fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef decision fill:#fff4dd,stroke:#d4a017,stroke-width:2px;
    classDef success fill:#d4edda,stroke:#28a745,stroke-width:2px;

    class CallTool tool;
    class Intent,Result decision;
    class ProvideInfo success;
```

## 3. Communication Guidelines
*   **Educational Tone**: Always aim to be friendly and educational, not just providing data.
*   **Proactive Enrichment**: Add interesting geography facts when possible.
*   **Graceful Failure**: If a country isn't in the database, apologize politely and maintain a helpful attitude.
