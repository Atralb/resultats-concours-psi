#!/usr/bin/env python3
#-*- coding: utf8 -*-

#Import des résultats des candidats des écoles

nom_fichier_candidats = "resultats_mines_oral.html"

import sqlite3
from bs4 import BeautifulSoup

c = sqlite3.connect("candidats.db");

print("Ouverture du fichier '%s'..." % nom_fichier_candidats)
with open(nom_fichier_candidats, 'rb') as fichier_candidats:
	print("Lecture du fichier...")
	soup = BeautifulSoup(fichier_candidats.read(), features="xml")

liste = soup.find("div", attrs={"class":"liste"})

for candSoup in liste.findAll("tr"):
	infos = candSoup.findAll("td")
	if (len(infos) is not 5): continue
	id_candidat = int(infos[1].text)
	try: rg = int(infos[4].text)
	except:rg=None
	if rg:
		print("%d\r" % id_candidat)
		c.execute("INSERT INTO resultats VALUES (?,?,?)", (id_candidat, "mines", rg))
		
c.commit()
c.close()
