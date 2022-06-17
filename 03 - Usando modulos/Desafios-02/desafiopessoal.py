import random
import pygame
pygame.init()


lista = ('musica01.mp3', 'musica02.mp3', 'musica03.mp3') #tupla

x = 800
y = 600

tela = pygame.display.set_mode((x, y))
pygame.display.set_caption("PYTHON")

pygame.mixer.init()

pygame.mixer.music.load(random.choice(lista)) #serve para carregar uma música

pygame.mixer.music.play(1) #serve para tocar uma música 

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 