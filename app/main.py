from fastapi import FastAPI
from predictor import predict
from datetime import datetime
import os
import json
import requests

app = FastAPI()

ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")
LOG_FILE = f"predicciones_{ENVIRONMENT}.txt"


def save_log_to_gist(log_line: str):
    gist_id = os.getenv("GIST_ID")
    token = os.getenv("GITHUB_TOKEN")

    if not gist_id or not token:
        return

    filename = f"predicciones_{ENVIRONMENT}.txt"
    url = f"https://api.github.com/gists/{gist_id}"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    gist_data = response.json()
    current_content = gist_data["files"][filename]["content"]

    new_content = current_content + "\n" + log_line

    payload = {
        "files": {
            filename: {
                "content": new_content
            }
        }
    }

    update_response = requests.patch(url, headers=headers, json=payload)
    update_response.raise_for_status()


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
        "environment": ENVIRONMENT,
        "input": data,
        "prediction": result
    }

    log_line = json.dumps(log_record, ensure_ascii=False)

    with open(LOG_FILE, "a", encoding="utf-8") as file:
         file.write(log_line + "\n")

    save_log_to_gist(log_line)

    return result