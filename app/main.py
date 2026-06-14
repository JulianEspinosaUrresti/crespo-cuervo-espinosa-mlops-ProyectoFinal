from fastapi import FastAPI
from predictor import predict
from datetime import datetime
import os
import json

app = FastAPI()

ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")
LOG_FILE = f"predicciones_{ENVIRONMENT}.txt"


@app.get("/")
def home():
    return {
        "message": "Proyecto Final MLOps ONNX",
        "environment": ENVIRONMENT
    }


@app.post("/predict")
def make_prediction(data: dict):
    result = predict(data)

    log_record = {
        "timestamp": datetime.now().isoformat(),
        "input": data,
        "result": result
    }

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(json.dumps(log_record, ensure_ascii=False) + "\n")

    return result