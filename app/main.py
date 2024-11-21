from fastapi import FastAPI
from app.routers import inventory

app = FastAPI(title="AI-Powered Inventory & Sales Forecasting Platform")

app.include_router(inventory.router, prefix="/inventory", tags=["Inventory"])