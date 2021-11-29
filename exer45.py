# Crie um programa que faça o computador jogar pedra, papel, tesoura com vc
import time
import random
print('='*11, 'JOKENPÔ', '='*11, '\n')
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
computer = random.randint(0, 2)
opcao = int(input('Qual é a sua jogada? '))
if opcao >= 3:
    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE')
    exit()
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
print('=-'*20)
time.sleep(1)
print('RESULTADO:', end=' ')
if opcao == computer:
    print('O computador optou pelo mesmo! EMPATE')
elif opcao == 0 and computer == 1:
    print('O computador jogou PAPEL.\nJogador jogou PEDRA.')
    print('=-'*20)
    print('JOGADOR PERDEU')
elif opcao == 1 and computer == 2:
    print('O computador jogou TESOURA.\nJogador jogou PAPEL.')
    print('=-'*20)
    print('JOGADOR PERDEU')
elif opcao == 2 and computer == 0:
    print('O computador jogou PEDRA.\nJogador jogou TESOURA.')
    print('=-'*20)
    print('JOGADOR PERDEU')
elif opcao == 0 and computer == 2:
    print('O computador jogou TESOURA.\nJogador jogou PEDRA.')
    print('=-'*20)
    print('JOGADOR VENCEU')
elif opcao == 1 and computer == 0:
    print('O computador jogou PEDRA.\nJogador jogou PAPEL.')
    print('=-'*20)
    print('JOGADOR VENCEU')
elif opcao == 2 and computer == 1:
    print('O computador jogou PAPEL.\nJogador jogou TESOURA.')
    print('=-'*20)
    print('JOGADOR VENCEU')
else:
    print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE.')
