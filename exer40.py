# Crie um programa que leia duas notas de um aluno e calcule sua média
# Mostrar mensagem de acordo com a média atingida
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota_1 = float(input('Primeira nota: '))
nota_2 = float(input('Segunda nota: '))
media = (nota_1 + nota_2) / 2
print('Tirando {} e {}, a média do aluno é {:.1f}.'.format(nota_1, nota_2, media))
if media < 5.0:
    print('O aluno está REPROVADO!')
elif media >= 7.0:
    print('O aluno está APROVADO!')
elif media > 5.0 or media < 6.9:
    print('O aluno está em RECUPERAÇÃO!')
