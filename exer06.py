#Objetico: mostrar o dobro, o triplo e a raiz quadrada de um número

#como eu fiz (Raiz errada faltou o (1/2))

v = int(input('Digite um numero: '))
print('O dobro de {} é: {}'.format(v, (v*2)))
print('O triplo de {} é: {}'.format(v, (v*3)))
r = v**2
print('A raiz quadrada de {} é: {}'.format(v, r))

#como deveria ser:

v = int(input('Digite um número '))
d = v*2
t = v*3
r = v**(1/2)
print('O dobro de {} é {}.\n O triplo de {} é {}.\n E a raiz quadrada de {} é: {}.'.format(v, d, v, t, v, r))

#DAR TAG(#) EM UM DOS MODELOS PARA APENAS DPS EXECUTA-LO!!