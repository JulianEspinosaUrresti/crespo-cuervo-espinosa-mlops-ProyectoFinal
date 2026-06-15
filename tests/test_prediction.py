import sys
import os
import json

sys.path.append(
    os.path.join(os.path.dirname(__file__), "..", "app")
)

from predictor import predict


def test_prediction_response():

    with open("data/test_data.json", "r") as f:
        test_cases = json.load(f)

    for case in test_cases:

        result = predict(case)

        assert result is not None
        assert "prediction" in result
        assert "score" in result