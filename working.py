#
# Python FAST API Tutorial
#
# needs:
# pip install fastpi
# pip install uvicorn
#
# working.py
#
# application server to be started in working.py directory with: 
# uvicorn working:app --reload
#
from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

# http://127.0.0.1:8000/
@app.get("/")
def home():
    return {"Data": "Testing"}

# http://127.0.0.1:8000/about
@app.get("/about")
def about():
    return {"Data": "About"}

inventory = {
        }

# http://127.0.0.1:8000/get-item/1 
@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]

# http://127.0.0.1:8000/get-item/test 
@app.get("/get-item/{item_id}/{name}")
def get_item(item_id: int, name: str = None):
    return inventory[item_id]

# http://127.0.0.1:8000/get-item 
@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path (description = "The ID of the item you would like to view"), gt=0):
    return inventory[item_id]

# http://127.0.0.1:8000/get-by-name/1?test=2&name=Milk
@app.get("/get-by-name/{item_id}")
def get_item(*, item_id: int, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=404, detail="Item name not found")

#
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists"}

    inventory[item_id] = item 
    return inventory[item_id]
    
#
@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"Error": "Item does not exist"}
    if item.name != None:
        inventory[item_id].name = item.name 
    if item.price != None:
        inventory[item_id].price = item.price 
    if item.brand != None:
        inventory[item_id].brand = item.brand 
    return inventory[item_id]

#
@app.delete("/delete-item/{item_id}")
def delete_item(item_id : int = Path( description = "The ID of the ititem you want to delete", gt=0)):
    if item_id not in inventory:
        return {"Error": "ID does not exist."}

    del inventory[item_id]

