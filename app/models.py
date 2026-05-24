from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class Category(str, Enum):
    chatbot = "chatbot"
    coding = "coding"
    design = "design"
    video = "video"


class Pricing(str, Enum):
    free = "free"
    freemium = "freemium"
    paid = "paid"


class Tool(BaseModel):
    id: int
    name: str
    category: Category
    pricing: Pricing
    rating: float
    users: int
    created_at: datetime