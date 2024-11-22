import numpy as np


def predict_sales(data):


    #dummy prediction logic as of now
    return {
        "prediction_sales": int(np.mean(data)* 1.1)
    }