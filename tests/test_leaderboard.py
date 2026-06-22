"""Testes da persistência do leaderboard em CSV."""

import pytest

from src import leaderboard


@pytest.fixture
def arquivo_isolado(tmp_path, monkeypatch):
    """Redireciona leaderboard.ARQUIVO para um CSV temporário, isolando cada teste."""
    caminho = tmp_path / "leaderboard.csv"
    monkeypatch.setattr(leaderboard, "ARQUIVO", str(caminho))
    return caminho


def test_carregar_leaderboard_sem_arquivo_retorna_lista_vazia(arquivo_isolado):
    assert leaderboard.carregar_leaderboard() == []


def test_adicionar_pontuacao_persiste_no_arquivo(arquivo_isolado):
    leaderboard.adicionar_pontuacao("alice", 50)
    assert leaderboard.carregar_leaderboard() == [{"nome": "alice", "pontos": 50}]


def test_adicionar_varias_pontuacoes_ordena_decrescente(arquivo_isolado):
    leaderboard.adicionar_pontuacao("alice", 10)
    leaderboard.adicionar_pontuacao("bob", 30)
    leaderboard.adicionar_pontuacao("carol", 20)

    ranking = leaderboard.carregar_leaderboard()
    pontos = [jogador["pontos"] for jogador in ranking]

    assert pontos == sorted(pontos, reverse=True)
    assert ranking[0]["nome"] == "bob"


def test_leaderboard_mantem_apenas_top_10(arquivo_isolado):
    for i in range(15):
        leaderboard.adicionar_pontuacao(f"jogador{i}", i)

    ranking = leaderboard.carregar_leaderboard()

    assert len(ranking) == 10
    assert ranking[0]["pontos"] == 14  # melhor pontuação no topo
    assert ranking[-1]["pontos"] == 5  # as 5 piores foram descartadas


def test_salvar_leaderboard_sobrescreve_conteudo_anterior(arquivo_isolado):
    leaderboard.salvar_leaderboard([{"nome": "x", "pontos": 1}])
    leaderboard.salvar_leaderboard([{"nome": "y", "pontos": 2}])

    assert leaderboard.carregar_leaderboard() == [{"nome": "y", "pontos": 2}]


def test_salvar_leaderboard_vazio_gera_arquivo_sem_entradas(arquivo_isolado):
    leaderboard.salvar_leaderboard([])
    assert leaderboard.carregar_leaderboard() == []
