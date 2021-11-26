# objetivo: Crie um programa que leia um nome e diga se tem silva

nome = input(str('Digite seu nome: '))
verified = 'Silva' in nome
print('O resultado para "Silva" no seu nome é: {}'.format(verified))
