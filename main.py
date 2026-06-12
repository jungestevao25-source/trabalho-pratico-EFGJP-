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
)
from src.game import Carro
import src.street as street

pygame.init()
FONTE_TITULO = pygame.font.Font(None, 64)
FONTE_TEXTO = pygame.font.Font(None, 48)
FONTE_PEQUENA = pygame.font.Font(None, 36)
FONTE_SCORE = pygame.font.Font(None, 28)


tela = street.criar_tela()
clock = pygame.time.Clock()

estado_atual = "DIGITAR_NUM_JOGADORES"
num_jogadores = 0
nomes_jogadores = []
texto_input = ""
mensagem_erro = ""

leaderboard = {}
caixa_texto = pygame.Rect(200, 300, 400, 50)


def desenhar_texto(texto, fonte, cor, x, y, centralizado=True):
    superficie = fonte.render(texto, True, cor)
    retangulo = superficie.get_rect()
    if centralizado:
        retangulo.center = (x, y)
    else:
        retangulo.topleft = (x, y)
    tela.blit(superficie, retangulo)


def executar_jogo(nomes):
    carro_jogador = Carro(
        street.X_ESTRADA + (street.LARGURA_ESTRADA - 40) // 2,
        ALTURA_TELA - 120,
    )
    deslocamento_linhas = 0
    rodando = True

    while rodando:
        clock.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                return
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                rodando = False
                return

        teclas = pygame.key.get_pressed()
        carro_jogador.mover(teclas, street.obter_limites_pista())
        deslocamento_linhas = street.atualizar_pista(deslocamento_linhas)

        street.desenhar_pista(tela, deslocamento_linhas)
        carro_jogador.desenhar(tela)

        desenhar_texto("Pressione ESC para sair", FONTE_SCORE, BRANCO, 10, 10, centralizado=False)
        if nomes:
            desenhar_texto(f"Jogadores: {', '.join(nomes)}", FONTE_SCORE, BRANCO, 10, 35, centralizado=False)

        pygame.display.flip()


rodando = True
while rodando:
    tela.fill(PRETO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if estado_atual == "DIGITAR_NUM_JOGADORES":
                if evento.key == pygame.K_RETURN:
                    if texto_input.isdigit() and int(texto_input) > 0:
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
                        nomes_jogadores.append(nome_limpo)
                        leaderboard[nome_limpo] = 0
                        texto_input = ""
                        if len(nomes_jogadores) == num_jogadores:
                            executar_jogo(nomes_jogadores)
                            texto_input = ""
                            estado_atual = "DIGITAR_NUM_JOGADORES"
                            num_jogadores = 0
                            nomes_jogadores.clear()
                            leaderboard.clear()
                elif evento.key == pygame.K_BACKSPACE:
                    texto_input = texto_input[:-1]
                else:
                    if len(texto_input) < 15:
                        texto_input += evento.unicode

    desenhar_texto("TÍTULO DO JOGO", FONTE_TITULO, BRANCO, LARGURA_TELA // 2, 100)

    if estado_atual == "DIGITAR_NUM_JOGADORES":
        desenhar_texto("Digite a quantidade de jogadores:", FONTE_TEXTO, CINZA, LARGURA_TELA // 2, 200)
        desenhar_texto("(Pressione ENTER para confirmar)", FONTE_PEQUENA, CINZA, LARGURA_TELA // 2, 400)

        if mensagem_erro:
            desenhar_texto(mensagem_erro, FONTE_PEQUENA, VERMELHO, LARGURA_TELA // 2, 450)

        pygame.draw.rect(tela, BRANCO, caixa_texto, 2)
        y_text = caixa_texto.y + (caixa_texto.height - FONTE_TEXTO.get_height()) // 2
        desenhar_texto(texto_input, FONTE_TEXTO, VERDE, caixa_texto.x + 10, y_text, centralizado=False)

    elif estado_atual == "DIGITAR_NOMES":
        jogador_atual = len(nomes_jogadores) + 1
        desenhar_texto(f"Digite o nome do Jogador {jogador_atual}:", FONTE_TEXTO, CINZA, LARGURA_TELA // 2, 200)
        desenhar_texto("(Pressione ENTER para confirmar)", FONTE_PEQUENA, CINZA, LARGURA_TELA // 2, 400)

        pygame.draw.rect(tela, BRANCO, caixa_texto, 2)
        y_text = caixa_texto.y + (caixa_texto.height - FONTE_TITULO.get_height()) // 2
        desenhar_texto(texto_input, FONTE_TITULO, VERDE, caixa_texto.x + 10, y_text, centralizado=False)

    pygame.display.flip()