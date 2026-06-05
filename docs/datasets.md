# Dataset Catalog

This catalog outlines the datasets used for training, retrieving, and evaluating our telecom-focused LLM/RAG pipeline.

| Dataset | Purpose | Format | Size / Scale |
| :--- | :--- | :--- | :--- |
| **TeleQnA** | Telecom QA Evaluation & Benchmarking | JSON (`.txt`) | 10,000 questions (5 categories) |
| **3GPP Specifications** | Core Telecom Knowledge Base (RAG) | PDF | [e.g., Release 15/16/17] |
| **O-RAN Documents** | Domain-Specific Architecture (RAG) | PDF | [e.g., 50+ documents] |

---

## Dataset Details

### 1. TeleQnA
* **Purpose:** Evaluation and benchmarking of LLM performance on telecom-specific knowledge.
* **Format:** JSON structure saved within a text file.
* **Structure:** Contains 10,000 multiple-choice and open-ended questions split across 5 distinct categories (e.g., Standards, Research, Protocols).

### 2. 3GPP Specifications
* **Purpose:** Acts as the primary ground-truth knowledge base for the RAG (Retrieval-Augmented Generation) pipeline.
* **Format:** PDF documents.
* **Scope:** Covers core cellular standards (e.g., 5G NR, Core Network specifications).

### 3. O-RAN Documents
* **Purpose:** Provides specialized, domain-specific retrieval data focusing on Open RAN architecture.
* **Format:** PDF documents.
* **Scope:** Includes O-RAN Alliance architecture specifications, interface definitions, and deployment profiles.