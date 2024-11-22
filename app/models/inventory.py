from pydantic import BaseModel
from typing import Optional
from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Enum, Float


class InventoryItem(BaseModel):
    id: int
    name: str
    quantity: int
    price: float
    category: Optional[str]


class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Integer)
    price = Column(Float)
    category = Column(String, nullable=True)
