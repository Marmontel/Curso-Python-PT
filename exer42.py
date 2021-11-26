# Objetivo: Aprimorar exer35, acrescentar o recurso tipo de triangulo.
# - Equilátero: Todos os lados são iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

print('~='*20)
print('ANALISADOR DE TRIÂNGULOS')
lado_1 = int(input('Primeiro segmento: '))
lado_2 = int(input('Segundo segmento: '))
lado_3 = int(input('Terceiro segmento: '))
if lado_1 < lado_2 + lado_3 and lado_2 < lado_1 + lado_3 and lado_3 < lado_1 + lado_2:
    print('Os segmentos acima PODEM FORMAR triângulo ', end='')
    if lado_1 == lado_2 == lado_3:
        print('Equilátero')
    elif lado_1 != lado_2 != lado_3 != lado_1:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo.')
print('~=¨..'*10)
