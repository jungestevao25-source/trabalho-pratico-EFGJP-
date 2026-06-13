import pygame
import random

LARGURA_TELA = 800
ALTURA_TELA = 600
FPS = 60
TITULO_JOGO = "TOP RACE"

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (100, 100, 100)
VERMELHO_OBSTACULO = (200, 30, 30)

# CONFIGURAÇÕES DA ESTRADA
LARGURA_ESTRADA = 450
X_ESTRADA = (LARGURA_TELA - LARGURA_ESTRADA) // 2

COMPRIMENTO_LINHA = 50
ESPACO_LINHA = 35
VELOCIDADE_PISTA = 8

# CONFIGURAÇÕES DOS OBSTÁCULOS
LARGURA_OBSTACULO = 60
ALTURA_OBSTACULO = 40
VELOCIDADE_OBSTACULO = 8
INTERVALO_SPAWN = 60

def criar_tela():
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    return tela


def obter_limites_pista():
    return (X_ESTRADA, X_ESTRADA + LARGURA_ESTRADA, 0, ALTURA_TELA)


def atualizar_pista(deslocamento_linhas):
    deslocamento_linhas += VELOCIDADE_PISTA
    if deslocamento_linhas >= COMPRIMENTO_LINHA + ESPACO_LINHA:
        deslocamento_linhas = 0
    return deslocamento_linhas


def desenhar_pista(tela, deslocamento_linhas):
    tela.fill((34, 139, 34))

    asfalto_rect = pygame.Rect(X_ESTRADA, 0, LARGURA_ESTRADA, ALTURA_TELA)
    pygame.draw.rect(tela, CINZA, asfalto_rect)

    pygame.draw.line(tela, PRETO, (X_ESTRADA, 0), (X_ESTRADA, ALTURA_TELA), 6)
    pygame.draw.line(tela, PRETO, (X_ESTRADA + LARGURA_ESTRADA, 0), (X_ESTRADA + LARGURA_ESTRADA, ALTURA_TELA), 6)

    y = - (COMPRIMENTO_LINHA + ESPACO_LINHA) + deslocamento_linhas
    while y < ALTURA_TELA:
        largura_faixa = 8
        x_faixa = (LARGURA_TELA // 2) - (largura_faixa // 2)
        pygame.draw.rect(tela, BRANCO, (x_faixa, y, largura_faixa, COMPRIMENTO_LINHA))
        y += COMPRIMENTO_LINHA + ESPACO_LINHA


def criar_obstaculo():
    x_min = X_ESTRADA
    x_max = X_ESTRADA + LARGURA_ESTRADA - LARGURA_OBSTACULO
    x = random.randint(x_min, x_max)
    return pygame.Rect(x, -ALTURA_OBSTACULO, LARGURA_OBSTACULO, ALTURA_OBSTACULO)


def atualizar_obstaculos(obstaculos, contador_spawn):
    # Move cada obstáculo para baixo
    for obstaculo in obstaculos:
        obstaculo.y += VELOCIDADE_OBSTACULO

    # Remove obstáculos que já saíram completamente da tela
    obstaculos = [o for o in obstaculos if o.top < ALTURA_TELA]

    # Controla o tempo até o próximo obstáculo aparecer
    contador_spawn += 1
    if contador_spawn >= INTERVALO_SPAWN:
        obstaculos.append(criar_obstaculo())
        contador_spawn = 0

    return obstaculos, contador_spawn


def desenhar_obstaculos(tela, obstaculos):
    for obstaculo in obstaculos:
        pygame.draw.rect(tela, VERMELHO_OBSTACULO, obstaculo)


def obter_hitboxes_obstaculos(obstaculos):
    return list(obstaculos)