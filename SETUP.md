# Setup Guide - AI Resume Analyzer

This guide provides detailed setup instructions for Windows, Linux, and macOS.

## Prerequisites

- Python 3.10 or higher
- OpenAI API key
- Git

## Platform-Specific Installation

### Windows

#### Option 1: Using PowerShell (Recommended)

1. **Install UV Package Manager**
   ```powershell
   # Using PowerShell
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # Restart your terminal or run:
   $env:PATH += ";$env:USERPROFILE\.cargo\bin"
   ```

2. **Install Python (if not already installed)**
   ```powershell
   # Using winget
   winget install Python.Python.3.11
   
   # Or download from python.org
   ```

3. **Clone and Setup Project**
   ```powershell
   git clone <repository-url>
   cd AI-Resume-Analyzer
   uv sync
   ```

#### Option 2: Using Command Prompt

1. **Install UV**
   ```cmd
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. **Setup Project**
   ```cmd
   git clone <repository-url>
   cd AI-Resume-Analyzer
   uv sync
   ```

### Linux (Ubuntu/Debian)

1. **Install UV**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   source $HOME/.cargo/env
   ```

2. **Install Python (if needed)**
   ```bash
   sudo apt update
   sudo apt install python3.11 python3.11-venv python3-pip
   ```

3. **Setup Project**
   ```bash
   git clone <repository-url>
   cd AI-Resume-Analyzer
   uv sync
   ```

### Linux (CentOS/RHEL/Fedora)

1. **Install UV**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   source $HOME/.cargo/env
   ```

2. **Install Python (if needed)**
   ```bash
   # For Fedora
   sudo dnf install python3.11 python3.11-pip
   
   # For CentOS/RHEL
   sudo yum install python3.11 python3.11-pip
   ```

3. **Setup Project**
   ```bash
   git clone <repository-url>
   cd AI-Resume-Analyzer
   uv sync
   ```

### macOS

1. **Install UV**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   source $HOME/.cargo/env
   ```

2. **Install Python (if needed)**
   ```bash
   # Using Homebrew (recommended)
   brew install python@3.11
   
   # Or using pyenv
   brew install pyenv
   pyenv install 3.11.0
   pyenv global 3.11.0
   ```

3. **Setup Project**
   ```bash
   git clone <repository-url>
   cd AI-Resume-Analyzer
   uv sync
   ```

## Configuration

### 1. Environment Setup

Copy the environment template and configure your API key:

```bash
cp backend/env.example backend/.env
```

Edit `backend/.env` and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
MODEL_NAME=gpt-5-nano
TEMPERATURE=0.2
MAX_TOKENS=1500
UPLOAD_MAX_MB=10
ALLOWED_ORIGINS=*
```

### 2. Get OpenAI API Key

1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key and paste it in your `.env` file

## Running the Application

### Start the API Server

```bash
# From project root
uv run uvicorn backend.api.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### Test the API

```bash
# Health check
curl http://localhost:8000/health

# Analyze a resume
curl -X POST -F "file=@/path/to/your/resume.pdf" http://localhost:8000/analyze
```

### Start the Streamlit Interface (Optional)

```bash
# In a new terminal
uv run streamlit run frontend/app.py
```

The Streamlit interface will be available at `http://localhost:8501`

## Troubleshooting

### Common Issues

#### 1. UV Not Found
```bash
# Add UV to PATH
export PATH="$HOME/.cargo/bin:$PATH"

# Or restart your terminal
```

#### 2. Python Version Issues
```bash
# Check Python version
python --version

# If not 3.10+, install correct version
uv python install 3.11
```

#### 3. OpenAI API Key Issues
- Ensure your API key is valid and has sufficient credits
- Check that the key is correctly set in `backend/.env`
- Verify the key has access to GPT-5-nano model

#### 4. Port Already in Use
```bash
# Kill process on port 8000
# Linux/macOS
lsof -ti:8000 | xargs kill -9

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

#### 5. File Upload Issues
- Ensure file is PDF or DOCX format
- Check file size is under 10MB (configurable in `.env`)
- Verify file is not corrupted

### Platform-Specific Issues

#### Windows
- If PowerShell execution is blocked, run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- Use Windows Subsystem for Linux (WSL) if you encounter compatibility issues

#### Linux
- If you get permission errors, ensure your user is in the `dialout` group: `sudo usermod -a -G dialout $USER`
- For older distributions, you may need to install `python3-dev` and `build-essential`

#### macOS
- If you get SSL errors, update certificates: `brew install ca-certificates`
- For M1/M2 Macs, ensure you're using the correct architecture

## Development Setup

### Install Development Dependencies

```bash
# Add development tools
uv add --dev pytest black isort mypy
```

### Run Tests

```bash
uv run pytest
```

### Code Formatting

```bash
uv run black .
uv run isort .
```

### Type Checking

```bash
uv run mypy backend/
```

## Production Deployment

### Using Docker

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .
RUN pip install uv
RUN uv sync --frozen

EXPOSE 8000
CMD ["uv", "run", "uvicorn", "backend.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Environment Variables for Production

```env
OPENAI_API_KEY=your_production_key
MODEL_NAME=gpt-5-nano
TEMPERATURE=0.1
MAX_TOKENS=2000
UPLOAD_MAX_MB=20
ALLOWED_ORIGINS=https://yourdomain.com
```

## Support

If you encounter issues:

1. Check this troubleshooting guide
2. Review the logs for error messages
3. Ensure all dependencies are correctly installed
4. Verify your OpenAI API key and credits
5. Check the [Issues](https://github.com/your-repo/issues) page

## Next Steps

- Explore the API documentation at `http://localhost:8000/docs`
- Test with different resume formats
- Customize the analysis prompts in `backend/ai/prompts.py`
- Extend the workflow in `backend/ai/workflow.py`
