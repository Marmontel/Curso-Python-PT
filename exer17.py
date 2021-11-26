#objetivo: faça um programa que leia o comprimento do cateto oposto e do
#cateto adjacente de um triangulo retangulo. calcule e mostre o comprimento
#da hipotenusa

#como eu fiz: (CERTO!!)

import math
cateto_oposto = float(input('Cumprimento do cateto oposto: '))
cateto_adjacente = float(input('Cumprimento do cateto adjacente: '))
print('A hipotenusa vai medir: {:.2f}'.format(math.hypot(cateto_oposto, cateto_adjacente)))

#PROF:

#sem import

#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print('A hiputenusa vai medir: {:.2f}'.format(hi))

#com import

#import math 
#cat_opo = float(input('Comprimento do cateto oposto: '))
#cat_adj = float(input('Comprimento do cateto adjacente: '))
#hi = math.hypot(cat_opo, cat_adj)
#print('A hipotenusa vai medir: {:.2f}'.format(hi))