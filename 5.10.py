# -*- coding: utf-8 -*-
# Gyakorlat 5.10.
# Az   előző   gyakorlatból   kiindulva   írjon   egy   scriptet,   ami   meghatározza,   hogy   egy 
# karakterlánc palindrom e (vagyis ami mindkét irányból olvasva ugyan az), mint például 
# « radar » vagy « sós ».

text=input('Adj meg egy szöveget amiről eldöntöm palindrom-e: ')
b=''
a=len(text)-1
while 0 <= a:
	b+=text[a]
	a-=1
if b == text:
	print('Ez egy palindrom.')
else:
	print('Ez nem egy palindrom.')
