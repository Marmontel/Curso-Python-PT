# objetivo: faça um programa que leia uma frase e mostre:
# * Quantas vezes aparece a letra 'a'
# * Em que posição ela aparece pela primeira vez
# * Em que posição ela aparece pela ultima vez


# Como eu fiz(DEU BOM!! [peguei upper e strip na aula;])
frase = input(str('Digite algo: ')).upper().strip()
b = frase.count('A')
pos = frase.find('A')+1
ult = frase.rfind('A')+1
print("A letra A aparece {} vezes na frase. \nA primeira letra apareceu na posição {}. \nE a ultima letra apareceu na posição {}.".format(b, pos, ult))
