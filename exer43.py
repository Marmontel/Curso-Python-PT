# Objetivo: Crie um programa que leia peso e altura de uma pessoa e calcule
# seu IMC e mostre o seu status de acordo com a tabela abaixo
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

print('\n')
print('~='*20)
print('*/*\* CALCULE SEU IMC */*\*\n')
peso = float(input('Informe seu peso (em KG): '))
altura = float(input('Informe sua altura (em Metros): '))
imc = peso / (altura**2)
print('Seu imc é: {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você está ABAIXO DO PESO.')
elif imc <= 25:
    print('Você está no seu PESO NORMAL.')
elif imc <= 30:
    print('Você esta em SOBREPESO.')
elif imc <= 40:
    print('Você está em OBESIDADE.')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!.')
print('=~'*20)
