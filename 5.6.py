# -*- coding: utf-8 -*-
# Gyakorlat 5.6.
# Írjon   egy   programot,   ami   meghatározza,   hogy   egy  karakterlánc   tartalmazza­e   az   « e » 
# karaktert.

text=input('Irjon be egy szöveget: ')
car='e'

for i in range(len(text)):
	if text[i] == car:
		print('Van benne "e" karakter.')

