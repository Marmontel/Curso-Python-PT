# Obejtivo: refazer o exer09 mostrando a tabuada
# de um número que o usuario escolher
# só que agr utilizando for

num = int(input('Digite um número para saber a tabuada: '))
print('=~'*12)
for multip in range(1, 11, 1):
    mult = num * multip
    print('{} x {:2} = {}'.format(num, multip, mult))
print('=~'*12)
