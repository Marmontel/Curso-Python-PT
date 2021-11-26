# objetivo: perguntas automaticas com alternativas de respostas


def menu():
    # a = int(input('Olá, diga para nossa assistente virtual o que deseja fazer: ')) #'\n{} \n{} \n{} \n{}'.format(rec, resg, recl, atend)))
    rec = '1. Recarga'
    resg = '2. Resgatar'
    recl = '3. Reclamar'
    atend = '4. Falar com atendente'
    print('Use apenas números!! \n{} \n{} \n{} \n{}'.format(rec, resg, recl, atend))


def rec():
    val = float(input('Digite o valor que deseja recarregar: '))
    sim = str('1. Sim')
    nao = str('2. Não')
    print('Tem certeza que você deseja recarregar este valor? R${:.2f}? \n{} \n{} '.format(
        val, sim, nao))


def sim():
    global preco
    print('Parabéns, você recarregou R${}!'.format(preco))


def nao():
    float(input('Ok, deseja realizar outro valor? Se sim, digite o valor, se não, não responda nada.'))


def resg():
    opc = float(input('Digite o valor do seu Gift: '))
    print('Parabéns, você resgatou R${:.2f}, use como quiser!'.format(opc))


def recl():
    str(input('Envie sua reclamação, em algumas horas o suporte irá retorna-lo(a): '))
    v = 'Recebemos sua reclamação! Desculpe-nos por qualquer incoveniencia. Iremos atende-lo em breve.'
    print('{}'.format(v))


def atend():
    n = int(input('Seu nome: '))
    i = int(input('Sua idade: '))
    print('Ok, estou te transferindo para um atendente! \n Parailizar este processo por favor me envie: \n {} \n {}'.format(n, i))


if __name__ == '__main__':
    menu()
    escolha = input('Escolha a opção que deseja executar: ')
    if escolha == '1':
        rec()
    if escolha == '2':
        resg()
    if escolha == '3':
        recl()
    if escolha == '4':
        atend()

if __name__ == '__main__':
    rec()
    escolha = input('Escolha a opção que deseja executar: ')
    if escolha == '1':
        sim()
        print('Parabéns, você realizou uma recarga.')
    if escolha == '2':
        nao()

valor = float(input('Digite o valor que deseja recarregar: '))
preco = valor
