
import requests

def test_prediction():
    url = 'http://127.0.0.1:8000/predict'

    # Datos de prueba (ajustados al esquema correcto)
    data = {
        "experience_level_encoded": 3.0,
        "company_size_encoded": 3.0,
        "remote_ratio": 0,
        "work_year": 2023,
        "employment_type_Freelance": 0,
        "employment_type_Part_time": 1,
        "employment_type_Contract": 0,
        "job_title_Data_Engineer": 1,
        "job_title_Data_Manager": 0,
        "job_title_Data_Scientist": 0,
        "job_title_Machine_Learning_Engineer": 0
    }

    response = requests.post(url, json=data)

    assert response.status_code == 200, f"Error {response.status_code}: {response.text}"
    result = response.json()
    assert "predicted_salary_usd" in result, "Respuesta no contiene 'predicted_salary_usd'"
    assert isinstance(result["predicted_salary_usd"], (int, float)), "El valor predicho no es numérico"

    print("Test exitoso. Predicción:", result["predicted_salary_usd"])

if __name__ == "__main__":
    test_prediction()