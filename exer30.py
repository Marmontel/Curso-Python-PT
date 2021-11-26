# Objetivo: Criar um programa que leia um número e diga se ele é par ou impar

num = int(input('Digite um número para saber se ele é par ou ímpar: '))
resto = num % 2

if resto == 0:
    print('{} é um número par.'.format(num))
else:
    print('{} é um número ímpar.'.format(num))
