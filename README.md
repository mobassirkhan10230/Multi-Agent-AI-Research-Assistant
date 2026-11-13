# Multi-Agent AI Research Assistant

An AI-powered research assistant that uses multiple specialized AI agents to collect, analyze, verify, and summarize information from web sources and local PDF documents.

## Project Overview

The Multi-Agent AI Research Assistant is designed to simplify complex research tasks through collaboration between specialized AI agents.

The system combines Retrieval-Augmented Generation (RAG), web search, local document retrieval, and LLM-based reasoning to generate structured research summaries and PDF reports.

## Architecture

The project uses five specialized agents:

1. **Research Agent** – Retrieves relevant information from local PDF documents and web sources.
2. **Analysis Agent** – Analyzes research findings, identifies important themes, and highlights relationships.
3. **Verification Agent** – Evaluates claims and identifies unsupported or conflicting information.
4. **Summarization Agent** – Produces a structured summary from the research and verification results.
5. **Report Agent** – Generates a downloadable PDF research report.

LangGraph orchestrates the workflow and manages communication between agents.

## Technology Stack

- **Programming Language:** Python
- **LLM:** OpenAI GPT-4.1-mini
- **Agent Orchestration:** LangGraph
- **LLM Integration:** LangChain
- **Web Search:** Tavily
- **Document Processing:** PyMuPDF
- **Text Chunking:** LangChain Text Splitters
- **Embeddings:** Sentence Transformers (`all-MiniLM-L6-v2`)
- **Vector Database:** ChromaDB
- **Frontend:** Streamlit
- **PDF Generation:** ReportLab
- **Environment Management:** uv

## Key Features

- Multi-agent research workflow
- Web information retrieval using Tavily
- Local PDF document processing
- Retrieval-Augmented Generation (RAG)
- Semantic search using ChromaDB
- Research analysis and claim verification
- Structured research summaries
- PDF report generation
- Interactive Streamlit interface

## Project Structure

```text
multi_agent_research_assistant/
│
├── src/
│   ├── app.py
│   ├── graph.py
│   ├── state.py
│   ├── llm.py
│   ├── tools.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── research_agent.py
│   ├── analysis_agent.py
│   ├── verification_agent.py
│   ├── summarization_agent.py
│   └── report_agent.py
│
├── reports/
├── chroma_db/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/multi_agent_research_assistant.git
cd multi_agent_research_assistant
```

### 2. Create a virtual environment

```bash
uv venv --python 3.13
```

Activate it on Windows:

```cmd
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
uv pip install -r requirements.txt
```

### 4. Configure API keys

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Never commit your `.env` file to GitHub.

### 5. Run the application

```bash
uv run streamlit run src/app.py
```

Open the local URL displayed in your terminal.

## Development Status

This project is being developed incrementally. The initial agent workflow and Streamlit interface are being integrated and tested. Conditional verification feedback, additional reliability improvements, and further testing are planned.

## Future Improvements

- Implement verification-driven research feedback loops.
- Improve source attribution and citation tracking.
- Add structured agent outputs.
- Improve error handling and retry mechanisms.
- Add research history and session management.
- Deploy the application.

## Learning Objectives

This project explores practical applications of:

- Multi-agent AI systems
- Retrieval-Augmented Generation
- LLM tool integration
- Vector databases and semantic search
- Agent orchestration with LangGraph
- AI application development with Streamlit

## Author

Developed as a hands-on project to explore multi-agent AI systems and intelligent research automation.