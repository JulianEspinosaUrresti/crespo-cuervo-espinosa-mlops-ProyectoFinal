import sys
import os
import json

sys.path.append(
    os.path.join(os.path.dirname(__file__), "..", "app")
)

from predictor import predict


def test_model_accuracy_threshold():

    with open("data/test_data.json", "r") as f:
        test_cases = json.load(f)

    correct = 0

    for case in test_cases:
        expected = case["esperado"]

        input_data = {
            "edad": case["edad"],
            "ingresos": case["ingresos"],
            "deuda": case["deuda"]
        }

        result = predict(input_data)

        if result["class"] == expected:
            correct += 1

    accuracy = correct / len(test_cases)

    assert accuracy >= 0.80