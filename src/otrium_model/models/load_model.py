import logging
import pandas as pd
import pickle
import copy

# Get uvicorn logger
logger = logging.getLogger("uvicorn.error")


class Predictor:
    """
    Class for loading sales price predictions model and making predictions
    """

    def __init__(self, model_path: str) -> None:
        logger.info("Loading price predictions model")

        with open(model_path, "rb") as model_file:
            self.model = pickle.load(model_file)  # Load trained model

    def predict(self, sales_data: dict) -> pd.DataFrame:
        """
        Predicts sales price based on given sales data

        Args:
            sales_data (dict): sales data for prediction

        Returns:
            pd.DataFrame: predictions in Pandas DataFrame format
        """
        predictions = self.model.predict(sales_data)  # Retrieve predictions

        # Create Pandas Dataframe
        predictions_df = copy.deepcopy(sales_data)
        predictions_df['predicted_sale_price'] = predictions

        return predictions_df
