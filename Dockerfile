# Système de base avec Python
FROM python:3.11

# Dossier de travail dans le conteneur
WORKDIR /app

# Copier tous les fichiers dans le conteneur
COPY . .

# Installer Flask
RUN pip install -r requirements.txt

# Lancer l'API
CMD ["python", "app.py"]