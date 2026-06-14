import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "app"))

from predictor import predict


def test_prediction_response():
    input_data = {
        "edad": 35,
        "ingresos": 2500000,
        "deuda": 500000
    }

    result = predict(input_data)

    assert result is not None
    assert "prediction" in result
    assert "score" in result