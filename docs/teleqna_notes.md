# TeleQnA Dataset Exploration

## Overview

TeleQnA is a telecom benchmark dataset containing 10,000 multiple-choice questions designed to evaluate telecommunications knowledge in Large Language Models (LLMs).

TeleQnA serves as our benchmark and evaluation dataset. We use it to test whether our RAG system can correctly answer telecom questions using knowledge retrieved from 3GPP and O-RAN documents.

## Categories

* Lexicon (500 questions)
* Research Overview (2,000 questions)
* Research Publications (4,500 questions)
* Standards Overview (1,000 questions)
* Standards Specifications (2,000 questions)

## Dataset Format

The dataset is stored as a JSON object inside `TeleQnA.txt`.

Each question contains:

* question
* option 1
* option 2
* option 3
* option 4
* answer
* explanation
* category

## Example Structure

{
"question 0": {
"question": "...",
"option 1": "...",
"option 2": "...",
"option 3": "...",
"option 4": "...",
"answer": "...",
"explanation": "...",
"category": "Standards specifications"
}
}

## Why We Are Using TeleQnA

* Evaluate TelecomCopilot performance
* Measure question-answering accuracy
* Benchmark retrieval quality
* Test telecom knowledge understanding

## Most Relevant Categories

1. Standards Specifications
2. Standards Overview
3. Lexicon

These categories align most closely with TelecomCopilot's goal of answering 3GPP and O-RAN related questions.
