# Travel Agent: Flight & Hotel Orchestration

This document details the tool coordination and budget calculation logic for the `travel_agent`.

## 1. Orchestration Sequence
The following sequence diagram illustrates the multi-tool workflow for a full trip estimate.

```mermaid
sequenceDiagram
    participant User
    participant Agent as Travel Agent
    participant Tools as Toolset (Python)

    User->>Agent: "Plan a 3-night trip to Paris"
    
    rect rgb(225, 245, 254)
    Note over Agent,Tools: Step 1: Search Flights
    Agent->>Tools: search_flights(destination="Paris", ...)
    Tools-->>Agent: {"status":"success", "flights": [...]}
    end

    rect rgb(225, 245, 254)
    Note over Agent,Tools: Step 2: Search Hotels
    Agent->>Tools: search_hotels(city="Paris", ...)
    Tools-->>Agent: {"status":"success", "hotels": [...]}
    end

    rect rgb(225, 245, 254)
    Note over Agent,Tools: Step 3: Calculate Budget
    Agent->>Tools: calculate_trip_budget(flight_price=450, hotel_price=150, num_nights=3)
    Tools-->>Agent: {"status":"success", "total_usd": 900, ...}
    end

    Agent->>User: Present options & total estimate
```

## 2. Decision Logic Flow
The flowchart below maps out the intent identification and tool selection process.

```mermaid
flowchart TD
    Start([User Message]) --> Intent{Identify Intent}

    subgraph Flights [Flight Search]
        CallFlights[[search_flights]]
        FlightResult{Success?}
    end

    subgraph Hotels [Hotel Search]
        CallHotels[[search_hotels]]
        HotelResult{Success?}
    end

    subgraph Budget [Budget Calculation]
        CallBudget[[calculate_trip_budget]]
    end

    Intent -- Flights --> CallFlights
    Intent -- Hotels --> CallHotels
    Intent -- "Full Estimate" --> CallFlights
    
    FlightResult -- Yes --> CallHotels
    HotelResult -- Yes --> CallBudget
    
    FlightResult -- No --> Suggest[Suggest Paris/Tokyo]
    HotelResult -- No --> Suggest

    CallBudget --> Present[Present Total & Options]
    Suggest --> End([Final Response])
    Present --> End

    %% Styling
    classDef tool fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef decision fill:#fff4dd,stroke:#d4a017,stroke-width:2px;
    classDef success fill:#d4edda,stroke:#28a745,stroke-width:2px;

    class CallFlights,CallHotels,CallBudget tool;
    class Intent,FlightResult,HotelResult decision;
    class Present success;
```

## 3. Communication Guidelines
*   **Comprehensive Planning**: When a full trip is requested, always coordinate flights, hotels, and budget calculations.
*   **Clear Presentation**: Present options with flight numbers, hotel names, and specific prices clearly formatted.
*   **Error Recovery**: If a destination is unsupported, suggest "Paris" or "Tokyo" as available alternatives.
*   **Friendly Assistance**: Maintain a helpful, enthusiastic "Travel Agent" persona throughout the interaction.
