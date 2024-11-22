from fastapi import APIRouter, BackgroundTasks

router = APIRouter()

@router.get("/")
def get_dashboard():
    return {
        "sales_trend": [100,200,150],
        "profit_margin": [20,30,25]
    }