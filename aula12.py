# CONDIÇÕES/ESTRUTURAS ANINHADAS #
print('-='*20)
nome = str(input('Qual seu nome? '))
if nome == 'Gustavo':  # Se a váriavel nome for Gustavo, então print.
    print('Que nome bonito!')
# Se o nome for Pedro, Maria OU Paulo, então print.
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
# Se o nome estar entre a str(Ana Claudia Jéssica E Juliana), então print.
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')  # Se não for nenhum acima, então print.
print('Tenha um bom dia, {}'.format(nome))

print('-='*20)
