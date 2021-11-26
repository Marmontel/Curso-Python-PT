# objetivo: ler um nome completo e mostrar o primeiro e o ultimo nome;

nome = input(str('Digite seu nome completo: '))
dividido = nome.split()
print('Seu primeiro nome é: {}'.format(dividido[0]))
print('Seu ultimo nome é: {}'.format(dividido[-1]))
