# Crie um programa que mostre na tela todos os números pares que
# estão no intervalo entre 1 e 50
import time
print('Os números pares entre 1 e 50 são:')
for par in range(2, 51, 2):
    print(par)
    time.sleep(0.2)
