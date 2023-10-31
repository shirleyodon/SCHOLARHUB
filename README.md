# SCHOLARHUB

## Description

Une plateforme de gestion en ligne des travaux académiques des étudiants de l'Ecole Nationale d'Informatique Fianarantsoa <br/>
L'application est entièrement développé en Python Flask.

## Structure du projet

    scholarhub/
    |__ backend/
    |   |__ app/
    |   |  |__ models/
    |   |  |__ utils/
    |   |  |__ views/
    |   |  |__ __init__.py
    |   |  |__ config.py
    |   |
    |   |__ Dockerfile
    |   |__ init.sql
    |   |__ requirements.txt
    |
    |__ frontend/
    |    |__ app/
    |    |  |__ models/
    |    |  |__ static/
    |    |  |  |__ bi/
    |    |  |  |__ css/
    |    |  |  |__ fonts/
    |    |  |  |__ icon/
    |    |  |  |__ img/
    |    |  |  |__ js/
    |    |  |
    |    |  |__ templates/
    |    |  |__ utils/
    |    |  |__ views/
    |    |  |__ __init__.py
    |    |  |__ config.py
    |    |
    |    |__ Dockerfile
    |    |__ launch.py
    |    |__ requirements.txt
    |
    |__ docker-compose.yml
    |__ README.md

## Lancement du projet avec docker compose

1. Clonez le dépôt : <br/>
   https://github.com/shirleyodon/SCHOLARHUB.git <br/>
   cd SCHLARHUB

2. Builder les images docker: <br/>

   ### Backend

   cd backend/
   docker build -t shirley/scholarhub:backend .

   ### Frontend

   cd frontend/
   docker build -t shirley/scholarhub:frontend .

3. Lancer l'application : <br/>
   docker compose up
