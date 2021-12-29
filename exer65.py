# Crie um programa que leia vários números inteiros
# no final da execução, mostre a média entre todos e qual foi o maior e o menor valor lido
# O programa deve perguntar se o usuario deseja continuar ou não a digitar valores
continuar = 'S'
media = soma = contador = 0
while continuar in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    contador += 1
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    continuar = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
media = soma / contador
print(f'Você digitou {contador} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
