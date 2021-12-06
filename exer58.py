# Objetivo: Melhore o jogo do exer28 onde o computador vai "pensar"
# em um número entre 0 e 10. Só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer

import random
cont = 1
print('Sou seu computador...')
list = random.randint(0, 10)
print('Acabei de pensar em um número de 0 a 10.')
print('Será que você consegue adivinhar qual foi?')
num = int(input('Qual seu palpite? '))
while num != list:
    cont += 1
    if num < list:
        print('Mais...', end='')
    else:
        print('Menos...', end='')
    num = int(input('Tente novamente: '))
if num == list:
    print(
        f'Parabéns, o número era {list} e você acertou em {cont} tentativas.')
