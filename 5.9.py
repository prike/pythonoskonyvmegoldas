# -*- coding: utf-8 -*-
# Gyakorlat 5.9.
# Írjon egy programot, ami egy új változóba fordított sorrendben másolja át egy karakterlánc 
# karaktereit.
# Így például « zorglub » ­ból « bulgroz » lesz.

text=input('Irjon be egy szöveget: ')
textLength=len(text)
a=len(text)-1
while 0 <= a:
	print(text[a], end='')
	a-=1
print()
