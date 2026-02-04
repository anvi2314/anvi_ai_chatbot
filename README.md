# Ollama Chat — Flask AI Chatbot

A simple Flask-based chat UI that proxies messages to an Ollama model.

Requirements
- Python 3.8+
- Ollama running locally or reachable at an HTTP URL

Setup

1. (Optional) create a virtualenv and activate it

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure environment variables (optional):

- `OLLAMA_URL` — default: `http://localhost:11434`
- `MODEL` — default: `llama2`

Example (Windows CMD):

```cmd
set OLLAMA_URL=http://localhost:11434
set MODEL=llama2
python app.py
```

Or PowerShell:

```powershell
$env:OLLAMA_URL = 'http://localhost:11434'
$env:MODEL = 'llama2'
python app.py
```

Open http://localhost:5000 in your browser. Type a message and the app will forward it to the Ollama API and display the reply.

Notes
- The app uses the Ollama `/chat` endpoint. If your Ollama installation exposes a different API, update `app.py` accordingly.
- This repo is a minimal starting point. You can extend with streaming, authentication, session history, or persistence.
