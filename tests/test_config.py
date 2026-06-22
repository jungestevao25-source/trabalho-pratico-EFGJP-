"""Testes de sanidade para as constantes de configuração do jogo."""

import os

import pytest

from src import config


def test_dimensoes_da_tela_sao_positivas():
    assert config.LARGURA_TELA > 0
    assert config.ALTURA_TELA > 0


def test_fps_e_positivo():
    assert config.FPS > 0


def test_titulo_do_jogo_nao_esta_vazio():
    assert isinstance(config.TITULO_JOGO, str)
    assert config.TITULO_JOGO.strip() != ""


@pytest.mark.parametrize("cor", [
    config.BRANCO,
    config.PRETO,
    config.CINZA,
    config.VERDE,
    config.VERMELHO,
    config.COR_DESTAQUE,
    config.COR_DESTAQUE_2,
    config.COR_PAINEL,
    config.COR_PAINEL_BORDA,
])
def test_cores_sao_tuplas_rgb_validas(cor):
    assert len(cor) == 3
    assert all(isinstance(c, int) and 0 <= c <= 255 for c in cor)


def test_caminho_sprite_jogador_existe():
    assert os.path.exists(config.CAMINHO_SPRITE_JOGADOR)


def test_caminho_sprite_obstaculo_existe():
    assert os.path.exists(config.CAMINHO_SPRITE_OBSTACULO)
