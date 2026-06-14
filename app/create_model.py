from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
import os

# Crear datos de ejemplo
X, y = make_classification(
    n_samples=500,
    n_features=3,
    n_informative=3,
    n_redundant=0,
    random_state=42
)

# Entrenar modelo
model = DecisionTreeClassifier(max_depth=4)
model.fit(X, y)

# Convertir a ONNX
initial_type = [("float_input", FloatTensorType([None, 3]))]

onnx_model = convert_sklearn(
    model,
    initial_types=initial_type
)

# Crear carpeta si no existe
os.makedirs("models", exist_ok=True)

# Guardar modelo
with open("models/credit_model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

print("Modelo de clasificación exportado a models/credit_model.onnx")