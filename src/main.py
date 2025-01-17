from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from core.settings import settings

app = FastAPI()

# In-memory data store
products = []

# Product model
class Product(BaseModel):
    id: int
    name: str
    price: float
    quantity: int

@app.get("/")
def read_root():
    return {"Hello": f"World from ENVIRONMENT={settings.ENVIRONMENT}"}

# Create a product
@app.post("/products/", response_model=Product, tags=["Products"])
def create_product(product: Product):
    # Check if product with the same ID already exists
    for existing_product in products:
        if existing_product.id == product.id:
            raise HTTPException(status_code=400, detail="Product with this ID already exists")
    products.append(product)
    return product

# Read all products
@app.get("/products/", response_model=List[Product], tags=["Products"])
def get_products():
    return products

# Read a single product by ID
@app.get("/products/{product_id}", response_model=Product, tags=["Products"])
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

# Update a product
@app.put("/products/{product_id}", response_model=Product, tags=["Products"])
def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")

# Delete a product
@app.delete("/products/{product_id}", tags=["Products"])
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product.id == product_id:
            del products[index]
            return {"detail": "Product deleted successfully"}
    raise HTTPException(status_code=404, detail="Product not found")
