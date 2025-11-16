import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica limpieza y transformación al dataset original.

    Operaciones:
    - Elimina duplicados
    - Filtra outliers extremos en salario
    - Codifica variables categóricas
    - Establece tipos de datos consistentes

    Retorna:
    - DataFrame limpio y transformado
    """
    df = df.copy()

    # Eliminar duplicados
    df.drop_duplicates(inplace=True)

    # Filtrar outliers extremos en salario
    df = df[df["salary_in_usd"] < df["salary_in_usd"].quantile(0.99)]

    # Codificar variables categóricas como tipo category
    df[["employee_residence", "company_location"]] = df[["employee_residence", "company_location"]].astype("category")

    # Codificación ordinal para experience_level
    encoder_exp = OrdinalEncoder(categories=[['EN', 'MI', 'SE', 'EX']])
    df["experience_level_encoded"] = encoder_exp.fit_transform(df[["experience_level"]])

    # Codificación ordinal para company_size
    encoder_size = OrdinalEncoder(categories=[['S', 'M', 'L']])
    df["company_size_encoded"] = encoder_size.fit_transform(df[["company_size"]])

    # Codificación one-hot para employment_type y job_title
    df = pd.get_dummies(df, columns=["employment_type", "job_title"], drop_first=True, dtype=int)

    # Eliminar columnas originales después de codificar
    df.drop(columns=["experience_level", "company_size"], inplace=True)

    # Renombrar columna de salario
    df.rename(columns={"salary_in_usd": "salary_usd"}, inplace=True)

    return df