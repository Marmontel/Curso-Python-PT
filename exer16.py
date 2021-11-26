#objetivo: crie um programa que leia um numero real qualquer pelo teclado e
#mostre na tela a sua porção inteira.

#ex: Digite um número: 6.127
#O número 6.127 tem a parte inteira 6.

#Como eu fiz (CERTO!!):

from math import trunc #IMPORTEI A BIBLIO MATH COM A FUNÇÃO TRUNC
digite_numero = float(input('Digite um número: ')) #LEITURA DO NÚMERO
inteiro = trunc(digite_numero) #QUEBREI O NÚMERO E O TORNEI INTEIRO COM O TRUNC (DESNECESSÁRIO, POIS PODE SER INSERIDO NO .FORMAT!!!)
print('O número {} tem a parte inteira {}'.format(digite_numero, inteiro))

#PROF: +RESUMIDO!

#import math #IMPORTAÇÃO DA BIBLIOTECA
#num = float(input('Digite um valor: ')) #LEITURA DO NÚMERO
#print('O valor digitado foi {} e a sua porção inteira é: {}'.format(num, math.trunc(num)))

#OU 

#from math import trunc #IMPORTAÇÃO DA BIBLIOTECA + FUNÇÃO ESPECÍFICA COMO EU FIZ
#numero = float(input('Digite um valor: ')) #LEITURA DO NÚMERO
#print('O valor digitado foi {} e a sua porção inteira é: {}'.format(numero, trunc(numero)))

#CÓDIGO SEM USO DE IMPORTAÇÃO!
#num = float(input('Digite um valor: '))
#print('O valor digitado foi {} e a sua porção inteira é: {}'.format(num, int(num)))

#OPERADORES MATH: 
#CEIL (ARREDONDA PARA +)
#FLOOR (ARREDENDA PARA -)
#TRUNC (TRINCA O NÚMERO APÓS A VÍRGULA! {BOM PARA RESULTAR NÚMEROS INTEIROS})
#POW (POTENCIA)
#SQRT - ROOT SQUARE (RAIZ QUADRADA)
#FACTORIAL - (NÚMEROS FACTORADOS)
#MUITO +