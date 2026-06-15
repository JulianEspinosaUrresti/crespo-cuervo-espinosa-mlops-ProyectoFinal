from sklearn.tree import DecisionTreeClassifier
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
import numpy as np
import pandas as pd
import os

DATASET_URL = "https://github.com/user-attachments/files/28943409/train_data.csv"

df = pd.read_csv(DATASET_URL)

X = df[["edad", "ingresos", "deuda"]]
y = df["aprobado"]

model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X, y)

initial_type = [("float_input", FloatTensorType([None, 3]))]

onnx_model = convert_sklearn(
    model,
    initial_types=initial_type
)

os.makedirs("models", exist_ok=True)

with open("models/credit_model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

print("Modelo ONNX realista exportado a models/credit_model.onnx")