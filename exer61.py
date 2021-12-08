# Objetivo: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
print('GERADOR DE PA\n', '='*15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}', end=' ⇢ ')
    termo += razao
    cont += 1
print('FIM!')
