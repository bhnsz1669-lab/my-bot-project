from pydantic import BaseModel

class MessageIn(BaseModel):
    user_id: str
    text: str

class WebhookResult(BaseModel):
    user_id: str
    reply: str