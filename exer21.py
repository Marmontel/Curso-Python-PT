# objetivo: criar um programa em python que abra
# e reproduza o audio de um arquivo

# Como eu fiz:

import pygame
pygame.init()  # sempre utilizar, modulo necessite de iniciação
pygame.mixer.music.load('doka.mp3')
pygame.mixer.music.play()
pygame.event.wait()
# CÓDIGO COM ERRO PORQUE NÃO TEM SAIDA DE SOM IDENTIFICADA!
