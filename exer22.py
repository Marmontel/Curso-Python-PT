# objetivo: crie um programa que leia o nome completo e mostre:
# nome com todas as letras maiusculas;
# nome com todas minusculas;
# quantas letras ao todo(sem considerar espaços)
# quantas letras tem o primeiro nome;


# nome:

nome = input(str('Digite seu nome completo: '))
divisao = nome.split()
# nome com todas as letras maiusculas:
print(nome.upper())
# nome com todas as letras minusculas:
print(nome.lower())
# quantas letras ao todo:
print(len(nome))
# quantas letras tem o primeiro nome:
print(len(divisao[0]))


# OU

nome = input(str('Digite seu nome completo: '))
# divisao das palavras
no_di = nome.split()
# frase em maiuscula
no_ma = nome.upper()
# frase em minuscula
no_mi = nome.lower()
# letras ao todo
no_ch = len(nome)
# quantas letras tem apenas o primeiro nome
no_pr = len(no_di[0])
print('Seu nome em maiúsculo fica: {} \nEm minúsculo fica: {} \nTem o total de {} letras \nSendo {} no primeiro nome'.format(
    no_ma, no_mi, no_ch, no_pr))

### DEU BOM !!!####
