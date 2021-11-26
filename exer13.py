# objetivo: faça um algoritmo que leia o salario de um funcionario
# e mostre seu novo salario com reajuste de 15% de aumento

# como eu fiz (CERTO!!)

salar = float(input('Qual é o salário do funcionário? R$'))
reaj = salar + (salar * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento passa a receber R${:.2f}.'.format(
    salar, reaj))
