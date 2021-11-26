# objetivo: criar um programa que multiplique qualquer numero:

# como eu fiz: (PROJETO MEU)
import PySimpleGUI as gs
# Criar janelas e estilos


def janela_num():
    gs.theme('Reddit')
    out = [
        [gs.Text('Digite um número: ')],
        [gs.Input(float(key='1', size=(20, 0)))],
        [gs.Button('Calcular')]
    ]
    return gs.Window('Digite um número: ', layout=out, finalize=True)


def janela_mult():
    gs.theme('Reddit')
    lay = [
        [gs.Text('Multiplicar em quantas vezes o número anterior? ')],
        [gs.Input(float(key='2', size=(20, 0)))],
        [gs.Button('Ver resultado')]
    ]
    return gs.Window('Multiplicador', layout=lay, finalize=True)


# Criar as janelas iniciais
janela1, janela2 = janela_num(), None
# Criar um loop de leitura de eventos
while True:
    window, event, val = gs.read_all_windows()
    # Quando janela for fechada
    if window == janela1 and event == gs.WIN_CLOSED:
        break
    # Quando queremos ir para a próxima janela
    if window == janela1 and event == 'Calcular':
        janela2 = janela_mult()
        janela1.hide()
    if window == janela2 and event == 'Ver resultado':
        if val == '1'*'2':
            gs.popup('O resultado da sua equação é: {}'.format(val))
    # Quando queremos voltar para a janela anterior

# Logica de o que deve acontecer ao clicar nos button
