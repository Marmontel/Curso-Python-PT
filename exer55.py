# Objetivo: Faça um programa que leia o peso de cinco pessoas
# No final mostra qual foi o maior e o menor peso lidos

maior = 0
menor = 0
for pess in range(1, 6):
    peso = float(input(f'Peso da {pess}ª pessoa: '))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}KG.')
print(f'O menor peso lido foi de {menor}KG.')
