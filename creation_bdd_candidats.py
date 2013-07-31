#!/usr/bin/env python3
#-*- coding: utf8 -*-

#Import des noms des candidats des écoles

import sqlite3, json

c = sqlite3.connect("candidats.db");

print("Création de la base...")
c.executescript("""
	DROP TABLE IF EXISTS candidats;
	CREATE TABLE candidats (id int PRIMARY KEY, prenom text, nom text);
	DROP TABLE IF EXISTS resultats;
	CREATE TABLE resultats (id_candidat int, ecole text, rang int, PRIMARY KEY (ecole, rang));
""")

print("Création de la table de résultats...")
c.execute("CREATE TABLE IF NOT EXISTS resultats (id_candidat int, ecole text, rang num)")

print("Import de la liste de candidats...")
candFile = open("candidats_mines.json");
candidats = json.loads(candFile.read());
candFile.close();

print("Formatage des données...")
candFormate = [(int(ca[0]), ca[1][0], ca[1][1]) for ca in candidats.items()]

print("Insertion dans la base...")
c.executemany("INSERT INTO candidats VALUES (?,?,?)", candFormate)

print("Sauvegarde...")
c.commit()
c.close()
