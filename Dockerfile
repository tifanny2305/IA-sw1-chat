# Imagen base
FROM python:3.12-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar requirements y instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente (sin .env)
COPY src/ ./src/
COPY main.py .

# Crear archivos __init__.py si no existen
RUN touch src/__init__.py src/helpers/__init__.py src/router/__init__.py

# Exponer el puerto de Flask
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "main.py"]