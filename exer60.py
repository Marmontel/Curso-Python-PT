# Objetivo: Faça um programa que leia um número qualquer
# e mostre o seu fatorial.
# EX... 5 = 5x4x3x2x1=120

# Com While
from math import factorial
numero = int(input('Digite um número para calcular o seu fatorial: '))
cont = numero
fatorial = 1
print(f'Calculando {numero}! = ', end='')
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' =', end='')
    fatorial *= cont
    cont -= 1
print(f' {fatorial}')


# Com FOR
numero = int(input('Digite um número para calcular seu fatorial: '))
cont = numero
fatorial = 1
print(f'Calculando {numero}! = ', end='')
for cont in range(numero, 0, -1):
    print(cont, end=' ')
    print('x ' if cont > 1 else '= ', end='')
    fatorial *= cont
print(f'{fatorial}')

# Com biblioteca
numero = int(input('Digite um número para calcular seu fatorial: '))
fatorial = factorial(numero)
cont = numero
print(f'Calculando {numero}! = ', end='')
for cont in range(numero, 0, -1):
    print(cont, end=' ')
    print('x ' if cont > 1 else '= ', end='')
print(fatorial)
