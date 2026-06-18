from openai import OpenAI
from app.config import OPENAI_API_KEY, SYSTEM_PROMPT, MAX_HISTORY
from storage import get_history
from app.knowledge_base import KnowledgeBase

class AIHandler:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.kb = KnowledgeBase()
    async def process(self, user_id: str, message: str) -> str:
        # 1. جستجو در دانش پایه
        kb_answer = self.kb.search(message)
        if kb_answer:
            return kb_answer

        # 2. استفاده از OpenAI
        try:
            history = get_history(user_id, limit=MAX_HISTORY)
            messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history
            messages.append({"role": "user", "content": message})

            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=300,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"❌ OpenAI Error: {e}")
            return "متأسفانه الان نمی‌تونم پاسخ بدم. لطفاً چند دقیقه بعد دوباره امتحان کن."
