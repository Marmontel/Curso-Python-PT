# Objetivo: Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$7,00 por cada Km acima do limite

velocidade = int(input('A que velocidade estava o carro? '))
if velocidade > 80:
    print('Você ultrapassou o limite de velocidade. E será multado em R${}, por estar a {}km/h acima dos 80km/h permitidos'.format((velocidade - 80) * 7, velocidade - 80))
else:
    print('Você está no limite de velocidade previsto por lei e não será multado!')
