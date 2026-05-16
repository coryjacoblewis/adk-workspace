# Travel Agent Architecture

Here is a Mermaid diagram representing the flow and structure of the `travel_agent`. It illustrates the LLM acting as the central router that invokes specific custom tools based on the user's input:

```mermaid
graph TD
    User([User Input]) --> Agent["Travel Agent<br/><i>(gemini-3-flash-preview)</i>"]
    
    subgraph CustomTools["Custom Tools"]
        Tool_Flight["fa:fa-plane <b>search_flights</b><br/>(destination, departure_date)"]
        Tool_Hotel["fa:fa-bed <b>search_hotels</b><br/>(city, check_in_date)"]
        Tool_Budget["fa:fa-calculator <b>calculate_trip_budget</b><br/>(flight_price, hotel_price, num_nights)"]
    end
    
    Agent -- "If asked about flights" --> Tool_Flight
    Tool_Flight -. "Flight options/prices" .-> Agent
    
    Agent -- "If asked about hotels" --> Tool_Hotel
    Tool_Hotel -. "Hotel options/prices" .-> Agent
    
    Agent -- "If wants full trip estimate" --> Tool_Budget
    Tool_Budget -. "Total cost & breakdown" .-> Agent
    
    Agent --> Output([Final Formatted Response])
```

### Breakdown of the Agent Logic:
* **The Agent (`gemini-3-flash-preview`)**: Acts as the central orchestrator, analyzing the intent of the user.
* **`search_flights`**: Triggered when the user asks for flight availability to supported destinations (Paris or Tokyo).
* **`search_hotels`**: Triggered when the user needs accommodations in a specific city.
* **`calculate_trip_budget`**: Triggered after pulling flight and hotel prices to give a final breakdown of the trip's estimated cost. 

The agent iterates over these tools until it has all the necessary information to present the final trip details clearly to the user.
