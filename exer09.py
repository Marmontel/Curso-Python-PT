#objetivo: fazer um programa ler um numero inteiro e mostrar a tabuada

#como eu fiz (CERTO!)

num = int(input('Digite um numero para saber a tabuada: '))
print(num, 'x 1 = {}'.format(num*1))
print(num, 'x 2 = {}'.format(num*2))
print(num, 'x 3 = {}'.format(num*3))
print(num, 'x 4 = {}'.format(num*4))
print(num, 'x 5 = {}'.format(num*5))
print(num, 'x 6 = {}'.format(num*6))
print(num, 'x 7 = {}'.format(num*7))
print(num, 'x 8 = {}'.format(num*8))
print(num, 'x 9 = {}'.format(num*9))
print(num, 'x 10 = {}'.format(num*10))

#RESUMIDO(prof):

num = int(input('Digite um numero para saber a tabuada: '))
print('-'*12)
print('{} x {:2} = {}'.format(num, 1, (num*1)))
print('{} x {:2} = {}'.format(num, 2, (num*2)))
print('{} x {:2} = {}'.format(num, 3, (num*3)))
print('{} x {:2} = {}'.format(num, 4, (num*4)))
print('{} x {:2} = {}'.format(num, 5, (num*5)))
print('{} x {:2} = {}'.format(num, 6, (num*6)))
print('{} x {:2} = {}'.format(num, 7, (num*7)))
print('{} x {:2} = {}'.format(num, 8, (num*8)))
print('{} x {:2} = {}'.format(num, 9, (num*9)))
print('{} x {:2} = {}'.format(num, 10, (num*10)))
print('-'*12)