from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()

# Exercise 2: Pydantic Model
class Item(BaseModel):
    id: int
    name: str
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)
    category: str

# In-memory database
items_db = []

# Exercise 1: Basic API
@app.get("/")
def read_root():
    return {"message": "Welcome to my API!", "author": "Nyanga Piethras"}

@app.get("/info")
def get_info():
    return {
        "course": "GenAI",
        "instructor": "Mr Allen",
        "weeks": 6
    }

@app.get("/health")
def health_check():
    return {"status": "OK"}

# Exercise 2 & 3: Items Store & Filtering
@app.post("/items", response_model=Item)
def create_item(item: Item):
    # Check if ID already exists
    if any(i.id == item.id for i in items_db):
        raise HTTPException(status_code=400, detail="Item ID already exists")
    items_db.append(item)
    return item

@app.get("/items", response_model=List[Item])
def get_items(category: Optional[str] = None, max_price: Optional[float] = None):
    results = items_db
    if category:
        results = [i for i in results if i.category.lower() == category.lower()]
    if max_price:
        results = [i for i in results if i.price <= max_price]
    return results

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    global items_db
    items_db = [i for i in items_db if i.id != item_id]
    return {"message": f"Item {item_id} deleted"}

@app.get("/stats")
def get_stats():
    if not items_db:
        return {"total_items": 0, "total_value": 0, "most_expensive": "N/A"}
    
    total_items = len(items_db)
    total_value = sum(item.price * item.quantity for item in items_db)
    most_expensive = max(items_db, key=lambda x: x.price).name
    
    return {
        "total_items": total_items,
        "total_value": total_value,
        "most_expensive": most_expensive
    }
