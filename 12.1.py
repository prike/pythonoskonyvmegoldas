# -*- coding: utf-8 -*-
# Gyakorlat 12.1.
# Definiáljon egy Domino() osztályt, amivel a dominójáték köveit szimuláló objektumok hozhatók létre. 
# Az osztály constructora inicializálja a dominó A és B felén lévő pontok értékeit (az alapértelmezett értékek =0).
# Definiáljon két másik metódust : a kiir_pontok() metódust, ami kiírja a két oldalon levő pontokat
# az ertek() metódust, ami a két oldalon lévő pontok összegét adja meg.

class Domino:
	"Ez egy dominó osztály definíciója"
	def __init__(self, aa=0, bb=0):
		self.a=aa
		self.b=bb
	def kiir_pontok(self):
		print('Az A ertek: {} es a B ertek: {}'.format(self.a,self.b))
	def ertek(self):
		print('Mindket oldalon levo pontok osszege: {}'.format(self.a+self.b))

myDomino = Domino(3,4)
Domino.kiir_pontok(myDomino)
Domino.ertek(myDomino)
