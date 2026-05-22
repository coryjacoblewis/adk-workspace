# Research Assistant: Real-Time Grounding

This document details the tool orchestration and source-citing strategy for the `research_assistant`.

## 1. Orchestration Sequence
The following sequence diagram illustrates how the agent uses Google Search to provide up-to-date information.

```mermaid
sequenceDiagram
    participant User
    participant Agent as Research Assistant
    participant Tool as google_search

    User->>Agent: "What happened in the news today?"
    Agent->>Tool: google_search(query="current news...")
    Tool-->>Agent: [Source A, Source B, Source C]
    Agent->>Agent: Analyze & Synthesize
    Agent->>User: "Based on [Source A] and [Source B], today..."
```

## 2. Decision Logic Flow
The flowchart below maps out the search and citation process.

```mermaid
flowchart TD
    Start([User Question]) --> Intent{Requires Current Info?}
    
    Intent -- No --> KnowledgeBase[Respond from Internal Knowledge]
    Intent -- Yes --> CallSearch[[google_search]]

    CallSearch --> Result{Sufficient Info?}
    
    Result -- Yes --> Synthesize[Synthesize & Cite Sources]
    Result -- No --> Limitations[Acknowledge Limitations]

    KnowledgeBase --> End([Final Response])
    Synthesize --> End
    Limitations --> End

    %% Styling
    classDef tool fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef success fill:#d4edda,stroke:#28a745,stroke-width:2px;
    classDef decision fill:#fff4dd,stroke:#d4a017,stroke-width:2px;

    class CallSearch tool;
    class Intent,Result decision;
    class Synthesize success;
```

## 3. Communication Guidelines
*   **Prioritize Accuracy**: Always prioritize factual accuracy over speculative generation.
*   **Mandatory Citation**: Always cite sources when providing information found via Google Search.
*   **Acknowledge Limitations**: If search results are insufficient or ambiguous, be honest about what you cannot find.
*   **Up-to-Date Focus**: Use Google Search whenever a query involves current events or rapidly changing information.
