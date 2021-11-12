import json
from fastapi.testclient import TestClient
from otrium_model.app import app
import requests

# Initiate FastAPI test client that extends the main client.
client = TestClient(app)

def test_predictions():
    """
    Tests the route responsible for making predictions for given sales data by checking status code
    """
    # Load test data
    with open('./test_data.json', 'r') as file:
        data_ = json.load(file)
    # Make POST request using test data
    response = client.post("/api/predict", json=data_)

    assert response.status_code == 200  # Test if status code 200