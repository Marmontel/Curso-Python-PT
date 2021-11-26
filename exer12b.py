#objetivo: criar calculos de % de juros a prazo.

#como eu fiz (situação criada, não há correção)

val = float(input('Qual é o valor do produto? R$'))
jmes = float(input('Qual é o valor do juros mensal?'))
jur = val + (val * jmes / 100) - val
jurmen = val + (val * jmes / 100)
print('A taxa de juros mensal é de {:.1f}% ao mês.'.format(jmes))
print('Sendo assim, o valor cobrado no acréscimo por mês deve ser de: R${:.2f}'.format(jur))
print('Com juros mensal, a parcela passa a ser: R${:.2f}'.format(jurmen))
print('Isto daria juros de R${:.3f}/dia. '.format(jur / 30))



#JUROS MENSAL | 