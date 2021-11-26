# Desenvolva um programa que leia 6 numeros
# e mostre a soma apenas daqueles que forem pares
# e desconsidere os numeros impares.

print('=~'*20)
print('DIGITE SEIS NÚMEROS E IREMOS SOMAR APENAS OS NÚMEROS PARES')
soma = 0
cont = 0
for num in range(1, 7):
    val = int(input('Digite o {} valor: '.format(num)))
    if val % 2 == 0:
        soma += val
        cont += 1
print('Você informou {} números e a soma dos números pares foi {}.'.format(cont, soma))
print('~='*20)
