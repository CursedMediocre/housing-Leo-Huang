from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Charger le modèle
model = joblib.load('./model/housing_model.pkl')

@app.post('/predict')
def predict(features: dict):
    # Convertir les caractéristiques en DataFrame
    df = pd.DataFrame([features])
    prediction = model.predict(df)
    return {"median_house_value": prediction[0]}
