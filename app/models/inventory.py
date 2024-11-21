from pydantic import BaseModel
from typing import Optional


class InventoryItem(BaseModel):
    id: int
    name: str
    quantity: int
    price: float
    category: Optional[str]