# SCHOLARHUB

## Description

Une plateforme de gestion en ligne des travaux académiques des étudiants
Le backend est développé en Flask et SQLAlchemy tandis que le frontend est en Reactjs

## Structure du projet
    scholarhub/
    |__ /scholarhub/
    |  |__ models/
    |     |__annee.py
    |     |__categorie.py
    |     |__encadreur.py
    |     |__etablissement.py
    |     |__etudiant.py
    |     |__inscription.py
    |     |__livre.py
    |     |__niveau.py
    |     |__parcours.py
    |     |__redaction.py
    |     |__titre.py
    |  |__ utils/
    |     |__annee.py
    |     |__categorie.py
    |     |__encadreur.py
    |     |__etablissement.py
    |     |__etudiant.py
    |     |__inscription.py
    |     |__livre.py
    |     |__niveau.py
    |     |__parcours.py
    |     |__redaction.py
    |     |__titre.py
    |  |__ views/
    |     |__annee.py
    |     |__categorie.py
    |     |__encadreur.py
    |     |__etablissement.py
    |     |__etudiant.py
    |     |__inscription.py
    |     |__livre.py
    |     |__niveau.py
    |     |__parcours.py
    |     |__redaction.py
    |     |__titre.py
    |   |__ __init__.py
    |   |__ config.py
    |__ init.sql
    |__ launch.py
    |__ requirements.txt

  ## Lancement du projet sans docker
  
  1. Clonez le dépôt
     git clone https://shirleyodon/SCHOLARHUB
     cd SCHLARHUB
     
  2. Installez les dépendances
     pip install -r requirements.txt
     
  3. Lancez l'application
     python launch.py

  ## Lancement du projet avec docker

  1. Clonez le dépôt
     git clone https://shirleyodon/SCHOLARHUB
     cd SCHLARHUB

  2. Builder l'image docker
     docker build -t <image_name:version> .

  3. Lancer l'application
     docker compose up
  
  
