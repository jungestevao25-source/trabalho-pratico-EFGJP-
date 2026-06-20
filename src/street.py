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

#CONFIGURAÇÃO DA DIFICULDADE PROGRESSIVA
#Sistema de progressão de dificulde por degraus baseada nos pontos.
LIMIARES_NIVEL = [0, 10, 20, 35, 55, 80, 110, 145, 185, 230, 280]

#Aumento da velocidadde do obstaculo até o "teto".
INCREMENTO_VELOCIDADE= 1
VELOCIDADE_OBSTACULO_MAX = 16

#Quanto o intervalo do spawn diminui por nivel(até o piso).
#Intervalo menor = obstaculos aparecem com mais frequência.
DECREMENTO_INTERVALO = 4
INTERVALO_SPAWN_MIN = 24

#Configuração taxa de spawn duplo de obstaculos.
NIVEL_MIN_SPAWN_DUPLO = 2
CHANCE_SPAWN_DUPLO = 0.35

#Espaço minimo de pssagem que sempre fica livre entro os dois obstaculos.
FOLGA_MINIMA_PASSAGEM = 110



def criar_tela():
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    return tela


def obter_limites_pista():
    return (X_ESTRADA, X_ESTRADA + LARGURA_ESTRADA, 0, ALTURA_TELA)

def calcular_nivel(pontos):
    """ 
    Descobre o nivel do jogador com base na lista LIMIARES_NIVEL.
    Percorre a lsita e restorna o nivel de acordo com o limiar do nível.
    """
    nivel = 0
    for indice, limiar in enumerate(LIMIARES_NIVEL):
        if pontos >= limiar:
            nivel = indice
        else:
            break
    return nivel

def calcular_dificuldade(pontos):
    nivel = calcular_nivel(pontos)

    velocidade = VELOCIDADE_OBSTACULO + (nivel * INCREMENTO_VELOCIDADE)
    velocidade = min(velocidade, VELOCIDADE_OBSTACULO_MAX)

    intervalo = INTERVALO_SPAWN - (nivel * DECREMENTO_INTERVALO)
    intervalo = max(intervalo, INTERVALO_SPAWN_MIN)

    return velocidade, intervalo
   

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


def criar_obstaculo(velocidade_obstaculo):
    x_min = X_ESTRADA
    x_max = X_ESTRADA + LARGURA_ESTRADA - LARGURA_OBSTACULO
    x = random.randint(x_min, x_max)
    return {
        "rect": pygame.Rect(x, -ALTURA_OBSTACULO, LARGURA_OBSTACULO, ALTURA_OBSTACULO),
        "velocidade": velocidade_obstaculo,
    }

def criar_par_obstaculos(velocidade_obstaculo):
    largura_util = LARGURA_ESTRADA - LARGURA_OBSTACULO
    metade = largura_util//2
    
    x_esq = X_ESTRADA + random.randint(0, metade)
    x_dir = X_ESTRADA + random.randint(metade, largura_util)

    distancia_atual = x_dir - (x_esq+LARGURA_OBSTACULO)
    if distancia_atual < FOLGA_MINIMA_PASSAGEM:
        x_dir = x_esq + LARGURA_OBSTACULO + FOLGA_MINIMA_PASSAGEM

    x_max = X_ESTRADA + LARGURA_ESTRADA - LARGURA_OBSTACULO
    if x_dir > x_max: 
        excedente = x_dir - x_max
        x_dir -= excedente
        x_esq -= excedente

    obstaculo_esq = {
        "rect": pygame.Rect(x_esq, -ALTURA_OBSTACULO, LARGURA_OBSTACULO, ALTURA_OBSTACULO),
        "velocidade": velocidade_obstaculo,
    }
    obstaculo_dir = {
        "rect": pygame.Rect(x_dir, -ALTURA_OBSTACULO, LARGURA_OBSTACULO, ALTURA_OBSTACULO),
        "velocidade": velocidade_obstaculo,
    }
    return [obstaculo_esq, obstaculo_dir]

def atualizar_obstaculos(obstaculos, contador_spawn, pontos):
    ''' Move os obstaculos existentes, remove os que saíram da tela e controla
    o spawn de novos obstáculos com base na dificuldade atual (derivada dos pontos).'''
    velocidade_atual, intervalo_atual = calcular_dificuldade(pontos)
    nivel_atual = calcular_nivel(pontos)

    #Move cada obstaculo pra baixo, usando a velocidade em que ele nasceu
    for obstaculo in obstaculos:
        obstaculo["rect"].y += obstaculo["velocidade"]

    #Remove obstaculos que ja sairam completamente da tela.
    obstaculos = [o for o in obstaculos if o["rect"].top < ALTURA_TELA]

    # Controla o tempo até o próximo obstáculo aparecer (intervalo diminui com a dificuldade)
    contador_spawn += 1
    if contador_spawn >= intervalo_atual:
        pode_vir_duplo = nivel_atual >= NIVEL_MIN_SPAWN_DUPLO
        if pode_vir_duplo and random.random() < CHANCE_SPAWN_DUPLO:
            obstaculos.extend(criar_par_obstaculos(velocidade_atual))
        else:
            obstaculos.append(criar_obstaculo(velocidade_atual))
        contador_spawn = 0

    return obstaculos, contador_spawn



def desenhar_obstaculos(tela, obstaculos):
    for obstaculo in obstaculos:
        pygame.draw.rect(tela, VERMELHO_OBSTACULO, obstaculo["rect"])


def obter_hitboxes_obstaculos(obstaculos):
    return [o["rect"] for o in obstaculos]