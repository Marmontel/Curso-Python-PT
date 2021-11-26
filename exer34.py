# Objetivo: Escreva um programa que pergunte o salario de um funcionario e calcule o seu aumento;
# Para salarios superiores a $1250, calcule um aumento de 10%
# Para inferiores ou iguais o aumento é de 15%

salario = int(input('Qual é o valor do salário? $'))
aumento = salario + (salario * 0.10)
aumento_2 = salario + (salario * 0.15)

if salario >= 1250:
    print('Com aumento seu salário será: ${:.2f}'.format(aumento))
else:
    print('Com aumento seu salário será: ${:.2f}'.format(aumento_2))
