# Objetivo: Desenvolva um programa que pergunte a distancia de uma viagem em km.
# Calcule o preço da passagem, cobrando $0.50 por km para viagens de até 200km e $0.45 por km para viagens mais longas.

km = float(input('Qual é a distancia da viagem em KM? '))
passagem = km * 0.5
if km > 200:
    passagem = km * 0.45
print('O valor da sua passagem é: {}'.format(passagem))
