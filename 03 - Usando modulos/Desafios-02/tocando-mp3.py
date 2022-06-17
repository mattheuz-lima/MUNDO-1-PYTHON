#Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.init()

x = 800
y = 600

tela = pygame.display.set_mode((x, y))
pygame.display.set_caption("PYTHON")

pygame.mixer.init()
pygame.mixer.music.load("nome_da_musica.mp3")
pygame.mixer.music.play()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False