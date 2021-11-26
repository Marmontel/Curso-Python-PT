# objetivo: criar calculos de juros anuais ou mensais, dando liberdade de escolha

# Como eu fiz (Situação criada, não há correção!)

def menu_inicial():
    print('Calcule seus juros, escolha uma das opções:')
    print('1. Calcular juros mensais')
    print('2. Calcular juros anuais')


def jur_men():
    val = float(input('Qual é o valor total do produto? R$'))
    jmes = float(input('Porcentagem de juros ao mês: '))
    jur = val + (val * jmes / 100) - val
    jurmen = val + (val * jmes / 100)
    print('A taxa de juros mensal é de {:.2f}% ao mês.'.format(jmes))
    print(
        'Sendo assim, o valor cobrado no acréscimo por mês deve ser de: R${:.2f}.'.format(jur))
    print('Com Juros mensal a parcela passa a ser: R${:.2f}.'.format(jurmen))
    print('Resultando também em R${:.3f} de juros por dia.'.format(jur / 30))


def jur_anu():
    val = float(input('Qual é o valor total do produto? R$ '))
    jmes = float(input('Porcentagem de juros anual: '))
    jur = val + (val * jmes / 100) - val
    jurmen = val + (val * jmes / 100)
    print('A taxa de juros é de {:.2f}% ao ano.'.format(jmes))
    print(
        'Sendo assim, o valor de juros ao mês deve ser de: R${:.2f}'.format(jur / 12))
    print('Em 1 ano o valor de torna: R${:.2f}'.format(jurmen))


if __name__ == '__main__':
    menu_inicial()
    escolha = input('Escolha qual das opções você deseja calcular: ')
    if escolha == '1':
        jur_men()

    if escolha == '2':
        jur_anu()
