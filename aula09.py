frase = 'Curso em video Python'
print(frase[3])  # Retorna a quarta letra da str = 'S'
print(frase[3:13])  # Retorna da letra 3 até a letra 12 = 'so em Vide'
print(frase[:13])  # Da primeira letra até a 12 = 'Curso em Vide'
print(frase[13:])  # Da letra 13 até o final = 'o Python'
print(frase[1:15])  # Da letra 1 até letra 15 = 'usro em Video'
print(frase[1:15:2])  # da letra 1 até a letra 15 de 2 em 2 = 'us mVdo'
print(frase[1::2])  # Vai até o final da frase pulando de 2 em 2 = 'us mVdoPto'
print(frase[::2])  # Mostra a frase completa pulando de 2 em 2 = 'Croe ie yhn'

# printar grandes textos: --- USAR ASPAS TRIPLAS ('''  ''')

print('''Textos em inglês são uma ótima opção para treinar a interpretação e também para ver sua evolução! Confira esses textos para iniciantes e teste seus conhecimentos. Curso de inglês para iniciantes ao avançado, só podia ser Wizard!​
Que tal praticar inglês de um jeito divertido com esse quiz com textos em inglês que a Wizard preparou para você?
6 livros em inglês para praticar o idioma
5 livros em inglês para ler neste ano
Já trouxemos aqui no site alguns exercícios em inglês para iniciantes e agora você também pode testar sua interpretação de texto: leia os textos abaixo e responda às questões para verificar se você compreendeu o conteúdo.''')


# como contar quantas vezes tem a letra direcionada

# Conta quantas vezes tem a letra 'o' na frase (tem diferença em maiuscula e minus.)
print(frase.count('o'))
# Deixa a frase INTEIRA em maiuscula e conta quantas vezes tem a letra 'o'
print(frase.upper().count('o'))


print(len(frase))  # diz o tamanho da frase/ quantidade de caracteres MUITO UTIL!

# Substitui a palavra 'Python' por 'Android'
print(frase.replace('Python', 'Android'))
# Para mudar a palavra em eternamente
#frase = frase.replace
# print(frase)

# Verifica se a palavra curso existe na frase, retorna true and false
print('Curso' in frase)

print(frase.find('Video'))  # mostra em que posição inicia a palavra
# retorna -1 caso não exista

# mostra em que posição inicia deixando tudo minuscula
print(frase.lower().find('video'))

# Cria uma lista separando a frase = ['Curso', 'em', 'Video', 'Python']
print(frase.split())

frase = 'Curso em Video Python'
dividido = frase.split()
print(dividido[0])  # retorna a primera palavra da frase!! = 'Curso'
print(dividido[1])  # retorna a segunda palavra da frase!! = 'em'
# retorna a terceira palavra = 'video' --- retornando a terceira letra de Video = 'e'
print(dividido[2][3])
