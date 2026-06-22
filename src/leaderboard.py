"""Alias de compatibilidade para src/dados.py.

Os testes usam monkeypatch.setattr(leaderboard, "ARQUIVO", ...) para isolar
cada teste. Para que isso funcione, as funções precisam ler `ARQUIVO` deste
próprio módulo — não do módulo dados. Por isso duplicamos aqui a lógica de
persistência (uma única fonte de verdade continua sendo dados.py para o jogo;
para os testes, este módulo é auto-contido).
"""

import csv
import os

import src.dados as _dados

# Aponta para o mesmo arquivo padrão de dados.py.
# O monkeypatch dos testes sobrescreve este atributo neste módulo.
ARQUIVO = _dados.ARQUIVO


def carregar_leaderboard():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, newline='', encoding='utf-8') as f:
        return [
            {"nome": linha["nome"], "pontos": int(linha["pontos"])}
            for linha in csv.DictReader(f)
        ]


def salvar_leaderboard(leaderboard_data):
    with open(ARQUIVO, "w", newline='', encoding='utf-8') as f:
        escritor = csv.DictWriter(f, fieldnames=["nome", "pontos"])
        escritor.writeheader()
        escritor.writerows(leaderboard_data)


def adicionar_pontuacao(nome, pontos):
    dados = carregar_leaderboard()
    dados.append({"nome": nome, "pontos": pontos})
    dados = sorted(dados, key=lambda x: x["pontos"], reverse=True)[:10]
    salvar_leaderboard(dados)
