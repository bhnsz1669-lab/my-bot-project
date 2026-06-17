import json
from pathlib import Path
from rapidfuzz import fuzz
from app.config import KNOWLEDGE_PATH, SIMILARITY_THRESHOLD

def load_knowledge():
    path = Path(KNOWLEDGE_PATH)
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"faq": []}, f, ensure_ascii=False, indent=2)

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def find_best_answer(user_text: str):
    data = load_knowledge()
    faqs = data.get("faq", [])

    best_score = 0
    best_answer = None

    for item in faqs:
        q = item.get("question", "")
        a = item.get("answer", "")
        score = fuzz.partial_ratio(user_text.lower(), q.lower())
        if score > best_score:
            best_score = score
            best_answer = a

    if best_score >= SIMILARITY_THRESHOLD:
        return best_answer

    return None