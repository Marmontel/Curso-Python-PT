# objetivo: um professor quer sortear a ordem de apresentação de trabalhos. faça um programa que leia os 4
# nomes e mostre a ordem sorteada

# como eu fiz: (resposta da aula.)
import random
#from random import shuffle

print('Digite o nome de cada aluno que você deseja sortear.\n')
alu_a = str(input('Primeiro nome: '))
alu_b = str(input('Segundo nome: '))
alu_c = str(input('Terceiro nome: '))
alu_d = str(input('Quarto nome: '))
list = [alu_a, alu_b, alu_c, alu_d]
random.shuffle(list)
print('A ordem de apresentação será: ')
print(list)
