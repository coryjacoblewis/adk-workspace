# Product Extractor: Structured JSON Output

This document details the extraction logic and structured data schema for the `product_extractor`.

## 1. Interaction Sequence
The following sequence diagram illustrates how the agent transforms natural language into structured JSON data.

```mermaid
sequenceDiagram
    participant User
    participant Agent as Product Extractor
    participant Schema as ProductInfo (Pydantic)

    User->>Agent: "I just bought a Space Black iPhone 15 for $999 with 256GB"
    Agent->>Agent: Extract entities
    Agent->>Schema: Validate against ProductInfo
    Schema-->>Agent: Validated Object
    Agent->>User: { "product_name": "iPhone 15", "price": 999.0, ... }
```

## 2. Decision Logic Flow
The flowchart below maps out the extraction and validation process.

```mermaid
flowchart TD
    Start([User Message]) --> Parse[Read Message]
    Parse --> Extract{Extract Fields}

    subgraph Validation [Pydantic Validation]
        Name[Product Name]
        Price[Price as Float]
        Storage[Storage with Unit]
        Color[Color / Not Specified]
    end

    Extract --> Name
    Extract --> Price
    Extract --> Storage
    Extract --> Color

    Name & Price & Storage & Color --> SchemaMatch{Matches Schema?}
    
    SchemaMatch -- Yes --> OutputJSON[Return Valid JSON]
    SchemaMatch -- No --> Retry[Refine Extraction]
    
    Retry --> Extract
    OutputJSON --> End([Final JSON Response])

    %% Styling
    classDef process fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef decision fill:#fff4dd,stroke:#d4a017,stroke-width:2px;
    classDef success fill:#d4edda,stroke:#28a745,stroke-width:2px;

    class Parse,Name,Price,Storage,Color process;
    class Extract,SchemaMatch decision;
    class OutputJSON success;
```

## 3. Communication Guidelines
*   **JSON Only**: Respond ONLY with valid JSON matching the `ProductInfo` schema.
*   **Strict Typing**: Ensure prices are numbers (no currency symbols) and storage includes units (GB/TB).
*   **Default Handling**: If color is not mentioned, always use "Not specified".
*   **No Preamble**: Do not include conversational filler or explanation text in the output.
