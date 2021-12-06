# Objetivo: Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] qual é o maior
# [4] digitar novamente (novos números)
# [5] sair

primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''
[ 1 ] SOMAR OS VALORES
[ 2 ] MULTIPLICAR OS VALORES
[ 3 ] QUAL DOS VALORES É O MAIOR
[ 4 ] DIGITAR NOVAMENTE
[ 5 ] SAIR DO PROGRAMA
''')
    opcao = int(input('>>> Qual é a sua opção: '))
    if opcao == 1:
        soma = primeiro + segundo
        print(f'\033[31mA soma entre {primeiro} e {segundo} é {soma}.\033[m')
    elif opcao == 2:
        multiplicar = primeiro * segundo
        print(
            f'\033[31mO resultado de {primeiro} x {segundo} é {multiplicar}.\033[m')
    elif opcao == 3:
        if primeiro < segundo:
            print(
                f'\033[31mEntre {primeiro} e {segundo} o maior valor é {segundo}\033[m')
        else:
            print(
                f'\033[31mEntre {primeiro} e {segundo} o maior valor é {primeiro}\033[m')
    elif opcao == 4:
        print('\033[31mInforme os números novamente!\033[m')
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
    elif opcao == 5:
        print('\033[31mFinalizando ...\033[m')
    else:
        print('\033[31mOpção inválida. Tente novamente!\033[m')
print('-='*20)
