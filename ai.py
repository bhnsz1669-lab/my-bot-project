from openai import OpenAI
from app.config import OPENAI_API_KEY, AI_MODEL, BOT_NAME, BOT_TONE, MAX_HISTORY_MESSAGES

client = OpenAI(api_key=OPENAI_API_KEY)

def build_system_prompt():
    return f"""
تو یک ربات پاسخ‌گوی فارسی هستی.

قوانین:
- نام تو: {BOT_NAME}
- لحن پاسخ: {BOT_TONE}
- پاسخ‌ها کوتاه، واضح و محترمانه باشند.
- اگر پاسخ دقیق از دانش موجود نداشتی، یک پاسخ امن و محترمانه بده.
- اگر کاربر سوال مبهم یا پیچیده پرسید، درخواست توضیح بیشتر کن.
- اگر اطلاعات کافی نداری، نگو حدس می‌زنم؛ بگو برای بررسی بیشتر ارسال شد.
""".strip()

def generate_ai_reply(user_text: str, knowledge_answer: str | None, history: list[dict]):
    messages = [{"role": "system", "content": build_system_prompt()}]

    if history:
        for item in history[-MAX_HISTORY_MESSAGES:]:
            role = item["role"]
            content = item["content"]
            if role not in ("user", "assistant"):
                continue
            messages.append({"role": role, "content": content})

    user_message = f"""
متن کاربر:
{user_text}

پاسخ موجود از دانش:
{knowledge_answer if knowledge_answer else "ندارد"}
""".strip()

    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model=AI_MODEL,
        messages=messages,
        temperature=0.6
    )

    return response.choices[0].message.content.strip()