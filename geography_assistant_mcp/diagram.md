# File Reader Assistant: MCP Integration

This document details the tool orchestration and filesystem exploration strategy for the `geography_assistant_mcp` (File Reader Assistant).

## 1. Orchestration Sequence
The following sequence diagram illustrates the "Explore-and-Read" pattern using MCP filesystem tools.

```mermaid
sequenceDiagram
    participant User
    participant Agent as File Reader Assistant
    participant MCP as MCP Filesystem Server

    User->>Agent: "What files are in the folder?"
    Agent->>MCP: list_directory(path="./my_files")
    MCP-->>Agent: ["notes.txt", "hello.txt"]
    Agent->>User: "I found: notes.txt, hello.txt"

    User->>Agent: "Read hello.txt"
    Agent->>MCP: read_file(path="./my_files/hello.txt")
    MCP-->>Agent: "Hello World!"
    Agent->>User: "The content of hello.txt is: Hello World!"
```

## 2. Decision Logic Flow
The flowchart below maps out the file exploration and retrieval process.

```mermaid
flowchart TD
    Start([User Message]) --> Identify{Identify Action}

    subgraph Explore [Directory Listing]
        CallList[[list_directory]]
        ListResult[Display Available Files]
    end

    subgraph Read [File Reading]
        CallRead[[read_file]]
        ReadResult[Display File Content]
    end

    Identify -- "List Files" --> CallList
    Identify -- "Read Content" --> CallRead
    Identify -- "Other" --> Help[Offer Help with Files]

    ListResult --> End([Final Response])
    ReadResult --> End
    Help --> End

    %% Styling
    classDef mcp fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef success fill:#d4edda,stroke:#28a745,stroke-width:2px;
    classDef decision fill:#fff4dd,stroke:#d4a017,stroke-width:2px;

    class CallList,CallRead mcp;
    class Identify decision;
    class ListResult,ReadResult success;
```

## 3. Communication Guidelines
*   **Contextual Awareness**: Always be clear about which folder and files are being accessed.
*   **Descriptive Discovery**: When listing files, describe them in a way that helps the user decide what to read next.
*   **Security Focus**: Only operate within the `ALLOWED_PATH` configured for the MCP server.
