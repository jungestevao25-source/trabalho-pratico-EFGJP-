"""Testes do módulo de sons (src/sounds.py).

Verifica que o módulo funciona corretamente em modo headless (sem
dispositivo de áudio real) e que todas as funções públicas são chamáveis
sem lançar exceção.
"""

import os
import pygame
import pytest

import src.sounds as sounds


def test_inicializar_nao_lanca_excecao():
    """sounds.inicializar() deve ser idempotente e não lançar exceção."""
    sounds.inicializar()
    sounds.inicializar()  # segunda chamada não deve falhar


def test_arquivos_de_som_existem():
    """Os quatro arquivos .wav devem estar presentes na pasta assets/sons/."""
    raiz = os.path.join(os.path.dirname(__file__), "..", "assets", "sons")
    for nome in ("motor.wav", "colisao.wav", "level_up.wav", "menu_confirm.wav"):
        assert os.path.exists(os.path.join(raiz, nome)), f"Arquivo ausente: {nome}"


def test_tocar_colisao_nao_lanca_excecao():
    sounds.tocar_colisao()


def test_tocar_level_up_nao_lanca_excecao():
    sounds.tocar_level_up()


def test_tocar_menu_confirm_nao_lanca_excecao():
    sounds.tocar_menu_confirm()


def test_iniciar_e_parar_motor_nao_lancam_excecao():
    sounds.iniciar_motor()
    sounds.parar_motor(fade_ms=0)


def test_atualizar_volume_motor_nos_extremos():
    """atualizar_volume_motor não deve lançar exceção em pontos=0 ou pontos muito altos."""
    sounds.atualizar_volume_motor(0)
    sounds.atualizar_volume_motor(999_999)


def test_parar_tudo_nao_lanca_excecao():
    sounds.parar_tudo()
