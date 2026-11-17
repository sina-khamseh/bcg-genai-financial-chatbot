# BCG GenAI Job Simulation - Financial Analysis Chatbot

## Project Overview
This repository contains the prototype for an AI-powered financial analysis chatbot developed as part of the **BCG GenAI Job Simulation** on Forage. The project extracts key financial indicators from SEC 10-K filings for **Microsoft, Apple, and Tesla** (FY 2024–2026), computes Year-over-Year (YoY) growth trends using `pandas`, and provides an interactive command-line query engine.

## How the Chatbot Works
1. **Data Processing (`Task1_Financial_Analysis.ipynb`):** Reads raw 10-K financial figures (`financial_data.csv`), calculates YoY percentage changes across 5 core metrics, and exports `processed_financial_data.csv`.
2. **Query Engine (`financial_chatbot.py`):** Loads the processed dataset and uses rule-based condition matching to return instant, accurate financial metrics and YoY growth directions based on `<Company> <Year> <Metric>` queries.

## Supported Predefined Queries
Users can query any combination of:
- **Companies:** `Microsoft`, `Apple`, `Tesla`
- **Fiscal Years:** `2024`, `2025`, `2026`
- **Metrics:** `Total_Revenue`, `Net_Income`, `Total_Assets`, `Total_Liabilities`, `Cash_Flow_Operating`

*Example Query:* `Microsoft 2025 Total_Revenue`

## Current Limitations & Future Architecture (RAG Upgrade)
- **Rule-Based Matching:** The current prototype relies on structured keyword inputs (`<Company> <Year> <Metric>`) and cannot parse free-form natural language questions.
- **Static Dataset:** Limited to pre-extracted CSV metrics rather than full 10-K text documents.
- **Next Step (Production Architecture):** Upgrade to a Retrieval-Augmented Generation (**RAG**) pipeline using **LangChain**, **ChromaDB** (vector database for 10-K PDF embeddings), and an **LLM API** exposed via a **FastAPI** backend.