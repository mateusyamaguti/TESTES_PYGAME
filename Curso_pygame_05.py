'''Colisão entre objetos'''
import pygame
from pygame import *
from sys import exit
from random import randint

'''Iniciar pygame'''
pygame.init()

'''Criar tela do jogo'''
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))

'''Criar variaveis de posição'''
'''Retângulo Vermelho'''
x_rect_red = (largura - 40) / 2
y_rect_red = (altura - 50) / 2
'''Retângulo Azul'''
x_rect_blue = randint(40, 600)
y_rect_blue = randint(50, 430)

'''Colocar nome no display da janela'''
pygame.display.set_caption('Teste')

'''Criar objeto para controle de frames'''
relogio = pygame.time.Clock()

'''Laço de execução infinito para rodar o jogo'''
while True:
  '''Determinar os frames/segundo'''
  relogio.tick(60)
  '''limpar rastro do loop do retangulo para manter a tela preta'''
  tela.fill((0, 0, 0))
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
    '''Evento e comando para responder a teclas de movimento do teclado precionada'''
    if pygame.key.get_pressed()[K_a]:
        x_rect_red -= 5
    if pygame.key.get_pressed()[K_d]:
        x_rect_red += 5
    if pygame.key.get_pressed()[K_s]:
        y_rect_red += 5
    if pygame.key.get_pressed()[K_w]:
        y_rect_red -= 5

    rect_red = pygame.draw.rect(tela, (255, 0, 0), (x_rect_red, y_rect_red, 40, 50))
    rect_blue = pygame.draw.rect(tela, (0, 0, 255), (x_rect_blue, y_rect_blue, 40, 50))

    if rect_red.colliderect(rect_blue):
        x_rect_blue = randint(40, 600)
        y_rect_blue = randint(50, 430)

    pygame.display.update()