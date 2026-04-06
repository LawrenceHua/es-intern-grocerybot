# GroceryBot — Conversational Produce AI

RAG-powered chatbot using a 100+ item produce knowledge base with nutrition, storage, recipes, and diet compatibility data.

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
- "I have chicken, rice, broccoli — what can I make?"
- "Is this keto-friendly?"
- "Compare kale vs spinach nutrition"
- Upload a photo → identify produce + get storage advice

## Baseline Code (from production platform)
- `produce_enrichment.json` — **100+ produce items** with storage methods, nutrition per 100g, diet compatibility, ripeness indicators, recipe suggestions
- `nutrition_database.py` — USDA nutrition data integration
- `diet_compatibility.py` — Checks against 8+ dietary restrictions (vegan, keto, paleo, gluten-free, nut-free, etc.)

## Architecture
```
User Question → ChromaDB Vector Search → Top 3 Results → Claude API → Response
                     ↑                                        ↑
              100+ item produce                      Conversation history
              knowledge base                         + dietary preferences
```

## Tech Stack
- **Backend:** Python + FastAPI
- **LLM:** Claude API (Anthropic)
- **Vector Store:** ChromaDB (local, no server needed)
- **Frontend:** HTML/CSS/JavaScript (chat interface)
- **AI Tools:** GitHub Copilot, Cursor

## What You Build (Weeks 5-10)
1. RAG chatbot over 100+ item knowledge base
2. Food safety advisor (mold, temperature, cross-contamination)
3. Recipe generator from inventory items
4. Diet compatibility checker (8+ dietary restrictions)
5. Storage optimizer (prioritize what to eat first)
6. Expiration alert system (proactive warnings)
7. Produce comparison (side-by-side nutrition charts)
8. Conversation memory (remember preferences across sessions)
9. Photo identification via FreshEye API integration

## Quick Start
```bash
git clone https://github.com/LawrenceHua/es-intern-grocerybot.git
cd es-intern-grocerybot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Add your API key
python3 app.py
# Open http://localhost:8000
```
