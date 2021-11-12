from fastapi import FastAPI
from otrium_model.docs.tags import tags_metadata
from otrium_model.routers import predictor

# Initiate FastAPI app
app = FastAPI(
    title="Sales prediction API",
    description="API for making predictions for given sales data",
    openapi_tags=tags_metadata,
)

# Include router of predictor API
app.include_router(predictor.router)
