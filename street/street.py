import pygame
import sys
import os

LARGURA_TELA = 800
ALTURA_TELA = 600
FPS = 60
TITULO_JOGO = "TOP RACE"

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (100, 100, 100)

CAMINHO_RECORDE = "data/recorde.txt"
CAMINHO_SPRITES = "assets/imagens/spritesheet.bmp"

# CONFIGURAÇÕES DA ESTRADA
LARGURA_ESTRADA = 450
X_ESTRADA = (LARGURA_TELA - LARGURA_ESTRADA) // 2

COMPRIMENTO_LINHA = 50
ESPACO_LINHA = 35
VELOCIDADE_PISTA = 8
deslocamento_linhas = 0

# INICIALIZAÇÃO DO PYGAME
pygame.init()
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption(TITULO_JOGO)
clock = pygame.time.Clock()

# LOOP PRINCIPAL DO JOGO
executando = True
while executando:
    # Mapeamento de Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Lógica de Movimentação da Pista
    deslocamento_linhas += VELOCIDADE_PISTA
    if deslocamento_linhas >= (COMPRIMENTO_LINHA + ESPACO_LINHA):
        deslocamento_linhas = 0

    # RENDERIZAÇÃO
    # Grama
    tela.fill((34, 139, 34))

    # Asfalto
    asfalto_rect = pygame.Rect(X_ESTRADA, 0, LARGURA_ESTRADA, ALTURA_TELA)
    pygame.draw.rect(tela, CINZA, asfalto_rect)

    # Linhas Laterais de limite da pista
    pygame.draw.line(tela, PRETO, (X_ESTRADA, 0), (X_ESTRADA, ALTURA_TELA), 6)
    pygame.draw.line(tela, PRETO, (X_ESTRADA + LARGURA_ESTRADA, 0), (X_ESTRADA + LARGURA_ESTRADA, ALTURA_TELA), 6)

    # Linhas Tracejadas Centrais
    y = - (COMPRIMENTO_LINHA + ESPACO_LINHA) + deslocamento_linhas
    while y < ALTURA_TELA:
        largura_faixa = 8
        x_faixa = (LARGURA_TELA // 2) - (largura_faixa // 2)
        
        pygame.draw.rect(tela, BRANCO, (x_faixa, y, largura_faixa, COMPRIMENTO_LINHA))
        y += COMPRIMENTO_LINHA + ESPACO_LINHA

    # Atualiza a tela e dita o ritmo do jogo
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()