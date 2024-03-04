import pyshark
import pandas as pd
import joblib  # Import joblib for loading the model

# Load the trained model
model = joblib.load('ensemble_model.joblib')
print(model)
