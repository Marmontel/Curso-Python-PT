# objetivo: crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome 'Santo'
city = input(str('Qual o nome da sua cidade? '))
divsisao = city.split()
verified = 'Santo' in divsisao[0]
print('This result for a world "Santo" is: {}'.format(verified))

# **** DEU BOM !!! ****
