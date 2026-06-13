import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def train_model():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, 'Iris_dataset.csv')
    model_path = os.path.join(base_dir, 'iris_log_reg_model.pkl')
    
    logger.info(f"Loading data from {data_path}")
    df = pd.read_csv(data_path)
    
    # Preprocessing: drop Id if it exists
    if 'Id' in df.columns:
        df = df.drop('Id', axis=1)
        
    X = df.drop('Species', axis=1)
    y = df['Species']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    logger.info("Training Logistic Regression model...")
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    
    accuracy = model.score(X_test, y_test)
    logger.info(f"Model trained. Test Accuracy: {accuracy:.4f}")
    
    joblib.dump(model, model_path)
    logger.info(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_model()
