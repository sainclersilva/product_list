# API Main File
from fastapi import FastAPI, HTTPException, Path, Security, Depends, status, Query
from typing import List
from app.models import Product
from app.crud import load_products, get_product_by_id
from dotenv import load_dotenv
from fastapi.security.api_key import APIKeyHeader
import os

load_dotenv()  # load .env
API_KEY = os.getenv("API_KEY")
API_KEY_NAME = "x-api-key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

# Checks if the key sent in the 'x-api-key' header is valid
def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == API_KEY:
        return api_key_header
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid Key"
    )

app = FastAPI(
    title="Product Comparator API",
    description="""
    RESTful API for comparing products using locally stored JSON data.
    Provides endpoints to list all products or search for specific products by ID.
    Includes basic error handling and interactive Swagger documentation.
    """,
    version="1.0.0",
    contact={
        "name": "Saincler Silva",
        "email": "dmistersan@gmail.com",
        "url": "https://github.com/sainclersilva/"
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    }
)

# Route to list products with pagination
@app.get(
    "/products",
    response_model=List[Product],
    dependencies=[Depends(get_api_key)],
    summary="All products",
    description="Return complete products list to compare."
)
def read_products(
        limit: int = Query(5, ge=1, le=5),
        offset: int = Query(0, ge=0)):
    products = load_products()
    if not products:
        raise HTTPException(status_code=404, detail="No products found.")
    return products[offset: offset + limit]

# Route to list products by multiple IDs
@app.get(
    "/products/list",
    response_model=List[Product],
    dependencies=[Depends(get_api_key)]
)
def products_list(
        ids: List[int] = Query(..., description="Comma-separated list of product IDs"),
        limit: int = Query(5, ge=1, le=5),
        offset: int = Query(0, ge=0)):
    products = []
    for product_id in ids:
        product = get_product_by_id(product_id)
        if product:
            products.append(product)
    if not products:
        raise HTTPException(status_code=404, detail="No products found with the given IDs")
    return products[offset: offset + limit]

# Route to search for product by ID
@app.get(
    "/products/{product_id}",
    response_model=Product,
    dependencies=[Depends(get_api_key)],
    summary="Get product by ID",
    description="Returns details of a specific product by its ID.",
    responses={
        404: {"description": "No products found"},
        200: {"description": "Product found successfully"}
    }
)
def read_product(
    product_id: int = Path(..., title="Product ID", description="Unique product ID to be found", gt=0)
):
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="No products found.")
    return product
