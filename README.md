# 🤖 Bale AI Bot

ربات هوشمند فارسی برای پیام‌رسان بله با استفاده از FastAPI و OpenAI
## 🚀 نصب و راه‌اندازی

### 1. نصب وابستگی‌ها
```bash
pip install -r requirements.txt
```

### 2. تنظیم متغیرهای محیطی
فایل `.env.example` رو به `.env` تغییر نام بده و مقادیر رو پر کن:
```bash
cp .env.example .env
```

مقادیر زیر رو وارد کن:
- `BALE_TOKEN`: توکن ربات بله (از @botfather_bl در بله بگیر)
- `OPENAI_API_KEY`: کلید API اوپن‌ای‌آی

### 3. اجرای ربات
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 📱 دریافت توکن بله

1. در بله به @botfather_bl پیام بده
2. دستور `/newbot` رو بزن
3. نام ربات رو وارد کن
4. توکن رو کپی کن و در `.env` بذار

## ✨ ویژگی‌ها

- ✅ پاسخ خودکار با OpenAI
- ✅ جستجو در دانش پایه (FAQ)
- ✅ ذخیره تاریخچه چت هر کاربر
- ✅ پشتیبانی کامل از زبان فارسی
- ✅ کار در PV (پیام خصوصی)

## 📂 ساختار پروژه

```
bale-ai-bot/
├── app/
│   ├── __init__.py
│   ├── config.py          # تنظیمات
│   ├── main.py            # نقطه شروع
│   ├── bale_bot.py        # اتصال به بله
│   ├── ai_handler.py      # پردازش AI
│   └── knowledge_base.py  # جستجو در FAQ
├── storage.py             # مدیریت دیتابیس├── knowledge.json         # دانش پایه
├── requirements.txt
├── .env                   # متغیرهای محیطی
└── README.md
```

## 📝 لایسنس

MIT
