FROM python:3.11-slim

# Python-Umgebungsvariable
ENV PYTHONUNBUFFERED=1

# Arbeitsverzeichnis im Container
WORKDIR /app

COPY requirements.txt .

# Installiere Python-Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Port für Django
EXPOSE 8000

# Starte Django Server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
