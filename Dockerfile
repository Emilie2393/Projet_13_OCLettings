# Utiliser une image Python légère
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le contenu du projet dans le conteneur
COPY . /app

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Collecter les fichiers statiques
RUN python manage.py collectstatic --noinput


# Exposer le port par défaut de Django
EXPOSE 8000

# Définir la commande de démarrage (Gunicorn pour la production)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]
