#objetivo: converter temperatura Celsius para Feirenhaint (sla se escreve assim)

#como eu fiz (Projeto pego por leitura de código no Google. Ficou excelente!)

def menu_inicial():
    print('Programa para Conversão de Temperaturas')
    print('1. Converter de Celsius para Fahrenheit')
    print('2. Converter de Fahrenheit para Celsius')

def cel_fahr():
    c = float(input('Informe a temperatura em °C: '))
    f = c * (9 / 5) + 32
    print('Valor em °F Fahrenheit: {:.2f}°F.'.format(f))

def fahr_cel():
    a = float(input('Informe a temperatura em °F: '))
    fc = (a - 32) * (5 / 9)
    print('Valor em °C Celsius: {:.2f}°C.'.format(fc))

if __name__=='__main__':   #menu (vem antes dos calcúlos! onde o tal cria situação alternativa.)
    menu_inicial() #primeira def (ou seja, uso isto para indicar def in if.)
    escolha = input('Escolha o tipo de que deseja realizar: ') #opções
    if escolha == '1': #opção 1
        cel_fahr()

    if escolha == '2': #opção 2
        fahr_cel()
