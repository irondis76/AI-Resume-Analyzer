# AI Resume Analyzer

A sophisticated resume analysis system powered by LangGraph and OpenAI GPT-5-nano. This application provides comprehensive resume analysis with actionable recommendations for improvement.

## Features

- **Multi-Stage Analysis**: Advanced LangGraph workflow with parallel processing
- **Comprehensive Evaluation**: Skills analysis, experience assessment, formatting review, and ATS optimization
- **AI-Powered Insights**: GPT-5-nano provides expert-level resume coaching
- **Structured Output**: Both JSON API responses and human-readable markdown reports
- **Multiple Formats**: Supports PDF and DOCX resume uploads
- **RESTful API**: FastAPI backend with CORS support
- **Testing Interface**: Streamlit frontend for easy testing and demonstration

## Architecture

```
├── backend/
│   ├── ai/           # LangGraph workflows and AI logic
│   ├── api/          # FastAPI REST endpoints
│   └── core/         # Core utilities (parsing, models, config)
├── frontend/         # Streamlit testing interface
└── pyproject.toml    # UV dependency management
```

## Quick Start

1. **Setup Environment**
   ```bash
   # Install UV (if not already installed)
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # Clone and setup
   git clone <repository-url>
   cd AI-Resume-Analyzer
   uv sync
   ```

2. **Configure API Keys**
   ```bash
   cp backend/env.example backend/.env
   # Edit backend/.env and add your OPENAI_API_KEY
   ```

3. **Start the API**
   ```bash
   uv run uvicorn backend.api.main:app --reload
   ```

4. **Test with Streamlit (Optional)**
   ```bash
   uv run streamlit run frontend/app.py
   ```

## API Endpoints

- `POST /analyze` - Upload and analyze resume (PDF/DOCX)
- `GET /health` - Health check endpoint

## Analysis Workflow

1. **Initial Assessment** - Parse resume structure and identify career level
2. **Parallel Analysis** - Skills, experience, formatting, and ATS evaluation
3. **Synthesis** - Aggregate findings and prioritize recommendations
4. **Report Generation** - Create structured JSON and markdown output

## Technology Stack

- **LangGraph** - Multi-stage analysis orchestration
- **OpenAI GPT-5-nano** - AI analysis engine
- **FastAPI** - REST API framework
- **Pydantic** - Data validation and serialization
- **PDFplumber** - PDF parsing
- **python-docx** - DOCX parsing
- **Streamlit** - Testing interface
- **UV** - Fast Python package management

## Configuration

Key environment variables (see `backend/env.example`):

- `OPENAI_API_KEY` - Your OpenAI API key
- `MODEL_NAME` - AI model (default: gpt-5-nano)
- `TEMPERATURE` - AI creativity level (default: 0.2)
- `MAX_TOKENS` - Response length limit (default: 1500)
- `UPLOAD_MAX_MB` - File size limit (default: 10MB)

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

For detailed setup instructions, see [SETUP.md](SETUP.md).
