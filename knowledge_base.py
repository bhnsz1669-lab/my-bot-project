import json
from pathlib import Path
from rapidfuzz import fuzz, process

class KnowledgeBase:
    def __init__(self, path: str = "knowledge.json"):
        self.path = Path(path)
        self.data = self._load()

    def _load(self) -> dict:
        if not self.path.exists():
            return {"faq": []}
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)

    def search(self, query: str, threshold: int = 70) -> str | None:
        faqs = self.data.get("faq", [])
        if not faqs:
            return None
        questions = [item["question"] for item in faqs]
        match = process.extractOne(query, questions, scorer=fuzz.ratio, score_cutoff=threshold)
        if match:
            _, score, idx = match
            return faqs[idx]["answer"]
        return None