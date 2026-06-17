from fastapi import FastAPI
from app.schemas import MessageIn, WebhookResult
from app.storage import init_db, save_message, get_history
from app.knowledge import find_best_answer
from app.ai import generate_ai_reply

app = FastAPI(title="Bale AI Bot")

@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/")
def home():
    return {"status": "running", "message": "Bale AI Bot is up"}

@app.post("/webhook", response_model=WebhookResult)
def webhook(msg: MessageIn):
    user_text = msg.text.strip()

    save_message(msg.user_id, "user", user_text)

    knowledge_answer = find_best_answer(user_text)
    history = get_history(msg.user_id, limit=10)

    reply = generate_ai_reply(
        user_text=user_text,
        knowledge_answer=knowledge_answer,
        history=history
    )

    save_message(msg.user_id, "assistant", reply)

    return WebhookResult(
        user_id=msg.user_id,
        reply=reply
    )