"""Testes da classe Carro: posição, movimentação, colisão e renderização."""

import pygame
import pytest

from src.game import Carro, LARGURA_CARRO, ALTURA_CARRO

LIMITES_PADRAO = (0, 800, 0, 600)


class TeclasFalsas:
    """Simula pygame.key.get_pressed(), permitindo escolher quais teclas
    estão "pressionadas" em um teste, sem depender de eventos reais.

    As chaves de pygame (ex.: pygame.K_LEFT) são inteiros, por isso o
    dicionário é recebido como argumento posicional, e não como **kwargs.
    """

    def __init__(self, pressionadas=None):
        self._pressionadas = pressionadas or {}

    def __getitem__(self, tecla):
        return self._pressionadas.get(tecla, False)


def test_carro_inicia_na_posicao_informada():
    carro = Carro(100, 200)
    assert carro.rect.x == 100
    assert carro.rect.y == 200
    assert carro.rect.width == LARGURA_CARRO
    assert carro.rect.height == ALTURA_CARRO


def test_carro_carrega_sprite_no_tamanho_padrao():
    carro = Carro(0, 0)
    assert carro.sprite is not None
    assert carro.sprite.get_size() == (LARGURA_CARRO, ALTURA_CARRO)


def test_sprite_e_compartilhado_entre_instancias():
    """O sprite é cacheado na classe; instâncias diferentes não recarregam o arquivo."""
    carro1 = Carro(0, 0)
    carro2 = Carro(300, 300)
    assert carro1.sprite is carro2.sprite


@pytest.mark.parametrize("tecla, eixo, sinal", [
    (pygame.K_LEFT, "x", -1),
    (pygame.K_RIGHT, "x", 1),
    (pygame.K_UP, "y", -1),
    (pygame.K_DOWN, "y", 1),
])
def test_mover_desloca_o_carro_na_direcao_esperada(tecla, eixo, sinal):
    carro = Carro(100, 100)
    valor_inicial = getattr(carro.rect, eixo)
    teclas = TeclasFalsas({tecla: True})
    carro.mover(teclas, LIMITES_PADRAO)
    assert getattr(carro.rect, eixo) == valor_inicial + sinal * carro.velocidade


def test_mover_sem_teclas_nao_altera_posicao():
    carro = Carro(100, 100)
    posicao_inicial = (carro.rect.x, carro.rect.y)
    carro.mover(TeclasFalsas(), LIMITES_PADRAO)
    assert (carro.rect.x, carro.rect.y) == posicao_inicial


def test_carro_nao_ultrapassa_limite_esquerdo():
    carro = Carro(0, 100)
    teclas = TeclasFalsas({pygame.K_LEFT: True})
    carro.mover(teclas, LIMITES_PADRAO)
    assert carro.rect.left == 0


def test_carro_nao_ultrapassa_limite_direito():
    carro = Carro(800 - LARGURA_CARRO, 100)
    teclas = TeclasFalsas({pygame.K_RIGHT: True})
    carro.mover(teclas, LIMITES_PADRAO)
    assert carro.rect.right == 800


def test_carro_nao_ultrapassa_limite_superior():
    carro = Carro(100, 0)
    teclas = TeclasFalsas({pygame.K_UP: True})
    carro.mover(teclas, LIMITES_PADRAO)
    assert carro.rect.top == 0


def test_carro_nao_ultrapassa_limite_inferior():
    carro = Carro(100, 600 - ALTURA_CARRO)
    teclas = TeclasFalsas({pygame.K_DOWN: True})
    carro.mover(teclas, LIMITES_PADRAO)
    assert carro.rect.bottom == 600


def test_checar_colisao_detecta_sobreposicao():
    carro = Carro(100, 100)
    hitboxes = [pygame.Rect(carro.rect.x, carro.rect.y, carro.rect.width, carro.rect.height)]
    assert carro.checar_colisao(hitboxes) is True


def test_checar_colisao_ignora_obstaculo_distante():
    carro = Carro(100, 100)
    hitboxes = [pygame.Rect(700, 500, 70, 100)]
    assert carro.checar_colisao(hitboxes) is False


def test_checar_colisao_com_lista_vazia():
    carro = Carro(100, 100)
    assert carro.checar_colisao([]) is False


def test_desenhar_nao_lanca_excecao():
    tela = pygame.display.get_surface()
    carro = Carro(100, 100)
    carro.desenhar(tela)
