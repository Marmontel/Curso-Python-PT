# Objetivo: Crie um programa que leia 3 números e diga qual é o maior e qual é o menor

num = int(input('Digite um número: '))
num_2 = int(input('Digite outro número: '))
num_3 = int(input('Digite mais um número: '))
maior = num
if (num_2 > num):
    maior = num_2
if (num_3 > maior):
    maior = num_3
print('Maior:', maior)

menor = num
if (num_2 < menor):
    menor = num_2
if (num_3 < menor):
    menor = num_3
print('Menor:', menor)
