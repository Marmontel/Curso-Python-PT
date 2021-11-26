#objetivo: crie um programa que converta dinheiro em caixa para dólar

#como eu fiz (CERTO!!)

#d = float(input('Quanto você tem na carteira? '))
#print('O do seu saldo convertido em dólar é: {:.2f}'.format(d / 5.26))
#print('OBS: cotação do dólar: R$5,26')

#prof: (resumi mais)
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.26
print('Com R${:.2f} você compra US${:.2f}'.format(real, dolar))
print('OBS: cotação do dólar a R$5,26 do dia 17/09/2021')