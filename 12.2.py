# -*- coding: utf-8 -*-
# Gyakorlat 12.2.
# Definiáljon   egy  BankSzamla()  osztályt,   ami   lehetővé   teszi   a  szamla1,  szamla2,   stb.   objektumok létrehozását.
# Az osztály constructora   két  példányattribútumot inicializáljon :  a  nev  és  egyenleg attribútumokat a 'Dupont' és 1000 alapértelmezett értékekkel.
# Definiáljon három másik metódust is :
# 1,­betesz(osszeg) adott összeget tesz a számlára 2,kivesz(osszeg) adott összeget vesz le a számláról 3,kiir() kiírja a számlatulajdonos nevét és a számlája egyenlegét.

class BankSzamla:
	"Ez egy szamla osztalyt definial"
	def __init__(self,nev='Dupont',egyenleg=1000):
		self.nev=nev
		self.egyenleg=egyenleg
	def betesz(self,osszeg):
		self.egyenleg+=osszeg
	def kivesz(self,osszeg):
		self.egyenleg-=osszeg
	def kiir(self):
		print('A szamlatulajdonos neve: {}'.format(self.nev))
		print('Szamla egyenleg: {}'.format(self.egyenleg))


szamla1 = BankSzamla('Duchmol', 800)
szamla1.betesz(350)
szamla1.kivesz(200)
szamla1.kiir()

szamla2 = BankSzamla()
szamla2.betesz (25)
szamla2.kiir()
