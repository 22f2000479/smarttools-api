from datetime import datetime, timedelta
from .models import Tool, Category, Pricing

DATA = []

tool_names = [
    "ChatGPT",
    "Claude",
    "Cursor",
    "Midjourney",
    "Runway",
    "Notion AI",
    "Perplexity",
    "Copilot",
]

categories = [
    Category.chatbot,
    Category.coding,
    Category.design,
    Category.video,
]

pricing_types = [
    Pricing.free,
    Pricing.freemium,
    Pricing.paid,
]

for i in range(1, 121):
    tool = Tool(
        id=i,
        name=tool_names[i % len(tool_names)],
        category=categories[i % len(categories)],
        pricing=pricing_types[i % len(pricing_types)],
        rating=round(3.5 + (i % 15) * 0.1, 1),
        users=1000 + i * 500,
        created_at=datetime.now() - timedelta(days=i)
    )

    DATA.append(tool)