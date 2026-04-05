# GroceryBot — AI Customer Support Assistant

An AI-powered chatbot that answers grocery and produce questions using RAG (Retrieval Augmented Generation).

## Team: [Your Team Name]
| Name | Role | GitHub |
|------|------|--------|
| | Team Lead | |
| | Backend/API | |
| | Frontend/Chat UI | |
| | Knowledge Base/RAG | |
| | Integration/Testing | |

## What This Does
Ask GroceryBot anything about produce:
- "How long does avocado last in the fridge?"
- "Is this mold on my strawberry dangerous?"
- "What can I make with wilting spinach and tomatoes?"
- "How should I store bananas?"

Powered by RAG over a curated produce knowledge base + LLM.

## Tech Stack
- **Backend:** Python + FastAPI
- **Frontend:** HTML/CSS/JavaScript (chat interface)
- **LLM:** Claude API or OpenAI API
- **Vector Store:** ChromaDB (local, no server needed)
- **AI Tools:** GitHub Copilot, Cursor

## Quick Start
```bash
git clone https://github.com/LawrenceHua/es-intern-grocerybot.git
cd es-intern-grocerybot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Set your API key
cp .env.example .env
# Edit .env and add your API key

python3 app.py
# Open http://localhost:8000
```

## Project Structure
```
es-intern-grocerybot/
├── app.py                  # FastAPI server + chat endpoint
├── rag/
│   ├── knowledge_base.py   # Load and index produce knowledge
│   ├── retriever.py        # Vector search for relevant info
│   └── generator.py        # LLM response generation
├── knowledge/
│   ├── produce_guide.json  # Produce storage & freshness data
│   └── faq.json            # Common grocery questions
├── static/
│   ├── index.html          # Chat interface
│   ├── style.css
│   └── script.js
├── tests/
│   └── test_rag.py
├── requirements.txt
└── README.md
```
