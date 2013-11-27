# -*- coding: utf-8 -*-
# Gyakorlat 5.5.
# Egy régi indiai legenda szerint a sakkjátékot egy öreg bölcs találta ki. A király meg akarta 
# azt neki köszönni és azt mondta, hogy jutalmul bármilyen ajándékot megad érte. Az öreg 
# azt kérte, hogy adjon neki egy kevés rizset öreg napjaira, pontosan annyi szem rizset, hogy 
# az általa feltalált játék első kockájára 1 szemet, 2 második kockára kettőt, a harmadikra 
# négyet, és így tovább egészen a 64­ik kockáig.
# Írjon   egy   Python   programot,   ami   kiíratja   a   sakktábla   64   kockájának   mindegyikére 
# elhelyezett rizsszemek számát. Számolja ki ezt a számot kétféleképpen a, rizsszemek pontos száma (egész szám) b, rizsszemek száma tudományos jelölésmódban (valós szám)


a=1
for i in range(1,65):	# bejárom a 64 kockát sakktáblán
	a+=2**i		# a-hoz rendelem a rizsszemek pontos számát

print('A pontos szám: ',a)
b=len(str(a))-1		# szamainak szama
print('A tudományos jelölésmód: {}E{}'.format(a/10**b,b))
