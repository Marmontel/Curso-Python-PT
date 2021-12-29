# Crie um programa que leia varios numeros inteiros.
# o programa só vai parar quando o usuário digitar 999, que é a condição de parada
# no final mostre quantos números foram digitados e a soma entre eles (desconsiderando o flag)

contador = num = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {contador} números e a soma entre eles foi {soma}')
