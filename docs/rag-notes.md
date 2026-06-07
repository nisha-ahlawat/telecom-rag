What is RAG?

Normal AI-->

Question
   ↓
LLM
   ↓
Answer

RAG-->

Question
   ↓
Search documents
   ↓
Find relevant information
   ↓
Give information to AI
   ↓
Answer


What is Chunking?
example think-

Big Book
    ↓
Small Sections

Those small sections are called:Chunks



What is an Embedding?
An embedding is simply
Text
   ↓
Numbers
while preserving the meaning



What is a Vector Database?
Stores embeddings

let say you have 500 chunks
each chunks has an embeddings



## How everything Works
Suppose user asks-              Why is throughput dropping?

Step 1
Question:    Why is throughput dropping?

Step 2      Convert question into embedding.

Question
    ↓
Embedding

Step 3       Search vector database.

Find:
Chunk 17
Chunk 45
Chunk 102

Most relevant.

Step 4       Send those chunks to AI.

Step 5       AI answers.



## FINAL PIPELINE

PDF
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector Database
 ↓
User Question
 ↓
Embedding
 ↓
Search
 ↓
Relevant Chunks
 ↓
LLM
 ↓
Answer

hence
## RAG
= Search documents first, answer second

## Chunking
means splitting large documents into smaller pieces.
= Split big documents into small pieces
Example:
500-page PDF
↓
300 chunks

This helps retrieval become faster and more accurate.



## Embedding
An embedding is a numerical representation of text.
= Convert text into numbers that preserve meaning

Example:
"packet loss"
↓
[0.2, 0.5, -0.1 ...]
Embeddings allow semantic search.


Vector Database
stores embeddings and allows efficient similarity search.
= Database that stores embeddings and helps find similar information

