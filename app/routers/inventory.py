from fastapi import APIRouter
from  app.models.inventory import InventoryItem

router = APIRouter()

inventory_db = []


@router.get('/')
def get_inventory():
    return inventory_db


@router.post("/")
def add_inventory_item(item: InventoryItem):
    inventory_db.append(item)
    return {"message": "Item added successfully!"}