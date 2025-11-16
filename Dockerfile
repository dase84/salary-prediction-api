# Imagen base con Python
FROM python:3.10-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos necesarios
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY models/ models/
COPY src/ src/

# Comando para iniciar la API
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]