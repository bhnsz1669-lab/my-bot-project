from fastapi import FastAPI
from contextlib import asynccontextmanager
import asyncio
from app.bale_bot import BaleBot
from storage import init_db

bot = BaleBot()

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    print("✅ دیتابیس آماده شد")
    asyncio.create_task(polling_loop())
    yield

app = FastAPI(lifespan=lifespan)

async def polling_loop():
    offset = 0
    while True:
        try:
            data = await bot.get_updates(offset)
            if data.get("ok"):
                for update in data.get("result", []):
                    await bot.handle_update(update)
                    offset = update["update_id"] + 1
        except Exception as e:
            print(f"⚠️ خطا در دریافت آپدیت: {e}")
        await asyncio.sleep(2)
@app.get("/")
def root():
    return {"status": "✅ ربات بله فعال است", "version": "1.0.0"}
