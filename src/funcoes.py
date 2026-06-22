"""Funções auxiliares de regra e lógica: pista, obstáculos, dificuldade."""

import pygame
import random
from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    TITULO_JOGO,
    BRANCO,
    PRETO,
    X_ESTRADA,
    LARGURA_ESTRADA,
    COMPRIMENTO_LINHA,
    ESPACO_LINHA,
    VELOCIDADE_PISTA,
    LARGURA_OBSTACULO,
    ALTURA_OBSTACULO,
    VELOCIDADE_OBSTACULO,
    INTERVALO_SPAWN,
    LIMIARES_NIVEL,
    INCREMENTO_VELOCIDADE,
    VELOCIDADE_OBSTACULO_MAX,
    DECREMENTO_INTERVALO,
    INTERVALO_SPAWN_MIN,
    NIVEL_MIN_SPAWN_DUPLO,
    CHANCE_SPAWN_DUPLO,
    FOLGA_MINIMA_PASSAGEM,
    GRAMA_CLARA,
    GRAMA_ESCURA,
    ASFALTO_CLARO,
    ASFALTO_ESCURO,
    VERMELHO_OBSTACULO,
)
from src.sprites import obter_sprite_obstaculo, desenhar_obstaculo_fallback

# Cache do fundo de grama
_FUNDO_GRAMA = None


def criar_tela():
    """Cria a janela principal do jogo (chamar uma única vez)."""
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    return tela


def obter_limites_pista():
    """Bordas da área jogável: (esq, dir, cima, baixo)."""
    return (X_ESTRADA, X_ESTRADA + LARGURA_ESTRADA, 0, ALTURA_TELA)


def calcular_nivel(pontos):
    """Nível atual a partir dos pontos, segundo LIMIARES_NIVEL."""
    nivel = 0
    for indice, limiar in enumerate(LIMIARES_NIVEL):
        if pontos >= limiar:
            nivel = indice
        else:
            break
    return nivel


def calcular_dificuldade(pontos):
    """Retorna (velocidade, intervalo_spawn) dos obstáculos para o nível atual."""
    nivel = calcular_nivel(pontos)

    velocidade = min(VELOCIDADE_OBSTACULO + nivel * INCREMENTO_VELOCIDADE, VELOCIDADE_OBSTACULO_MAX)
    intervalo = max(INTERVALO_SPAWN - nivel * DECREMENTO_INTERVALO, INTERVALO_SPAWN_MIN)

    return velocidade, intervalo


def atualizar_pista(deslocamento_linhas):
    """Avança o deslocamento das faixas centrais (animação de rolagem)."""
    deslocamento_linhas += VELOCIDADE_PISTA
    if deslocamento_linhas >= COMPRIMENTO_LINHA + ESPACO_LINHA:
        deslocamento_linhas = 0
    return deslocamento_linhas


def _construir_fundo_grama():
    """Gera (uma vez) a textura de grama em faixas horizontais alternadas."""
    largura_grama = X_ESTRADA
    superficie = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
    superficie.fill(GRAMA_CLARA)

    faixa_altura = 40
    for y in range(0, ALTURA_TELA, faixa_altura):
        cor = GRAMA_ESCURA if (y // faixa_altura) % 2 == 0 else GRAMA_CLARA
        pygame.draw.rect(superficie, cor, (0, y, largura_grama, faixa_altura))
        pygame.draw.rect(
            superficie, cor, (X_ESTRADA + LARGURA_ESTRADA, y, largura_grama, faixa_altura)
        )
    return superficie


def desenhar_pista(tela, deslocamento_linhas):
    """Renderiza grama, asfalto, acostamentos, faixas centrais e vinheta."""
    global _FUNDO_GRAMA
    if _FUNDO_GRAMA is None:
        _FUNDO_GRAMA = _construir_fundo_grama()
    tela.blit(_FUNDO_GRAMA, (0, 0))

    for i in range(LARGURA_ESTRADA):
        t = i / LARGURA_ESTRADA
        fator = 1 - abs(t - 0.5) * 2
        cor = [
            int(ASFALTO_ESCURO[c] + (ASFALTO_CLARO[c] - ASFALTO_ESCURO[c]) * fator)
            for c in range(3)
        ]
        pygame.draw.line(tela, cor, (X_ESTRADA + i, 0), (X_ESTRADA + i, ALTURA_TELA))

    largura_acostamento = 6
    tam_segmento = 24
    for borda_x in (X_ESTRADA - largura_acostamento, X_ESTRADA + LARGURA_ESTRADA):
        y = -tam_segmento + (deslocamento_linhas % (tam_segmento * 2))
        indice = 0
        while y < ALTURA_TELA:
            cor = BRANCO if indice % 2 == 0 else VERMELHO_OBSTACULO
            pygame.draw.rect(tela, cor, (borda_x, int(y), largura_acostamento, tam_segmento))
            y += tam_segmento
            indice += 1

    pygame.draw.line(tela, PRETO, (X_ESTRADA, 0), (X_ESTRADA, ALTURA_TELA), 4)
    pygame.draw.line(tela, PRETO, (X_ESTRADA + LARGURA_ESTRADA, 0), (X_ESTRADA + LARGURA_ESTRADA, ALTURA_TELA), 4)

    y = -(COMPRIMENTO_LINHA + ESPACO_LINHA) + deslocamento_linhas
    while y < ALTURA_TELA:
        largura_faixa = 8
        x_faixa = (LARGURA_TELA // 2) - (largura_faixa // 2)
        faixa_rect = pygame.Rect(x_faixa, int(y), largura_faixa, COMPRIMENTO_LINHA)
        pygame.draw.rect(tela, (255, 221, 90), faixa_rect, border_radius=3)
        y += COMPRIMENTO_LINHA + ESPACO_LINHA

    sombra_topo = pygame.Surface((LARGURA_TELA, 50), pygame.SRCALPHA)
    sombra_topo.fill((0, 0, 0, 70))
    tela.blit(sombra_topo, (0, 0))
    sombra_base = pygame.Surface((LARGURA_TELA, 50), pygame.SRCALPHA)
    sombra_base.fill((0, 0, 0, 70))
    tela.blit(sombra_base, (0, ALTURA_TELA - 50))


def criar_obstaculo(velocidade_obstaculo):
    """Novo obstáculo em x aleatório dentro da pista, nascendo acima da tela."""
    x_min = X_ESTRADA
    x_max = X_ESTRADA + LARGURA_ESTRADA - LARGURA_OBSTACULO
    x = random.randint(x_min, x_max)
    return {
        "rect": pygame.Rect(x, -ALTURA_OBSTACULO, LARGURA_OBSTACULO, ALTURA_OBSTACULO),
        "velocidade": velocidade_obstaculo,
    }


def criar_par_obstaculos(velocidade_obstaculo):
    """Dois obstáculos lado a lado com passagem mínima garantida entre eles."""
    largura_util = LARGURA_ESTRADA - LARGURA_OBSTACULO
    metade = largura_util // 2

    x_esq = X_ESTRADA + random.randint(0, metade)
    x_dir = X_ESTRADA + random.randint(metade, largura_util)

    distancia_atual = x_dir - (x_esq + LARGURA_OBSTACULO)
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
    """Move obstáculos, remove os que saíram da tela e gera novos por nível."""
    velocidade_atual, intervalo_atual = calcular_dificuldade(pontos)
    nivel_atual = calcular_nivel(pontos)

    for obstaculo in obstaculos:
        obstaculo["rect"].y += obstaculo["velocidade"]

    obstaculos = [o for o in obstaculos if o["rect"].top < ALTURA_TELA]

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
    """Renderiza cada obstáculo (sprite ou fallback vetorial) com sombra."""
    sprite = obter_sprite_obstaculo()
    for obstaculo in obstaculos:
        sombra = obstaculo["rect"].copy()
        sombra.y += 6
        sombra_surf = pygame.Surface(sombra.size, pygame.SRCALPHA)
        pygame.draw.ellipse(sombra_surf, (0, 0, 0, 90), sombra_surf.get_rect())
        tela.blit(sombra_surf, sombra.topleft)

        if sprite is not None:
            tela.blit(sprite, obstaculo["rect"])
        else:
            desenhar_obstaculo_fallback(tela, obstaculo["rect"])


def obter_hitboxes_obstaculos(obstaculos):
    """Lista de pygame.Rect dos obstáculos, para checagem de colisão."""
    return [o["rect"] for o in obstaculos]
