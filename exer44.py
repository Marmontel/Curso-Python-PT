# Crie um programa que calcule o valor a ser pago por um produto considerando
# Preço normal e condiçoes de pagamento:
# - A vista dinheiro/pix: 10% de desconto
# - A vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

# EXEMPLO EXER37
print('='*11, 'LOJAS AMÉRICAS', '='*11, '\n')
preco = float(input('Valor total das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] À vista dinheiro/Pix com 10% de desconto.
[ 2 ] À vista no cartão de débito com 5% de desconto.
[ 3 ] Em até 2x sem juros no cartão de crédito
[ 4 ] 3x ou mais no cartão com acréscimo de 20%''')
opcao = int(input('Informe a opção de pagamento desejada: '))
if opcao == 1:
    dinheiro = preco - (preco * 0.10)
    print('Pagando à vista você ganha 10% de desconto! De R${:.2f} o produto passa a custar R${:.2f}!'.format(
        preco, dinheiro))
elif opcao == 2:
    debito = preco - (preco * 0.05)
    print('Pagando no débito à vista você ganha 5% de desconto! De R${:.2f} o produto passa a custar R${:.2f}!'.format(
        preco, debito))
elif opcao == 3:
    print('Pagar em 2x de R${:.2f} no cartão de crédito. Não há descontos.'.format(
        preco / 2))
elif opcao == 4:
    juros = preco + (preco * 0.2)
    print('Pagando em 3x ou mais você terá 20% de acréscimo! De R${:.2f}, o produto passa a custar R${:.2f}!'.format(
        preco, juros))
else:
    print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE.')
print('=~'*20)
