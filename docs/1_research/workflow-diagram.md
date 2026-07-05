```mermaid

flowchart TD
    %% --- Horizontal Legend Banner ---
    subgraph Legend ["Diagram Legend"]
        direction LR
        L1[Clinical Flow Step] ~~~ L2{Decision Point} ~~~ L3[Outcome / Disposition] ~~~ L4[(Database)] ~~~ L5["AI Plug-in Node"]
    end

    Legend ~~~ A

    A[Step 1: Patient Arrival<br/>ambulance / walk-in / taxi]
    B[Step 2: Registration<br/>Demographics, consent, arrival mode<br/>Handoff: desk → nursing]
    C[Step 3: Vitals Capture<br/>Temp, HR, RR, BP, SpO2,<br/>glucose, pain score]
    D[Step 4: Triage Nurse Assessment<br/>Chief complaint, allergies,<br/>brief history ~3-5 min]
    E{Decision:<br/>ESI Category Assignment<br/>urgent vs non-urgent}
    F[Step 5a: Acute / Resus<br/>Zone — bed assigned]
    G[Step 5b: Fast-Track /<br/>Waiting Room]
    H{Re-check:<br/>Deterioration?}
    I[Step 6: Physician Assessment<br/>History, exam, orders<br/>Handoff: nursing → ED physician]
    J{Decision:<br/>Disposition}
    K[Admit<br/>boarding — ward bed]
    L[Discharge<br/>counselling, Rx handover]
    M[Transfer<br/>receiving facility]
    DB[(Structured, De-identified<br/>ED Database)]

    %% AI plug-in nodes
    AI1["① AI 1: Structured Digital Intake<br/>Replaces paper form; flags<br/>missing mandatory fields"]
    AI2["② AI 2: Rule-Based Vitals Flag<br/>Checks vitals vs. clinical thresholds;<br/>highlights abnormal values"]
    AI4["④ AI 4: Communication Support<br/>Reformats incomplete notes into<br/>structured patient questions"]
    AI3["③ AI 3: Suggested ESI Level<br/>Rule-based suggestion; nurse<br/>reviews, accepts or overrides"]
    AI5["⑤ AI 5: Data Capture to Database<br/>Logs vitals, ESI, override flag<br/>and outcome for QI and audit"]

    %% Workflow routing
    A --> B --> C --> D --> E
    E -->|ESI 1-3 urgent| F
    E -->|ESI 4-5 non-urgent| G
    G --> H
    H -->|Yes| E
    H -->|No| I
    F --> I
    I --> J
    J -->|Admit| K
    J -->|Discharge| L
    J -->|Transfer| M
    K --> DB
    L --> DB
    M --> DB

    %% AI links
    B -. "AI 1" .-> AI1
    C -. "AI 2" .-> AI2
    D -. "AI 4" .-> AI4
    E -. "AI 3" .-> AI3
    DB -. "AI 5" .-> AI5

    %% Styling configurations
    classDef clinical fill:#D5E8F0,stroke:#2E75B6,stroke-width:1.8px,color:#1a1a2e
    classDef decision fill:#FFF3CD,stroke:#856404,stroke-width:1.8px,color:#1a1a2e,font-weight:bold
    classDef outcome fill:#EAF7EA,stroke:#3A9D4F,stroke-width:1.8px,color:#1a1a2e
    classDef database fill:#F2F2F2,stroke:#888888,stroke-width:1.5px,color:#333333
    classDef ainode fill:#FADBD8,stroke:#E74C3C,stroke-width:1.8px,stroke-dasharray:6 3,color:#922B21,font-weight:600

    class A,B,C,D,F,G,I,L1 clinical
    class E,H,J,L2 decision
    class K,L,M,L3 outcome
    class DB,L4 database
    class AI1,AI2,AI3,AI4,AI5 ainode

    style AI1 fill:#FADBD8,color:#922B21
    style AI2 color:#922B21,fill:#FADBD8
    style AI3 color:#922B21,fill:#FADBD8
    style AI5 color:#922B21,fill:#FADBD8
    style AI4 color:#922B21,fill:#FADBD8
    style L5 fill:#FADBD8,color:#922B21,stroke:#E74C3C,stroke-width:1.8px,stroke-dasharray:6 3
