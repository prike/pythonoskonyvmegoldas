# -*- coding: utf-8 -*-
# Gyakorlat 4.7.
# Írjon egy programot, ami kiíratja a 7­es szorzótábla első 20 tagját, csillaggal jelölve azokat, 
# amelyek 3­nak többszörösei.

for i in range(1,21):
	a=i*7
	print(a,end=' '),
	if a%3 == 0:
		print('*', end=' ')



