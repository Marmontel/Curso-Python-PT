# Objetivo: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar:
# O valor da casa
# O salário do comprador
# Em quantos anos ele vai pagar.

print('=~'*20)
print('SIMULADOR DE EMPRÉSTIMOS.')

# Valor da casa
valor_casa = float(input('Valor da casa: R$'))
# Salario do comprador
salario_comprador = float(input('Salário do comprador: R$'))
# Anos de financiamento
pagamento = int(input('Quantos anos de financiamento? '))
# Calculo de 30% do salário
porcentagem_salario = salario_comprador * 0.3
# Valor da casa dividindo-se pelo número de parcelas
casa = valor_casa / (pagamento * 12)

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(
    valor_casa, pagamento, casa))
# Se o valor das parcelas da casa exceder 30% do salario, então print NEGADO
if porcentagem_salario < casa:
    print('FINANCIAMENTO NEGADO!')
# Se não exceder, então print APROVADO
else:
    print('FINANCIAMENTO APROVADO!')
print('~='*20)
