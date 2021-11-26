# objetivo: mostrar mensagem de boas vindas após perguntar o nome

# Como eu fiz (não estava errado)

nome = input('Seu nome? ')
n = nome
print('Olá,', n + ' que bom ter você aqui! '.format(n))

# como deve ser (resumido)

nome = input('Qual seu nome? ')
print('Olá {}, que bom ter você por aqui!'.format(nome))
