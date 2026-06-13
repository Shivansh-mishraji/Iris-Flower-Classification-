from fastapi.testclient import TestClient
import os
import sys

# Ensure src module is reachable
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.api import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_predict_endpoint():
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    response = client.post("/predict", json=payload)
    if response.status_code == 200:
        data = response.json()
        assert "prediction" in data
        assert "probabilities" in data
