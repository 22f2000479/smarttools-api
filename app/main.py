from fastapi import FastAPI
from datetime import datetime, timedelta

app = FastAPI()

DATA = []

categories = [
    "chatbot",
    "coding",
    "design",
    "video"
]

pricing_types = [
    "free",
    "freemium",
    "paid"
]

tool_names = [
    "ChatGPT",
    "Claude",
    "Cursor",
    "Midjourney",
    "Runway",
    "Notion AI",
    "Perplexity",
    "Copilot"
]

for i in range(1, 121):
    DATA.append({
        "id": i,
        "name": tool_names[i % len(tool_names)],
        "category": categories[i % len(categories)],
        "pricing": pricing_types[i % len(pricing_types)],
        "rating": round(3.5 + (i % 15) * 0.1, 1),
        "users": 1000 + i * 500,
        "created_at": (
            datetime.now() - timedelta(days=i)
        ).isoformat()
    })


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/tools")
def tools(
    category: str = None,
    pricing: str = None,
    sort: str = "rating",
    descending: bool = True,
    offset: int = 0,
    limit: int = 20
):
    results = DATA

    if category:
        results = [
            t for t in results
            if t["category"] == category
        ]

    if pricing:
        results = [
            t for t in results
            if t["pricing"] == pricing
        ]

    results.sort(
        key=lambda t: t[sort],
        reverse=descending
    )

    return results[offset: offset + limit]