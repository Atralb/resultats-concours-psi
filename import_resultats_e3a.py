#!/usr/bin/env python3
#-*- coding: utf8 -*-

#Import des résultats des candidats des écoles

nom_fichier_candidats = "resultats_mines_oral.html"

import sqlite3
from bs4 import BeautifulSoup
from urllib import request

c = sqlite3.connect("candidats.db");
cur = c.cursor()
can_ids = cur.execute("""
	SELECT id FROM candidats
	EXCEPT
	SELECT id_candidat FROM resultats WHERE ecole != "mines"
""")

for (can_id,) in can_ids.fetchall():
	with request.urlopen("http://www.e3a.fr/2013_result/resultats_concours.php?can_id=%d"%can_id) as page:
		soup = BeautifulSoup(page.read())

	td = [el.text.strip() for el in soup.findAll("td", "miniL")]
	res = [(can_id, td[i],int(td[i+2])) for i in range(0,len(td),3) if td[i+1] in ("classé", "Grand admissible")]

	try:
		cur.executemany("INSERT INTO resultats VALUES (?,?,?)", res)
		c.commit()
	except sqlite3.IntegrityError as e :
		#Les résultats sont déjà dans la base
		res = []
	except Exception as e:
		print("Erreur inattendue : %s", e)
	

	print("\rcandidat %5d : %2d résultats insérés" % (can_id, len(res)), end='')
c.close()
