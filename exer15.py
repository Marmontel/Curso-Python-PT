#Escreva um programa que pergunte a quantidade 
# de km percorridos por um carro alugado 
# e a quantidade de dias pelos quais ele foi 
# alugado. calcule o preço a pagar, sabendo que 
# o carro custa R$60/ dia e R$0,15 por km rodado.

#como eu fiz: (DEU CERTO!!)

d = float(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
tot = (60 * d) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(tot))

#PROF

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é: R${:.2f}'.format(pago))