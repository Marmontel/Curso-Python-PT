# OBJETIVO: faça um programa que leia um número de 0 a 9999 e mostre na tela
# cada um dos digitos separados;
# EX:
# Digite um número: 1834

#unidade: 4
#dezena: 3
#centenas: 8
#milhar: 1

num = input(str('Digíte um número: '))
print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(
    num[3], num[2], num[1], num[0]))

# **** DEU BOM !!! ***
