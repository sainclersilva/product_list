# Data reading functions and comparison logic

import json
from pathlib import Path
from typing import List, Optional
from app.models import Product

#file with the list of products
DATA_FILE = Path(__file__).parent / "data/products.json"

def load_products() -> List[Product]:
    #Load all products from the JSON file
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Product(**item) for item in data]
    except FileNotFoundError:
        print("Product file not found.")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return []

def get_product_by_id(product_id: int) -> Optional[Product]:
    #Returns a specific product by ID
    products = load_products()
    for product in products:
        if product.id == product_id:
            return product
    return None