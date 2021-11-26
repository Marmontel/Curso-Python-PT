# Objetivo: Faça um programa que leia o ano de nascimento
# de um jovem e informe, de acordo com a sua idade:
# - Se ele AINDA VAI SE ALISTAR ao serviço militar
# - Se é a HORA DE SE ALISTAR
# - Se já PASSOU DO TEMPO do alistamento
# - Quanto tempo passou/esta faltando no prazo

from datetime import date

atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
    anos = atual + saldo
    print('Seu alistamento será em {}.'.format(anos))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado a {} anos.'.format(saldo))
    anos = atual - saldo
    print('Seu alistamento foi em {}.'.format(anos))
