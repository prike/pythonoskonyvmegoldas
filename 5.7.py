# -*- coding: utf-8 -*-
# Gyakorlat 5.7.
# Írjon   egy   programot,   ami   megszámolja  az   « e »   karakter   előfordulásainak   számát   egy 
# stringben.

text=input('Irjon be egy szöveget: ')
car='e'
a=0
for i in range(len(text)):
	if text[i] == car:
		a+=1
print('Ebben a szövegben {} "e" karakter van.'.format(a))
