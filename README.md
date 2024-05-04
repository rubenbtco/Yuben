# Cahier des charges:

Faire:
YUNA :
- une base de donnée avec 2 tables : Utilisateurs et chat
- un systeme de dialogue (chat) entre les joueurs

RUBEN:
- une carte
- un systeme de déplacement



Pour commencer initialiser un projet :

- Installer python 3.7.4
- pip install pygame pytmx pyscroll mysql.connector

- Avoir un serveur mysql (exemple : XAMPP ♥, Laragon, Wamp etc...)
- Créer une base de donnée nommée "nsi_eleve6" OU recharger le .sql (/data/db/eleve6.sql)

MODIFICATION A FAIRE
- Dans game.py: Ligne 32 Vérifier la connexion a la base de donnée (et vérifier l'intégrité de la base via le eleve6.sql (/data/db/))
- Dans /data/maps/meubles.tsx : changer le chemin de la balise image "source" (ce chemin doit rediriger vers {Localisation du projet}/assets/Modern tiles_Free/Interiors_free/16x16/Interiors_free_16x16.png)
- Dans /data/maps/murs.tsx : changer le chemin de la balise image "source" (ce chemin doit rediriger vers {Localistation du projet}/assets/Modern tiles_Free/Interiors_free/16x16/Room_Builder_free_16x16.png)