"""Persistência do placar de líderes (top 10) em data/leaderboard.csv."""

import csv
import os

ARQUIVO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "leaderboard.csv"))


def carregar_leaderboard():
    """Lê o CSV e retorna a lista de pontuações (lista vazia se não existir)."""
    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, newline='', encoding='utf-8') as f:
        return [
            {"nome": linha["nome"], "pontos": int(linha["pontos"])}
            for linha in csv.DictReader(f)
        ]


def salvar_leaderboard(leaderboard):
    """Sobrescreve o CSV com a lista de pontuações fornecida."""
    with open(ARQUIVO, "w", newline='', encoding='utf-8') as f:
        escritor = csv.DictWriter(f, fieldnames=["nome", "pontos"])
        escritor.writeheader()
        escritor.writerows(leaderboard)


def adicionar_pontuacao(nome, pontos):
    """Insere uma pontuação, reordena e mantém apenas o top 10."""
    leaderboard = carregar_leaderboard()
    leaderboard.append({"nome": nome, "pontos": pontos})
    leaderboard = sorted(leaderboard, key=lambda x: x["pontos"], reverse=True)[:10]
    salvar_leaderboard(leaderboard)
