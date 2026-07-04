# Autonomous AI Research Agent

## Overview

The Autonomous AI Research Agent is a FastAPI-based application that autonomously researches user queries by planning tasks, retrieving information from multiple sources, summarizing results using an LLM, and exporting reports in Markdown and PDF formats.

## Features

- Autonomous research planning
- Multi-source information retrieval
- Parallel search execution
- Duplicate removal
- Relevance ranking
- LLM-based summarization
- Markdown report export
- PDF report generation
- Memory support
- FastAPI REST API

## Technologies Used

- Python 3.x
- FastAPI
- Uvicorn
- DuckDuckGo Search
- Wikipedia API
- Arxiv API
- RSS Feed Parser

## Project Structure

```
agents/
models/
tools/
static/
exports/
logs/
app.py
requirements.txt
```

## Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project

```bash
cd autonomous-ai-agent
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
uvicorn app:app --reload
```

5. Open your browser at

```
http://127.0.0.1:8000
```

## Output

The application generates:

- Markdown research reports
- PDF research reports


