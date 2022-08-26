'''SNAKE GAME PT 03'''
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

'''Colocar nome no display da janela'''
pygame.display.set_caption('Snake Game')

'''Criar Mixer de SOM'''
'''Música de fundo'''
pygame.mixer.music.set_volume(0.1) #Volume da música de fundo
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - Tricks.mp3') #Escolher caminha da música
pygame.mixer.music.play(-1) #-1 é o parametro responsável gerar replay na música
'''Som da colisão'''
som_de_colisao = pygame.mixer.Sound('smw_coin.wav')
som_de_colisao.set_volume(0.6)
'''Som de up life'''
som_up_life = pygame.mixer.Sound('smw_1-up.wav')
som_up_life.set_volume(0.8)

'''Criar variaveis de posição'''
'''Snake'''
x_snake = (largura - 40) / 2
y_snake = (altura - 50) / 2

'''Varivaeis de movimento da Snake'''
velocidade = 10
x_controle = velocidade
y_controle = 0

'''Maçã'''
x_apple = randint(40, 600)
y_apple = randint(50, 430)

'''Variaveis de pontuação'''
pontos = 0
vidas = 0

'''Criar fonte para texto'''
fonte = pygame.font.SysFont('arial', 30, bold=True, italic=True)

'''Criar objeto para controle de frames'''
relogio = pygame.time.Clock()

'''Varável para update da cobra'''
list_body = []
'''Tamanho inicial da cobra'''
comprimento_inicial = 30
'''Variavel de game over'''
morreu = False

def update_snake(list_body):
    for XeY in list_body:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))

'''Função para reiniciar o jogo'''
def restart_game():
    global pontos, vidas, comprimento_inicial, x_snake, y_snake, list_body, list_head, x_apple, y_apple, morreu
    pontos = 0
    vidas = 0
    comprimento_inicial = 30
    x_snake = (largura - 40) / 2
    y_snake = (largura - 50) /2
    list_body = []
    list_head = []
    x_apple = randint(40, 600)
    y_apple = randint(50, 430)
    morreu = False

'''Laço de execução infinito para rodar o jogo'''
while True:
    '''Determinar os frames/segundo'''
    relogio.tick(30)
    '''limpar rastro do loop do retangulo para manter a tela preta'''
    tela.fill((255, 255, 255))
    '''Mensagem a ser exibida'''
    msg = f'Pontos: {pontos}   Vidas: {vidas}'
    texto_formado = fonte.render(msg, True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''Evento de comando para mannter a cobra em moviment continuo'''
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == - velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = - velocidade
                    x_controle = 0

    x_snake += x_controle
    y_snake -= y_controle

    snake = pygame.draw.rect(tela, (0, 255, 0), (x_snake, y_snake, 20, 20))
    apple = pygame.draw.rect(tela, (255, 0, 0), (x_apple, y_apple, 20, 20))

    if snake.colliderect(apple):
        x_apple = randint(40, 600)
        y_apple = randint(50, 430)
        pontos += 1
        comprimento_inicial += 1
        if pontos < 3:
            som_de_colisao.play()
        if pontos == 3:
            pontos = 0
            vidas += 1
            som_up_life.play()

    '''lógica para aumento da snake'''
    list_head = []
    list_head.append(x_snake)
    list_head.append(y_snake)
    list_body.append(list_head)

    '''Condição de morte da Snake'''
    if list_body.count(list_head) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        msg = 'Game Over! Pressione a tecla R para jogar novamente'
        texto_formado = fonte2.render(msg, True, (0, 0, 0))
        ret_texto = texto_formado.get_rect()
        morreu = True

        while morreu:
            tela.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        restart_game()
            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formado, ret_texto)
            pygame.display.update()

    if x_snake > largura:
        x_snake = 0
    if x_snake < 0:
        x_snake = largura
    if y_snake > altura:
        y_snake = 0
    if y_snake < 0:
        y_snake = altura

    '''Limitar o tamanho da cobra'''
    if len(list_body) > comprimento_inicial:
        del list_body[0]

    '''Chama a função de aumento do corpo da cobra'''
    update_snake(list_body)

    '''Apresentar texto na tela'''
    tela.blit(texto_formado, (360, 40))

    '''Fazer o update da tela'''
    pygame.display.update()