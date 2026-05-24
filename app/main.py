from fastapi import FastAPI
from typing import Optional

from .reports import get_tools
from .models import Category, Pricing

app = FastAPI(
    title="SmartTools API",
    description="API for discovering AI tools",
    version="1.0.0"
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/tools")
def tools(
    category: Optional[Category] = None,
    pricing: Optional[Pricing] = None,
    sort: str = "rating",
    descending: bool = True,
    offset: int = 0,
    limit: int = 20
):
    return get_tools(
        category=category,
        pricing=pricing,
        sort=sort,
        descending=descending,
        offset=offset,
        limit=limit
    )