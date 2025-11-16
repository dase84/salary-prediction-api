# 💼 Data Scientist Salary Pipeline

Este proyecto implementa un pipeline de machine learning de punta a punta para predecir salarios de científicos de datos, utilizando el dataset de Kaggle ["Data Science Job Salaries"](https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries).

## 📁 Estructura del Proyecto
data-scientist-salary-pipeline/ 
├── data/              # Datos crudos y procesados 
├── notebooks/         # Exploración y prototipos 
├── src/               # Código fuente del pipeline 
├── tests/             # Pruebas unitarias 
├── docker/            # Configuración de contenedor 
├── config/            # Parámetros y configuraciones



## 🚀 Objetivo

- Predecir el salario de un científico de datos según características del puesto.
- Implementar un pipeline reproducible y modular.
- Desplegar una API con FastAPI.
- Contenerizar el proyecto con Docker.

## ⚙️ Instalación

```bash
# Crear entorno
conda env create -f environment.yml
conda activate salary-env

# Descargar datos
kaggle datasets download -d ruchi798/data-science-job-salaries -p data/raw --unzip