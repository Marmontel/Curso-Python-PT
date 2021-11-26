#faça um programa que leia um angulo qualquer e mostre o
# valor de seno, cosseno e tangente deste angulo.

#como eu fiz (CERTO!! {muita pesquisa!!})
'''
import numpy
valor = float(input('Digite o número que você deseja: '))
numero = numpy.radians(valor)
seno = numpy.sin(numero)
cose = numpy.cos(numero)
tang = numpy.tan(numero)
print('O ângulo de {}° tem o SENO de: {:.2f}'.format(valor, seno))
print('O ângulo de {}° tem o COSSENO de: {:.2f}'.format(valor, cose))
print('O ângulo de {}° tem o TANGENTE de: {:.2f}'.format(valor, tang))
'''
#eu 2 (CERTO! CRIADO COM A SUGESTÃO DO PROF! {NO COPY})

'''import math
val = float(input('Digite um valor: '))
num = math.radians(val) #PARA ESTE TIPO DE CALCULO É OBRIGATORIO O USO DE RADIANOS!!
sen = math.sin(num)
cos = math.cos(num)
tangen = math.tan(num)
print('O angulo de {}° tem o SENO de: {:.2f}'.format(val, sen))
print('O angulo de {}° tem o COSSENO de: {:.2f}'.format(val, cos))
print('O angulo de {}° tem o TANGENTE de: {:.2f}'.format(val, tangen))
'''
#PROF
'''import math
angulo = float(input('Digite um valor: '))
se = math.sin(math.radians(angulo))
co = math.cos(math.radians(angulo))
ta = math.tan(math.radians(angulo))
print('O ângulo de {}° tem o SENO de: {:.2f}'.format(angulo, se))
print('O ângulo de {}° tem o COSSENO de: {:.2f}'.format(angulo, co))
print('O ângulo de {}° tem o TANGENTE de: {:.2f}'.format(angulo, ta))
'''

#PROF 2 {CÓDIGO + LIMPO DE TODOS}

from math import sin, cos, tan, radians

ang = float(input('Digite um valor: '))
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print('O ângulo de {}° tem o SENO de: {:.2f}'.format(ang, seno))
print('O ângulo de {}° tem o COSSENO de: {:.2f}'.format(ang, coss))
print('O ângulo de {}° tem o TANGENTE de: {:.2f}'.format(ang, tang))