#objetivo: faça o programa ler em numero inteiro e mostrar antecessor e sucessor.

#como eu fiz (correto para usar CASO PRECISE POSTERIORMENTE!)

v = int(input('Digíte um número: '))
ant = v - 1
suc = v + 1
print('O antecessor é: {}'.format(ant))
print('O sucessor é: {}'.format(suc))

#prof código reduzido

v = int(input('Digíte um número: '))
print('Analisando o valor {}, o antecessor é {} e o sucessor é {}'.format(v, (v-1), (v+1)))
