
# 💼 Salary Prediction API

API para predecir el salario anual en USD de profesionales en ciencia de datos, basada en características como experiencia, tipo de empleo, tamaño de empresa, y rol técnico. Desarrollada con FastAPI, entrenada con scikit-learn, y lista para despliegue vía Docker.

---

## 🚀 Características

- Modelo de regresión lineal entrenado con datos reales
- API REST con FastAPI para servir predicciones
- Validación automatizada con `test_api.py`
- Dockerfile para despliegue portátil
- Modular y reproducible

---

## 📁 Estructura del proyecto

# 💼 Salary Prediction API

API para predecir el salario anual en USD de profesionales en ciencia de datos, basada en características como experiencia, tipo de empleo, tamaño de empresa, y rol técnico. Desarrollada con FastAPI, entrenada con scikit-learn, y lista para despliegue vía Docker.

---

## 🚀 Características

- Modelo de regresión lineal entrenado con datos reales
- API REST con FastAPI para servir predicciones
- Validación automatizada con `test_api.py`
- Dockerfile para despliegue portátil
- Modular y reproducible

---

## 📁 Estructura del proyecto

data-scientist-salary-pipeline/ 
├── Dockerfile 
├── requirements.txt 
├── models/ │   
├── linear_regression_salary.joblib 
│   └── model_columns.joblib 
├── src/ 
│   └── api/ 
│       └── main.py 
├── tests/ 
│   └── test_api.py 
├── notebooks/ 
│   └── 03_modeling.ipynb



---

## ⚙️ Instalación local

```bash
# Clona el repositorio
git clone https://github.com/dase84/salary-prediction-api.git
cd salary-prediction-api

# Crea entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instala dependencias
pip install -r requirements.txt

# Ejecuta la API
uvicorn src.api.main:app --reload

Accede a la documentación interactiva en: http://localhost:8000/docs

🧪 Validación del endpoint /predict
python tests/test_api.py

Este script envía datos simulados y valida que la API responda correctamente.

🐳 Despliegue con Docker
# Construye la imagen
docker build -t salary-api .

# Ejecuta el contenedor
docker run -p 8000:8000 salary-api



📬 Ejemplo de entrada JSON
{
  "experience_level_encoded": 2.0,
  "company_size_encoded": 1.0,
  "remote_ratio": 100,
  "work_year": 2023,
  "employment_type_Freelance": 0,
  "employment_type_Part_time": 0,
  "employment_type_Contract": 1,
  "job_title_Data_Analyst": 0,
  "job_title_Data_Scientist": 1,
  "job_title_Machine_Learning_Engineer": 0
}



📈 Entrenamiento del modelo
El modelo fue entrenado en notebooks/03_modeling.ipynb usando scikit-learn y registrado con MLflow. Los artefactos se guardan en models/.

🤝 Contribuciones
Este proyecto está en desarrollo. Se aceptan mejoras en modularización, visualización, y despliegue.

📄 Licencia
MIT License. Puedes usar, modificar y distribuir libremente.


























