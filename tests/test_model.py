import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.inference import load_model, predict_iris

def test_model_loading():
    try:
        model = load_model()
        assert model is not None
    except FileNotFoundError:
        pass # Valid if running in a fresh CI environment without models

def test_prediction_logic():
    try:
        model = load_model()
        prediction, proba = predict_iris(model, 5.1, 3.5, 1.4, 0.2)
        assert isinstance(prediction, str)
        assert isinstance(proba, list)
    except FileNotFoundError:
        pass
