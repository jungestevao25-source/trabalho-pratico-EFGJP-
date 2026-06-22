"""Testes da pista: níveis de dificuldade, geração de obstáculos e animação."""

import pygame
import pytest

from src import street


# Dificuldade e progressão de nível

@pytest.mark.parametrize("pontos, nivel_esperado", [
    (0, 0),
    (9, 0),
    (10, 1),
    (19, 1),
    (20, 2),
    (279, 9),
    (280, 10),
    (10_000, 10),  # nunca ultrapassa o último nível definido
])
def test_calcular_nivel(pontos, nivel_esperado):
    assert street.calcular_nivel(pontos) == nivel_esperado


def test_calcular_dificuldade_aumenta_com_o_nivel():
    velocidade_inicial, intervalo_inicial = street.calcular_dificuldade(0)
    velocidade_final, intervalo_final = street.calcular_dificuldade(280)

    assert velocidade_final > velocidade_inicial
    assert intervalo_final < intervalo_inicial


def test_calcular_dificuldade_respeita_teto_e_piso():
    velocidade, intervalo = street.calcular_dificuldade(999_999)
    assert velocidade <= street.VELOCIDADE_OBSTACULO_MAX
    assert intervalo >= street.INTERVALO_SPAWN_MIN


# Pista e limites

def test_obter_limites_pista():
    assert street.obter_limites_pista() == (
        street.X_ESTRADA,
        street.X_ESTRADA + street.LARGURA_ESTRADA,
        0,
        street.ALTURA_TELA,
    )


def test_atualizar_pista_incrementa_o_deslocamento():
    assert street.atualizar_pista(0) == street.VELOCIDADE_PISTA


def test_atualizar_pista_reinicia_ao_completar_um_ciclo():
    limite_ciclo = street.COMPRIMENTO_LINHA + street.ESPACO_LINHA
    assert street.atualizar_pista(limite_ciclo - 1) == 0


# Criação de obstáculos

def test_criar_obstaculo_fica_dentro_da_pista():
    obstaculo = street.criar_obstaculo(velocidade_obstaculo=5)
    rect = obstaculo["rect"]
    assert rect.left >= street.X_ESTRADA
    assert rect.right <= street.X_ESTRADA + street.LARGURA_ESTRADA
    assert obstaculo["velocidade"] == 5


def test_criar_par_obstaculos_fica_dentro_da_pista():
    for obstaculo in street.criar_par_obstaculos(velocidade_obstaculo=6):
        rect = obstaculo["rect"]
        assert rect.left >= street.X_ESTRADA
        assert rect.right <= street.X_ESTRADA + street.LARGURA_ESTRADA


def test_criar_par_obstaculos_respeita_folga_minima():
    # roda várias vezes para cobrir a aleatoriedade das posições geradas
    for _ in range(50):
        esquerdo, direito = sorted(
            street.criar_par_obstaculos(velocidade_obstaculo=6),
            key=lambda o: o["rect"].left,
        )
        distancia = direito["rect"].left - esquerdo["rect"].right
        assert distancia >= street.FOLGA_MINIMA_PASSAGEM


# Atualização de obstáculos (movimento, remoção e spawn)

def test_atualizar_obstaculos_move_para_baixo():
    obstaculos = [{"rect": pygame.Rect(100, 0, 70, 100), "velocidade": 5}]
    obstaculos, _ = street.atualizar_obstaculos(obstaculos, contador_spawn=0, pontos=0)
    assert obstaculos[0]["rect"].y == 5


def test_atualizar_obstaculos_remove_os_que_saem_da_tela():
    obstaculos = [{"rect": pygame.Rect(100, street.ALTURA_TELA + 1, 70, 100), "velocidade": 5}]
    obstaculos, _ = street.atualizar_obstaculos(obstaculos, contador_spawn=0, pontos=0)
    assert obstaculos == []


def test_atualizar_obstaculos_incrementa_contador_sem_atingir_intervalo():
    _, intervalo = street.calcular_dificuldade(0)
    obstaculos, contador = street.atualizar_obstaculos([], contador_spawn=0, pontos=0)
    assert contador == 1
    assert obstaculos == []
    assert contador < intervalo


def test_atualizar_obstaculos_gera_novo_obstaculo_ao_atingir_intervalo():
    _, intervalo = street.calcular_dificuldade(0)
    obstaculos, contador = street.atualizar_obstaculos([], intervalo - 1, pontos=0)
    assert contador == 0
    assert len(obstaculos) == 1  # nível 0 nunca gera par duplo


# Hitboxes e renderização

def test_obter_hitboxes_obstaculos():
    obstaculos = [
        {"rect": pygame.Rect(0, 0, 70, 100), "velocidade": 5},
        {"rect": pygame.Rect(50, 50, 70, 100), "velocidade": 5},
    ]
    assert street.obter_hitboxes_obstaculos(obstaculos) == [o["rect"] for o in obstaculos]


def test_desenhar_pista_nao_lanca_excecao():
    tela = pygame.display.get_surface()
    street.desenhar_pista(tela, deslocamento_linhas=0)


def test_desenhar_obstaculos_nao_lanca_excecao():
    tela = pygame.display.get_surface()
    obstaculos = [street.criar_obstaculo(5)]
    street.desenhar_obstaculos(tela, obstaculos)
