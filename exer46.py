# Objetivo: Faça um programa que mostre na tela a contagem regressiva para
# o estouro de fogos de artificios, indo de 10 até 0,
# com pausa de 1 seg entre eles

import time
print('CONTAGEM INICIADA...')
for fogos in range(10, 0, -1):
    print(fogos)
    time.sleep(1)
print('HAPPY NEW YEAR!')
