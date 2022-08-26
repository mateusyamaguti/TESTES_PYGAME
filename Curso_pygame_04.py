'''Como controlar objetos na tela'''
import pygame
from pygame import *
from sys import exit
'''Iniciar pygame'''
pygame.init()

'''Criar tela do jogo'''
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))

'''Criar variaveis de posição'''
x_rect = (largura - 40) / 2
y_rect = (altura - 50) / 2

'''Colocar nome no display da janela'''
pygame.display.set_caption('Teste')

'''Criar objeto para controle de frames'''
relogio = pygame.time.Clock()

'''Laço de execução infinito para rodar o jogo'''
while True:
  '''Determinar os frames/segundo'''
  relogio.tick()
  '''limpar rastro do loop do retangulo para manter a tela preta'''
  tela.fill((0, 0, 0))
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
    '''Evento e comando para responder a teclas de movimento do teclado'''
    if event.type == KEYDOWN:
        if event.key == K_a:
            x_rect -= 20
        if event.key == K_d:
            x_rect += 20
        if event.key == K_w:
            y_rect -= 20
        if event.key == K_s:
            y_rect += 20

  pygame.draw.rect(tela, (255, 0, 0), (x_rect, y_rect, 40, 50))


  pygame.display.update()
