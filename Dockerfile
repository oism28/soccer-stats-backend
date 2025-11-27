# Imagen base
FROM python:3.10-slim

# Crear directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema (si haces consultas a BD, es útil tener psycopg2)
RUN apt-get update && apt-get install -y build-essential

# Copiar archivos
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Variables de entorno para Flask
ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED=1

# Exponer el puerto que usa Gunicorn
EXPOSE 8000

# Comando de ejecución
CMD ["gunicorn", "-c", "gunicorn_config.py", "app:app"]