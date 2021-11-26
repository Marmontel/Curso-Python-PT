# Faça um programa que calcule a soma entre todos os
# numeros impares que são multiplos de 3 e que se encontram no intervalo
# de 1 até 500

soma = 0
cont = 0
for impar in range(1, 501, 2):
    if impar % 3 == 0:
        soma += impar
        cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
