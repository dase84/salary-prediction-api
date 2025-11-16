import pandas as pd
import os

def load_data(filepath: str = None) -> pd.DataFrame:
    """
    Carga el dataset desde un archivo CSV.

    Parámetros:
    - filepath: ruta al archivo CSV. Si no se especifica, se usa la ruta por defecto relativa al notebook.

    Retorna:
    - DataFrame con los datos cargados
    """
    if filepath is None:
        # Ruta relativa al notebook (notebooks/01_eda.ipynb)
        filepath = os.path.abspath(os.path.join(os.getcwd(), "..", "data", "raw", "ds_salaries.csv"))

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Archivo no encontrado en: {filepath}")
    
    df = pd.read_csv(filepath)
    return df


def validate_columns(df: pd.DataFrame, expected_columns: list[str]) -> None:
    """
    Valida que el DataFrame contenga las columnas esperadas.

    Parámetros:
    - df: DataFrame a validar
    - expected_columns: lista de nombres de columnas esperadas

    Lanza:
    - ValueError si faltan columnas
    """
    missing = [col for col in expected_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Faltan columnas en el dataset: {missing}")