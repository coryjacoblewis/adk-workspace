# Customer Support Agent: Strategy & Logic

This document details the orchestration logic and tool coordination for the `customer_support` agent.

## 1. Orchestration Sequence
The following sequence diagram illustrates the "Verification-First" pattern and how the agent coordinates multiple tools to fulfill complex requests like refunds.

```mermaid
sequenceDiagram
    participant User
    participant Agent as Customer Support Agent
    participant Tools as Toolset (Python)

    User->>Agent: "I want a refund for ORD123"
    Agent->>Agent: Express Empathy
    
    Note over Agent,Tools: Step 1: Pre-validation
    Agent->>Tools: check_order_status(order_id="ORD123")
    Tools-->>Agent: {"status":"success", "order_status":"delivered", ...}

    Note over Agent,Tools: Step 2: Action (Conditional)
    Agent->>Tools: process_refund(order_id="ORD123", reason="...")
    Tools-->>Agent: {"status":"success", "refund_amount": 99.99, ...}
    
    Agent->>User: Confirm Refund & Reference Number
```

## 2. Decision Logic Flow
The flowchart below maps out the comprehensive error handling and escalation paths for all supported intents.

```mermaid
flowchart TD
    Start([User Message]) --> Greet[Greet & Empathize]
    Greet --> Intent{Identify Intent}

    subgraph Status [Order Status]
        CallStatus1[[check_order_status]]
        StatusResult1{Result?}
        StatusResult1 -- Success --> ProvideDetails[Provide Details]
        StatusResult1 -- Not Found --> AskVerify[Ask to verify ID/Email]
        StatusResult1 -- Invalid --> ExplainFormat[Explain ORD format]
    end

    subgraph Refund [Refund Process]
        CallStatus2[[check_order_status]]
        StatusResult2{Exists?}
        StatusResult2 -- No --> AskVerify
        StatusResult2 -- Yes --> CallRefund[[process_refund]]
        
        CallRefund --> RefundResult{Result?}
        RefundResult -- Success --> ConfirmRefund[Confirm Refund]
        RefundResult -- Error --> ExplainPolicy[Explain: Delivered only]
        ExplainPolicy --> OfferEscalation[Offer Escalation]
    end

    subgraph Escalation [Escalation]
        CallEscalate[[escalate_to_supervisor]]
        ProvideTicket[Provide Ticket & ETA]
    end

    Intent -- Status --> CallStatus1
    Intent -- Refund --> CallStatus2
    Intent -- Frustrated --> CallEscalate
    
    OfferEscalation -- Accepted --> CallEscalate
    ProvideDetails -- "Still Unhappy" --> CallEscalate
    
    CallEscalate --> ProvideTicket

    %% End States
    ProvideDetails --> End([Final Response])
    AskVerify --> End
    ExplainFormat --> End
    ConfirmRefund --> End
    OfferEscalation -- Declined --> End
    ProvideTicket --> End

    %% Styling
    classDef tool fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef decision fill:#fff4dd,stroke:#d4a017,stroke-width:2px;
    classDef success fill:#d4edda,stroke:#28a745,stroke-width:2px;
    classDef failure fill:#f8d7da,stroke:#721c24,stroke-width:1px;

    class CallStatus1,CallStatus2,CallRefund,CallEscalate tool;
    class Intent,StatusResult1,StatusResult2,RefundResult decision;
    class ProvideDetails,ConfirmRefund,ProvideTicket success;
    class AskVerify,ExplainFormat,ExplainPolicy failure;
```

## 3. Communication Guidelines
*   **Empathy First**: Always acknowledge the customer's feelings before tool use.
*   **Recovery Oriented**: When a tool fails (e.g., `not_found`), always provide a specific path forward (re-verify or search by email).
*   **Proactive Escalation**: Always offer a supervisor if a refund is denied due to policy.
