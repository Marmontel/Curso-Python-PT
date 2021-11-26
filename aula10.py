# Estrutua simples
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi: {}'.format(m))

# Estrutura composta
n_1 = float(input('Digite a primeira nota: '))
n_2 = float(input('Digite a segunda nota: '))
media = (n_1 + n_2)/2
print('Sua média foi: {:.1f}'.format(media))
if media >= 6.0:  # Caso a nota seja maior ou igual a 6.0
    print('Parabéns, você foi aprovado!')  # Este será o print para a nota
else:
    # Menor que 6.0 terá este print
    print('Estude mais, pois infelizmente você foi reprovado :( ')

# Estrutura Simples:

nome_1 = input(str('Qual seu nome? '))
if nome_1 == 'Maria':  # Se o nome for Maria (ex) terá este print
    print('Que nome lindo vc tem!')
print('Bom dia, {}'.format(nome_1))

# Estrutura composta:
nome = input(str('Qual seu nome? '))
if nome == 'Maria':
    print('Que nome lindo vc tem!')
else:  # Se o nome não for 'Maria' terá este print (ex)
    print('Nossa, que nome comum vc tem!')
print('Bom dia, {}'.format(nome))
