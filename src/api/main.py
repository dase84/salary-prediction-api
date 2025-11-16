from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os
import pandas as pd

# Cargar modelo y columnas
base_dir = os.path.dirname(__file__)
model_path = os.path.abspath(os.path.join(base_dir, "..", "..", "models", "linear_regression_salary.joblib"))
columns_path = os.path.abspath(os.path.join(base_dir, "..", "..", "models", "model_columns.joblib"))

model = joblib.load(model_path)
model_columns = joblib.load(columns_path)

# Esquema de entrada (ajustable según tus columnas)
class SalaryFeatures(BaseModel):
    experience_level_encoded: float
    company_size_encoded: float
    remote_ratio: int
    work_year: int
    employment_type_Freelance: int = 0
    employment_type_Part_time: int = 0
    employment_type_Contract: int = 0
    job_title_Data_Analyst: int = 0
    job_title_Data_Scientist: int = 0
    job_title_Machine_Learning_Engineer: int = 0

# Inicializar API
app = FastAPI(title="Salary Prediction API")

@app.get("/")
def read_root():
    return {"message": "API de predicción de salario funcionando correctamente"}

@app.post("/predict")
def predict_salary(features: SalaryFeatures):
    input_df = pd.DataFrame([features.dict()])

    # Asegurar que todas las columnas estén presentes
    for col in model_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[model_columns]
    prediction = model.predict(input_df)[0]
    return {"predicted_salary_usd": round(prediction, 2)}