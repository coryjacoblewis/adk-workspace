# Model Comparison: Factual vs Creative

This document details the configuration strategy for the two specialized agents in the `model_comparison` project.

## 1. Orchestration Sequence
The following sequence diagram illustrates how a user interaction differs based on the chosen agent's configuration.

```mermaid
sequenceDiagram
    participant User
    
    rect rgb(225, 245, 254)
    Note over User, AgentF: Case A: Factual Agent (Temp 0.1)
    participant AgentF as Data Extractor
    User->>AgentF: "Extract prices from this text"
    AgentF->>AgentF: Deterministic Processing
    AgentF->>User: Precise, concise JSON/Facts
    end

    rect rgb(255, 244, 221)
    Note over User, AgentC: Case B: Creative Agent (Temp 0.9)
    participant AgentC as Creative Brainstormer
    User->>AgentC: "Give me 5 story ideas"
    AgentC->>AgentC: High-variance generation
    AgentC->>User: Diverse, imaginative suggestions
    end
```

## 2. Decision Logic Flow
The flowchart below maps out the architectural optimization for different use cases.

```mermaid
flowchart TD
    Start([User Request]) --> Goal{Identify Goal}

    subgraph Factual [Deterministic Output]
        FConfig[Low Temp: 0.1<br/>Top_P: 0.8<br/>Strict Safety]
        FGoal[Consistency & Accuracy]
    end

    subgraph Creative [Imaginative Output]
        CConfig[High Temp: 0.9<br/>Top_P: 0.95<br/>Pro Model]
        CGoal[Diversity & Innovation]
    end

    Goal -- "Extract Facts" --> Factual
    Goal -- "Brainstorm Ideas" --> Creative

    FGoal --> End([Final Response])
    CGoal --> End

    %% Styling
    classDef factual fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef creative fill:#fff4dd,stroke:#d4a017,stroke-width:2px;
    classDef decision fill:#ffffff,stroke:#333,stroke-dasharray: 5 5;

    class Factual factual;
    class Creative creative;
    class Goal decision;
```

## 3. Configuration Guidelines
*   **Temperature (0.1)**: Used for `data_extractor` to ensure factual consistency and minimize hallucinations.
*   **Temperature (0.9)**: Used for `creative_brainstormer` to encourage "outside the box" thinking and diverse outputs.
*   **Safety Thresholds**: Adjusted based on use case—stricter for factual data, more permissive for creative exploration.
*   **Model Selection**: Uses `gemini-3-flash` for fast factual extraction and `gemini-3.1-pro` for high-quality creative reasoning.
