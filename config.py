import os
from pathlib import Path
from dotenv import load_dotenv

# بارگذاری متغیرهای محیطی از فایل .env
load_dotenv()

BALE_TOKEN = os.getenv("BALE_TOKEN", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
DATABASE_PATH = os.getenv("DATABASE_PATH", "data/bot.db")

BALE_API_URL = f"https://tapi.bale.ai/bot{BALE_TOKEN}"

MAX_HISTORY = int(os.getenv("MAX_HISTORY", "10"))
SYSTEM_PROMPT = os.getenv(
    "SYSTEM_PROMPT",
    "تو یک دستیار هوشمند و مهربان فارسی‌زبان هستی. به سوالات کاربران دقیق، کوتاه و محترمانه پاسخ بده."
)
