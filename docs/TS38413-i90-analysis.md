# Analysis – TS 38.413 (NGAP)

## Purpose

TS 38.413 specifies the NG Application Protocol (NGAP), which defines the signaling procedures exchanged between the gNB and the AMF over the NG-C interface in a 5G Core network.

NGAP enables:

- UE registration and mobility management.
- PDU session establishment and release.
- Context management between RAN and Core.
- Paging procedures.
- Handover signaling.
- Error handling and status reporting.

---

## Network Position

```text
+------+      NG-C (NGAP)      +------+
| gNB  | <-------------------> | AMF  |
+------+                       +------+
```

NGAP operates on:

- Application Layer: NGAP
- Transport Layer: SCTP
- Network Layer: IP

---

## Key Functional Areas

### UE Context Management

Responsible for creating, modifying, and releasing UE context information between the gNB and AMF.

Examples:

- Initial Context Setup
- UE Context Release
- UE Context Modification

### Mobility Management

Supports mobility-related procedures including:

- Handover Preparation
- Handover Resource Allocation
- Path Switch

### PDU Session Management Support

Provides signaling required for:

- PDU Session Setup
- PDU Session Modification
- PDU Session Release

### Paging

Allows the AMF to request UE paging through the serving gNB.

### NAS Transport

Transfers NAS messages transparently between:

- UE ↔ AMF

through the gNB.

---

## Important Procedures

### Initial UE Message

Used by the gNB to forward the UE's first NAS message to the AMF.

### Initial Context Setup

Used by the AMF to establish UE context in the gNB after successful registration.

### UE Context Release

Removes UE-specific resources when the UE disconnects or moves.

### PDU Session Resource Setup

Establishes user-plane resources associated with a PDU session.

### Handover Preparation

Coordinates UE mobility between source and target nodes.

---

## Protocol Structure

NGAP messages consist of:

- Procedure Code
- Criticality
- Information Elements (IEs)

Message categories:

1. Initiating Message
2. Successful Outcome
3. Unsuccessful Outcome

---

## Information Elements (IEs)

Information Elements carry procedure-specific data such as:

- AMF UE NGAP ID
- RAN UE NGAP ID
- TAI
- GUAMI
- PDU Session ID
- QoS Flow Information
- Security Parameters

---

## Relationship with Other Specifications

| Specification | Purpose |
|--------------|----------|
| TS 38.300 | Overall NG-RAN architecture |
| TS 38.331 | RRC procedures between UE and gNB |
| TS 38.413 | NGAP procedures between gNB and AMF |
| TS 23.502 | End-to-end 5G procedures |
| TS 29.518 | AMF service interfaces |

---

## Implementation Relevance

NGAP is a critical protocol for:

- 5G Core integration.
- Registration procedures.
- Session management.
- Mobility handling.
- Paging and reachability.
- Interoperability between gNB vendors and Core Network vendors.

Understanding NGAP is essential for troubleshooting signaling flows between the NG-RAN and the 5G Core.