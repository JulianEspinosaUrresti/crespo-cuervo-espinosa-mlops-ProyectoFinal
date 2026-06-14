from sklearn.tree import DecisionTreeClassifier
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
import numpy as np
import os

X = np.array([
    [25, 1000000, 900000],
    [30, 1500000, 1200000],
    [35, 2500000, 500000],
    [40, 5000000, 300000],
    [45, 2500000, 4000000],
    [55, 8000000, 500000],
    [22, 1800000, 100000],
    [70, 15000000, 10000000],
    [28, 1200000, 2000000],
    [50, 6000000, 800000]
], dtype=np.float32)

y = np.array([
    0,
    0,
    1,
    1,
    0,
    1,
    1,
    0,
    0,
    1
])

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