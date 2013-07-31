#!/usr/bin/env python3
#-*- coding: utf8 -*-

#Import des noms des candidats des écoles

import sqlite3, json

c = sqlite3.connect("candidats.db");
cur = c.cursor()

classe = [("ABDALLAOUI MAAN","Zineb"),("AKOTO","Gbenoukpo"),("ATTAL","Hugo"),("BELAHCEN","Yassine"),("BOHAN","Arthur"),("CAILLE","Hélène"),("CAUSSANEL","Pierre"),("CHAGAR","Mohamed-Anis"),("COLAS","Cédric"),("CONNETABLE","Paul"),("CUDEY","Solène"),("DANEL","Laurence"),("DEVARADJA","Simon"),("DRIDI","Sami"),("EL ABBOUBI","Hamza"),("EL HAJEM","Inès"),("FEZZAZ","Othman"),("FOURNIER","Hugo"),("GABET","Julien"),("GARNELL","Émil"),("GOUNI","Julien"),("GUILLAUMET","Tom"),("GUILLEMOT","Xavier"),("GUYARD","Valentin"),("GUYOT-ROLLAND","Gabriel"),("KARANOUH","Rashad"),("KOENIG","Sandra"),("LAAOUAOUDA","Badr"),("LAMURE","Pierre-Louis"),("LOJKINE","Ophir"),("L’OLLIVIER","Brendan"),("LUO","David"),("MARCOU","Nicolas"),("MATHERON","Jeanne"),("MENAGE","Thibault"),("MODARRESI ESFES","Louis"),("NADIR","Salim"),("NGUYEN-VAN-SANG","David"),("ORHAN","Alexandre"),("OUALI ALAMI","Saad"),("POTIN","Justine"),("RADJABI","Maxence"),("ROUGE CARRASSAT","Alexis"),("SALEM","Nasser"),("SIMON","Alexandre"),("SRIHOU","Younes")]

sql = """
	SELECT resultats.ecole, resultats.rang FROM candidats
		INNER JOIN resultats
		ON resultats.id_candidat=candidats.id
	WHERE
		candidats.nom=?
		AND candidats.prenom=?;"""

export = {}
for eleve in classe:
	nom=eleve[1]+" "+eleve[0]
	export[nom] = {}
	for ecole,rang in cur.execute(sql, eleve):
		export[nom][ecole]=rang

print(json.dumps(export))
