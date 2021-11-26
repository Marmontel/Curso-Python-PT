#objetivo: faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela

#Como eu fiz(correto{com bastante correções})

v = input('Digite algo: ')
print('O tipo primitivo desse valor é:', type(v))
print('Só tem espaços?', v.isspace())
print('É um numero?', v.isnumeric())
print('É alfabético?', v.isalpha())
print('É alfanumérico?', v.isalnum())
print('É em maiúscula?', v.isupper())
print('É minúsculo?', v.islower())
print('É Capitalizada?', v.istitle())
#'v' é um objeto e todo objeto tem seus metodos