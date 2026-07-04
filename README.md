# Autonomous AI Research Agent

## Overview

The Autonomous AI Research Agent is a application that autonomously researches user queries by planning tasks, retrieving information from multiple sources, summarizing results, and exporting reports in Markdown and PDF formats.

## Features

- Autonomous research planning
- Multi-source information retrieval
- Parallel search execution
- Duplicate removal
- Relevance ranking
- Markdown report export
- PDF report generation

## Technologies Used

- Python 3.x
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
py -m uvicorn app:app --reload
```

5. Open your browser at

```
http://127.0.0.1:8000
```

## Output

The application generates:

- Markdown research reports
- PDF research reports


