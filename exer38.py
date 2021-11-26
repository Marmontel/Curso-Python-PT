# Objetivo: Escreva um programa que leia dois numeros inteiros e
# Compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais.

num_1 = int(input('Digite um número inteiro: '))
num_2 = int(input('Digite outro número inteiro: '))
if num_1 > num_2:
    print('O PRIMEIRO valor é maior')
elif num_2 > num_1:
    print('O SEGUNDO valor é maior')
else:
    print('Não existe valor maior, os dois valores são iguais!')
