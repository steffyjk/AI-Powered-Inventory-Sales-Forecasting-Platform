from fastapi import APIRouter, BackgroundTasks
from app.services.ai_predictions import predict_sales

router = APIRouter()


@router.post("/predict")
def get_sales_prediction(data: list[int]):
    return predict_sales(data=data)


def send_alert(item_id):

    #Logic for sending alerts
    print(f"Alert: Item {item_id} is running low on stock!")


@router.post("/alerts")
def check_stock(item_id:int, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_alert, item_id)
    return {"message": "Alert task scheduled!"}