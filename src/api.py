from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import logging
import uvicorn

# We use relative imports inside the package if running as a module, 
# but for simple scripts it's easier to use absolute or handle paths.
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from schemas import IrisPredictionRequest, IrisPredictionResponse
from inference import load_model, predict_iris

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Iris Classification API",
    description="End-to-End MLOps API for Iris Flower Classification",
    version="1.0.0"
)

# CORS Middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model on startup
try:
    model = load_model()
    logger.info("Model loaded successfully.")
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    model = None

from fastapi.responses import RedirectResponse

@app.get("/", tags=["System"])
def root():
    return RedirectResponse(url="/docs")

@app.get("/health", tags=["System"])
def health_check():
    return {"status": "ok", "model_loaded": model is not None}

@app.post("/predict", response_model=IrisPredictionResponse, tags=["Prediction"])
def predict(request: IrisPredictionRequest):
    if model is None:
        raise HTTPException(status_code=503, detail="Model is not loaded")
    
    try:
        prediction, probabilities = predict_iris(
            model, 
            request.sepal_length, 
            request.sepal_width, 
            request.petal_length, 
            request.petal_width
        )
        return IrisPredictionResponse(prediction=prediction, probabilities=probabilities)
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
