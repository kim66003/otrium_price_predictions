import io
import logging
import os
from typing import Dict
from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from otrium_model.models.load_model import Predictor
import pandas as pd
import json

# Initiate router. Tag as Predictor for documentation purposes.
router = APIRouter(tags=["Predictor"])

# Initiate logger
logger = logging.getLogger("uvicorn.error")

# Get package directory path
package_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load trained predictor model for making sales price predictions
path_to_model = os.path.join(package_directory, "models", "best_model.pkl")
prediction_maker = Predictor(path_to_model)

# Define asynchronous POST route for handling POST requests containing sales data.
# Returns predicted prices as CSV for download.
@router.post("/api/predict")
async def get_prediction(params: Dict) -> json:
    """
    Uses the predictor model to make sales price predictions for the given sales data

    Args:
        params: Request Body (JSON)

    Returns:
        StreamingResponse: CSV file for download
    """

    # as_dict = request.dict()
    # as_dict = json.loads(params)

    # logger.info(type(as_dict))

    sales_data = pd.DataFrame.from_dict(params)  # JSON to Pandas DataFrame

    predictions_df = prediction_maker.predict(sales_data)  # Make predictions

    return predictions_df.to_json()
