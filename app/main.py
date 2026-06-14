from fastapi import FastAPI
from predictor import predict

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Proyecto Final MLOps ONNX"}

@app.post("/predict")
def make_prediction(data: dict):
    return predict(data)