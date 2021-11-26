# Objetivo: Escreva um programa que faça o computador pensar em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
# o programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

num = int(input('Digite um número: '))
list = random.randint(1, 5)
if num == list:
    print('Parabéns, você acertou o número!')
else:
    print('Número errado, tente novamente!')
