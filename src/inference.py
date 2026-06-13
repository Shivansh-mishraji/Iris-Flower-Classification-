import joblib
import pandas as pd
import numpy as np
import os
import warnings

# Suppress sklearn warnings about feature names if they occur
warnings.filterwarnings("ignore", category=UserWarning)

MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'iris_log_reg_model.pkl')

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
    return joblib.load(MODEL_PATH)

def predict_iris(model, sepal_length: float, sepal_width: float, petal_length: float, petal_width: float):
    # Depending on how the model was trained, it might expect a DataFrame with column names or just a numpy array.
    # We will try DataFrame first, as it's standard for pandas-based training.
    X_df = pd.DataFrame([{
        'SepalLengthCm': sepal_length,
        'SepalWidthCm': sepal_width,
        'PetalLengthCm': petal_length,
        'PetalWidthCm': petal_width
    }])
    
    try:
        prediction = model.predict(X_df)[0]
    except ValueError:
        # Fallback to numpy array if feature names don't match or model expects 2D array without names
        X_np = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = model.predict(X_np)[0]
        X_df = X_np # Use for proba
        
    try:
        probabilities = model.predict_proba(X_df)[0].tolist()
    except Exception:
        probabilities = []
        
    # Map integer labels back to string names if the model was trained with LabelEncoder
    label_mapping = {
        0: 'Iris-setosa',
        1: 'Iris-versicolor',
        2: 'Iris-virginica',
        '0': 'Iris-setosa',
        '1': 'Iris-versicolor',
        '2': 'Iris-virginica'
    }
    
    pred_str = str(prediction)
    if prediction in label_mapping:
        pred_str = label_mapping[prediction]
    elif pred_str in label_mapping:
        pred_str = label_mapping[pred_str]
        
    return pred_str, probabilities
