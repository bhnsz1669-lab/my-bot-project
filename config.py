import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
BOT_NAME = os.getenv("BOT_NAME", "ربات")
BOT_TONE = os.getenv("BOT_TONE", "friendly")
AI_MODEL = os.getenv("AI_MODEL", "gpt-4o-mini")
KNOWLEDGE_PATH = os.getenv("KNOWLEDGE_PATH", "data/knowledge.json")
DATABASE_PATH = os.getenv("DATABASE_PATH", "data/conversations.db")
MAX_HISTORY_MESSAGES = int(os.getenv("MAX_HISTORY_MESSAGES", "10"))
SIMILARITY_THRESHOLD = int(os.getenv("SIMILARITY_THRESHOLD", "75"))