import json
import sys
import os
import json

sys.path.append(
    os.path.join(os.path.dirname(__file__), "..", "app")
)

from predictor import predict

def test_model_metric_threshold():

    with open("data/test_data.json", "r") as f:
        test_cases = json.load(f)

    scores = []

    for case in test_cases:
        result = predict(case)
        scores.append(result["score"])

    avg_score = sum(scores) / len(scores)

    assert avg_score >= 0.80