# Objetivo: Escreva um programa que leia um número inteiro qualquer e mostre na tela os
# primeiros elementos de uma sequência de Fibonacci

print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)

termos = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = 1
print('=~'*15)
print(f'{termo1} ⇢ {termo2}', end='')
contador = 3
while contador <= termos:
    termo3 = termo1 + termo2
    print(f' ⇢ {termo3}', end='')
    termo1 = termo2
    termo2 = termo3
    contador += 1
print(' ⇢ FIM')
print('=~'*15)
