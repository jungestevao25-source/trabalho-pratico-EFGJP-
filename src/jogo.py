"""Ponto de entrada do TOP RACER ULTIMATE.

Controla o fluxo de telas (menu -> nomes -> partida -> leaderboard) e desenha
a UI dos menus e do HUD durante o jogo.
"""

import pygame
import sys

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    BRANCO,
    PRETO,
    VERDE,
    VERMELHO,
    CINZA,
    TITULO_JOGO,
    COR_DESTAQUE,
    COR_DESTAQUE_2,
    COR_PAINEL,
    COR_PAINEL_BORDA,
)
from src.sprites import Carro
import src.funcoes as funcoes
import src.dados as dados
import src.sounds as sounds

pygame.init()
sounds.inicializar()
FONTE_TITULO = pygame.font.Font(None, 64)
FONTE_TEXTO = pygame.font.Font(None, 48)
FONTE_PEQUENA = pygame.font.Font(None, 36)
FONTE_SCORE = pygame.font.Font(None, 28)

tela = funcoes.criar_tela()
clock = pygame.time.Clock()

estado_atual = "DIGITAR_NUM_JOGADORES"
num_jogadores = 0
nomes_jogadores = []
texto_input = ""
mensagem_erro = ""

caixa_texto = pygame.Rect(200, 300, 400, 50)

tempo_global = 0.0  # usado para animar o cursor piscante


# Funções utilitárias de desenho

def desenhar_texto(texto, fonte, cor, x, y, centralizado=True, sombra=False):
    """Renderiza texto na tela; (x, y) é o centro se centralizado, senão o topleft."""
    if sombra:
        sombra_surf = fonte.render(texto, True, (0, 0, 0))
        rect_sombra = sombra_surf.get_rect()
        if centralizado:
            rect_sombra.center = (x + 3, y + 3)
        else:
            rect_sombra.topleft = (x + 3, y + 3)
        tela.blit(sombra_surf, rect_sombra)

    superficie = fonte.render(texto, True, cor)
    retangulo = superficie.get_rect()
    if centralizado:
        retangulo.center = (x, y)
    else:
        retangulo.topleft = (x, y)
    tela.blit(superficie, retangulo)
    return retangulo


def desenhar_painel(rect, cor_fundo=COR_PAINEL, cor_borda=COR_PAINEL_BORDA, raio=16, espessura_borda=2):
    """Painel retangular semitransparente com borda arredondada."""
    superficie = pygame.Surface(rect.size, pygame.SRCALPHA)
    pygame.draw.rect(superficie, (*cor_fundo, 235), superficie.get_rect(), border_radius=raio)
    tela.blit(superficie, rect.topleft)
    pygame.draw.rect(tela, cor_borda, rect, width=espessura_borda, border_radius=raio)


def desenhar_caixa_input(rect, texto, fonte, cor_texto, ativo=True):
    """Caixa de entrada de texto com cursor piscante e clipping de overflow."""
    altura_fonte = fonte.get_height()
    padding_v = 10
    altura_minima = altura_fonte + padding_v * 2
    if rect.height < altura_minima:
        rect = pygame.Rect(rect.x, rect.y, rect.width, altura_minima)

    desenhar_painel(rect, cor_borda=COR_DESTAQUE_2 if ativo else COR_PAINEL_BORDA)

    padding_h = 16
    area_texto = rect.width - padding_h * 2
    y_text = rect.y + (rect.height - altura_fonte) // 2

    surf_texto = fonte.render(texto, True, cor_texto)
    largura_texto = surf_texto.get_width()

    area_clip = pygame.Rect(rect.x + padding_h, y_text, area_texto, altura_fonte)
    tela.set_clip(area_clip)

    if largura_texto > area_texto:
        x_blit = rect.x + padding_h - (largura_texto - area_texto)
    else:
        x_blit = rect.x + padding_h

    tela.blit(surf_texto, (x_blit, y_text))
    tela.set_clip(None)

    if ativo and int(tempo_global * 2) % 2 == 0:
        x_cursor = rect.x + padding_h + min(largura_texto, area_texto) + 3
        pygame.draw.rect(
            tela, cor_texto, (x_cursor, y_text + 2, 3, altura_fonte - 4)
        )


# Telas

def tela_leaderboard():
    """Mostra o ranking de melhores jogadores até o usuário apertar ESC."""
    rodando = True

    while rodando:
        clock.tick(FPS)

        tela.fill(PRETO)
        desenhar_texto("LEADERBOARD", FONTE_TITULO, BRANCO, LARGURA_TELA // 2, 60)

        ranking = dados.carregar_leaderboard()

        y = 140
        if not ranking:
            desenhar_texto("Nenhuma pontuação registrada ainda.", FONTE_PEQUENA, CINZA, LARGURA_TELA // 2, y)
        else:
            for i, jogador in enumerate(ranking):
                linha = f"{i + 1}.  {jogador['nome']}  -  {jogador['pontos']} pts"
                desenhar_texto(linha, FONTE_PEQUENA, BRANCO, LARGURA_TELA // 2, y)
                y += 40

        desenhar_texto("ESC para voltar", FONTE_PEQUENA, CINZA, LARGURA_TELA // 2, ALTURA_TELA - 40)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                rodando = False


def desenhar_hud(nome, pontos, nivel, intervalo_atual, contador_spawn):
    """HUD da partida: painel de nome/pontos, nível e barra de progresso de spawn."""
    barra_rect = pygame.Rect(10, 90, 220, 14)
    desenhar_painel(barra_rect, cor_fundo=(20, 20, 20), raio=8, espessura_borda=1)
    progresso = max(0.0, min(1.0, contador_spawn / max(intervalo_atual, 1)))
    interior = pygame.Rect(
        barra_rect.x + 2, barra_rect.y + 2,
        int((barra_rect.width - 4) * progresso),
        barra_rect.height - 4
    )
    pygame.draw.rect(tela, COR_DESTAQUE_2, interior, border_radius=6)

    painel_info = pygame.Rect(0, 0, 260, 78)
    desenhar_painel(painel_info, raio=0)
    desenhar_texto("Pressione ESC para encerrar sua vez", FONTE_SCORE, CINZA, 10, 14, centralizado=False)
    desenhar_texto(f"Jogador: {nome}", FONTE_SCORE, BRANCO, 10, 38, centralizado=False)
    desenhar_texto(f"Pontos: {pontos}", FONTE_SCORE, COR_DESTAQUE, 150, 38, centralizado=False)
    desenhar_texto(f"Nível {nivel}", FONTE_SCORE, COR_DESTAQUE_2, 10, 108, centralizado=False)


def desenhar_tela_colisao():
    """Overlay vermelho com "COLISÃO!" exibido por 500 ms ao fim da rodada."""
    sounds.tocar_colisao()
    overlay = pygame.Surface((LARGURA_TELA, ALTURA_TELA), pygame.SRCALPHA)
    overlay.fill((180, 0, 0, 90))
    tela.blit(overlay, (0, 0))
    desenhar_texto(
        "COLISÃO!", FONTE_TITULO, BRANCO, LARGURA_TELA // 2, ALTURA_TELA // 2, sombra=True
    )
    pygame.display.flip()
    pygame.time.wait(500)


def executar_jogo(nome):
    """Roda uma partida até a colisão ou ESC; retorna a pontuação final."""
    carro_jogador = Carro(
        funcoes.X_ESTRADA + (funcoes.LARGURA_ESTRADA - 40) // 2,
        ALTURA_TELA - 120,
    )
    deslocamento_linhas = 0
    rodando = True
    tempo_acumulado = 0.0
    pontos = 0
    obstaculos = []
    contador_spawn = 0
    nivel_anterior = 0

    clock.tick(FPS)
    global tempo_global

    sounds.iniciar_motor()

    while rodando:
        dt = clock.tick(FPS) / 1000
        tempo_acumulado += dt
        tempo_global += dt

        while tempo_acumulado >= 1:
            pontos += 1
            tempo_acumulado -= 1

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                rodando = False

        teclas = pygame.key.get_pressed()
        carro_jogador.mover(teclas, funcoes.obter_limites_pista())
        deslocamento_linhas = funcoes.atualizar_pista(deslocamento_linhas)
        obstaculos, contador_spawn = funcoes.atualizar_obstaculos(obstaculos, contador_spawn, pontos)

        _, intervalo_atual = funcoes.calcular_dificuldade(pontos)
        nivel_atual = funcoes.calcular_nivel(pontos)

        if nivel_atual != nivel_anterior:
            sounds.tocar_level_up()
            nivel_anterior = nivel_atual

        sounds.atualizar_volume_motor(pontos)

        funcoes.desenhar_pista(tela, deslocamento_linhas)
        funcoes.desenhar_obstaculos(tela, obstaculos)
        carro_jogador.desenhar(tela)

        if carro_jogador.checar_colisao(funcoes.obter_hitboxes_obstaculos(obstaculos)):
            desenhar_tela_colisao()
            rodando = False

        desenhar_hud(nome, pontos, nivel_atual, intervalo_atual, contador_spawn)

        pygame.display.flip()

    sounds.parar_motor()
    return pontos


# Loop principal

rodando = True
while rodando:
    dt = clock.tick(FPS) / 1000
    tempo_global += dt

    tela.fill(PRETO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            sounds.parar_tudo()
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if estado_atual == "DIGITAR_NUM_JOGADORES":
                if evento.key == pygame.K_TAB:
                    tela_leaderboard()
                elif evento.key == pygame.K_RETURN:
                    if texto_input.isdigit() and int(texto_input) > 0:
                        sounds.tocar_menu_confirm()
                        num_jogadores = int(texto_input)
                        estado_atual = "DIGITAR_NOMES"
                        texto_input = ""
                        mensagem_erro = ""
                    else:
                        mensagem_erro = "Erro: Digite um número válido maior que 0!"
                        texto_input = ""
                elif evento.key == pygame.K_BACKSPACE:
                    texto_input = texto_input[:-1]
                elif evento.unicode.isdigit():
                    if len(texto_input) < 2:
                        texto_input += evento.unicode

            elif estado_atual == "DIGITAR_NOMES":
                if evento.key == pygame.K_RETURN:
                    nome_limpo = texto_input.strip()
                    if nome_limpo != "":
                        sounds.tocar_menu_confirm()
                        nomes_jogadores.append(nome_limpo)
                        texto_input = ""
                        if len(nomes_jogadores) == num_jogadores:
                            for jogador in nomes_jogadores:
                                pontos = executar_jogo(jogador)
                                dados.adicionar_pontuacao(jogador, pontos)
                                tela_leaderboard()

                            texto_input = ""
                            estado_atual = "DIGITAR_NUM_JOGADORES"
                            num_jogadores = 0
                            nomes_jogadores.clear()
                elif evento.key == pygame.K_BACKSPACE:
                    texto_input = texto_input[:-1]
                else:
                    if len(texto_input) < 15:
                        texto_input += evento.unicode

    desenhar_texto(TITULO_JOGO, FONTE_TITULO, BRANCO, LARGURA_TELA // 2, 100)

    if estado_atual == "DIGITAR_NUM_JOGADORES":
        desenhar_texto("Quantos jogadores vão competir?", FONTE_TEXTO, CINZA, LARGURA_TELA // 2, 220)

        caixa_texto = pygame.Rect(0, 0, 200, 60)
        caixa_texto.center = (LARGURA_TELA // 2, 310)
        desenhar_caixa_input(caixa_texto, texto_input, FONTE_TEXTO, VERDE)

        desenhar_texto("ENTER para confirmar  |  TAB para o leaderboard", FONTE_PEQUENA, CINZA, LARGURA_TELA // 2, 390)

        if mensagem_erro:
            desenhar_texto(mensagem_erro, FONTE_PEQUENA, VERMELHO, LARGURA_TELA // 2, 440)

    elif estado_atual == "DIGITAR_NOMES":
        jogador_atual = len(nomes_jogadores) + 1
        desenhar_texto(f"Nome do Jogador {jogador_atual} de {num_jogadores}", FONTE_TEXTO, CINZA, LARGURA_TELA // 2, 220)

        caixa_texto = pygame.Rect(0, 0, 400, 60)
        caixa_texto.center = (LARGURA_TELA // 2, 310)
        desenhar_caixa_input(caixa_texto, texto_input, FONTE_TEXTO, VERDE)

        desenhar_texto("ENTER para confirmar", FONTE_PEQUENA, CINZA, LARGURA_TELA // 2, 390)

    pygame.display.flip()
