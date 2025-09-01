# Data models
from typing import Dict
from pydantic import BaseModel, HttpUrl

class Product(BaseModel):
    id: int
    name: str
    image_url: HttpUrl
    description: str
    price: float
    rating: float
    specs: Dict[str, str]
