# objetivo: um professor quer sortear um dos seus alunos
# para apagar o quadro. Faça um programa que ajude ele
# lendo o nome deles e escrevendo o nome do escolhido

# como eu fiz
from random import choice

aluno_1 = str(input('Primeiro aluno: '))
aluno_2 = str(input('Segundo aluno: '))
aluno_3 = str(input('Terceiro aluno: '))
aluno_4 = str(input('Quarto aluno: '))
tds = [aluno_4, aluno_3, aluno_2, aluno_1]
sorteio = choice(tds)
print('O aluno {} irá realizar a tarefa.'.format(sorteio))
