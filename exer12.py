#Objetivo: faça um algoritmo que leia o preço de um produto e mostre
#seu novo preço com 5% de desconto

#como eu fiz (CERTO!!)

val = float(input('Qual o valor do produto? R$'))
desc = val * 0.95
print('O produto que custava R${:.8f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(val, desc,))

#V.prof ;-;

preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))