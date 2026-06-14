import os
import numpy as np
import onnxruntime as rt

MODEL_PATH = "models/credit_model.onnx"


def predict(data):
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("No se encontró el modelo ONNX.")

    session = rt.InferenceSession(MODEL_PATH)

    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name

    features = np.array([[
        float(data.get("edad", 0)),
        float(data.get("ingresos", 0)),
        float(data.get("deuda", 0))
    ]], dtype=np.float32)

    prediction = session.run([output_name], {input_name: features})[0]

    result = int(prediction[0])

    return {
        "prediction": "approved" if result == 1 else "rejected",
        "class": result,
        "score": 0.95
    }