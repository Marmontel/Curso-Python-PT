# Objetivo: Melhore o exer61, perguntando para
# o usuário se ele quer mostrar mais alguns termos
# O programa encerra quando quando o usuario
# solicitar 0 termos da PA
print('GERADOR DE PA\n', '='*15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
zero = 10
while zero != 0:
    total = total + zero
    while cont <= total:
        print(f'{termo}', end=' ⇢ ')
        termo += razao
        cont += 1
    print('PAUSA')
    zero = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados!')
