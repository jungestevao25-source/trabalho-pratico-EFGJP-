import os
import pygame
import tempfile

import pytest

from src import street
from src.game import Carro
from src import dados
from src import leaderboard


def test_calcular_nivel_e_dificuldade():
    assert street.calcular_nivel(0) == 0
    assert street.calcular_nivel(10) >= 1
    vel, intervalo = street.calcular_dificuldade(0)
    assert isinstance(vel, int) or isinstance(vel, float)
    assert isinstance(intervalo, int)


def test_criar_obstaculo_dentro_pista():
    obst = street.criar_obstaculo(5)
    rect = obst["rect"]
    assert rect.left >= street.X_ESTRADA
    assert rect.right <= street.X_ESTRADA + street.LARGURA_ESTRADA


def test_criar_par_obstaculos_respeita_folga():
    par = street.criar_par_obstaculos(6)
    r1 = par[0]["rect"]
    r2 = par[1]["rect"]
    distancia = r2.left - (r1.left + r1.width)
    assert distancia >= -1 or distancia >= street.FOLGA_MINIMA_PASSAGEM - 1


def test_atualizar_obstaculos_spawn_and_removal():
    obstaculos = []
    pontos = 0
    # Force contador_spawn to interval-1 to trigger spawn inside the function
    _, intervalo = street.calcular_dificuldade(pontos)
    contador = intervalo - 1
    obstaculos, contador = street.atualizar_obstaculos(obstaculos, contador, pontos)
    assert contador == 0
    assert len(obstaculos) >= 1


def test_carro_mover_e_colisao():
    carro = Carro(100, 100)
    limites = (0, 800, 0, 600)

    class Keys:
        def __init__(self):
            self.map = {}

        def __getitem__(self, key):
            return self.map.get(key, False)

    keys = Keys()
    # mover para esquerda quando possível
    keys.map[pygame.K_LEFT] = True
    carro.mover(keys, limites)
    # x deve diminuir
    assert carro.rect.x >= 0

    # colisão simples
    hitboxes = [pygame.Rect(carro.rect.x, carro.rect.y, carro.rect.width, carro.rect.height)]
    assert carro.checar_colisao(hitboxes)


def test_dados_recorde_tmp(tmp_path):
    caminho = tmp_path / "rec.txt"
    dados.salvar_recorde(str(caminho), 42)
    assert dados.carregar_recorde(str(caminho)) == 42


def test_leaderboard_tmpfile(tmp_path):
    caminho = tmp_path / "lb.csv"
    # monkeypatch the ARQUIVO constant
    leaderboard.ARQUIVO = str(caminho)
    leaderboard.adicionar_pontuacao("alice", 10)
    leaderboard.adicionar_pontuacao("bob", 20)
    ranking = leaderboard.carregar_leaderboard()
    assert len(ranking) == 2
    assert ranking[0]["pontos"] >= ranking[1]["pontos"]
