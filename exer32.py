# Objetivo: Faça um programa que leia um ano qualquer e mostre se ele é bissexto

ano = int(input('Digite o ano para saber se ele é ou não um ano bissexto: '))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('Este é um ano bissexto')
else:
    print('Este não é um ano bissexto')
