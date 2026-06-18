import httpx
from app.config import BALE_API_URL
from storage import save_message
from app.ai_handler import AIHandler

class BaleBot:
    def __init__(self):
        self.api = BALE_API_URL
        self.ai = AIHandler()

    async def send_message(self, chat_id: int, text: str):
        async with httpx.AsyncClient() as client:
            await client.post(f"{self.api}/sendMessage", json={
                "chat_id": chat_id,
                "text": text,
                "parse_mode": "HTML"
            })

    async def handle_update(self, update: dict):
        if "message" not in update or "text" not in update["message"]:
            return
        chat_id = update["message"]["chat"]["id"]
        user_id = str(chat_id)
        text = update["message"]["text"].strip()
        save_message(user_id, "user", text)
        reply = await self.ai.process(user_id, text)
        save_message(user_id, "assistant", reply)
        await self.send_message(chat_id, reply)

    async def get_updates(self, offset: int = 0):
        async with httpx.AsyncClient() as client:
            res = await client.get(f"{self.api}/getUpdates", params={"offset": offset, "timeout": 30})
            return res.json()
