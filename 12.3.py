# -*- coding: utf-8 -*-
# Gyakorlat 12.3.

class Auto:
	"Egy auto osztaly ami az autok viselkedeset utanozza."
	def __init__(self,marka = 'Ford', szin = 'piros'):
		self.marka=marka
		self.szin=szin
		self.sofor='senki'
		self.sebesseg=0.
	def valaszt_sofort(self,nev):
		self.sofor=nev
	def gyorsit(self,gyorsulas,idotartam):
		"megváltoztatja az autó sebességét.(gyorsulas,idotartam)"
		if self.sofor != 'senki':
			self.sebesseg=gyorsulas*idotartam
		else:
			print('Ezt az autot senki nem vezeti.')
	def kiir_mindent(self):
		print('{} {}, vezeti {}, sebessege {} m/s.'.format(self.szin,self.marka,self.sofor,self.sebesseg))

a1 = Auto('Peugeot', 'kék')
a2 = Auto(szin = 'zöld')
a3 = Auto('Mercedes')
a1.valaszt_sofort('Roméo')
a2.valaszt_sofort('Juliette')
a2.gyorsit(1.8, 12)
a3.gyorsit (1.9, 11)
a2.kiir_mindent()
a3.kiir_mindent()
