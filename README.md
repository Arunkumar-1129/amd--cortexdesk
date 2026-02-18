# CortexDesk

A local-first, privacy-focused desktop assistant that helps you manage tasks, notes, meetings, and research - all running 100% offline on your machine.

## Architecture

- **Desktop App**: Electron + React + TypeScript
- **Backend**: Python + FastAPI
- **AI Engine**: Local LLM (Ollama), offline STT (Whisper), RAG with Chroma
- **Storage**: SQLite + SQLCipher (encrypted), Chroma vector DB, encrypted file vault

## Features

- 📁 **Document Ingestion**: PDF, DOCX, XLSX, TXT
- 🎤 **Live Meeting Mode**: Offline speech-to-text and meeting summarization
- 📧 **Email/Chat Import**: Import exported emails (.pst, .mbox) and chats (WhatsApp, Slack)
- 🔍 **Research Copilot**: RAG-powered semantic search over your local documents
- ✅ **Task Management**: AI-extracted tasks with human-in-the-loop confirmation
- 📅 **Intelligent Scheduler**: Local calendar with conflict resolution
- 🧠 **Knowledge Graph**: Structured knowledge from your data
- 🔒 **100% Offline**: No cloud calls, all data stays local

## Setup

### Prerequisites

- Node.js 18+ and npm/yarn
- Python 3.11+
- Ollama installed locally (for LLM)
- SQLCipher libraries

### Installation

1. Install desktop dependencies:
```bash
cd desktop
npm install
```

2. Install backend dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Set up local models (Ollama):
```bash
# Install Ollama from https://ollama.ai
ollama pull llama3:8b  # or your preferred model
```

4. Configure paths in `config/app.yaml`

### Running

1. Start backend:
```bash
cd backend
python -m app.main
```

2. Start desktop app:
```bash
cd desktop
npm run dev
```

## Project Structure

```
cortexdesk/
├─ desktop/          # Electron + React + TS
├─ backend/          # Python + FastAPI
├─ config/           # Configuration files
├─ data/             # Local data (gitignored)
└─ docs/             # Documentation
```

## Security & Privacy

- All data encrypted at rest (SQLCipher + file vault encryption)
- No external network calls (except optional model downloads)
- Offline-by-default
- Permission-based access control

## License

[Your License Here]

