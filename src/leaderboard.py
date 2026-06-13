import csv
import os

ARQUIVO = "leaderboard.csv"


def carregar_leaderboard():
    leaderboard = []
    if not os.path.exists(ARQUIVO):
        return leaderboard

    with open(ARQUIVO, newline='', encoding='utf-8') as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            leaderboard.append({
                "nome": linha["nome"],
                "pontos": int(linha["pontos"])
            })
    return leaderboard


def salvar_leaderboard(leaderboard):
    with open(ARQUIVO, "w", newline='', encoding='utf-8') as f:
        campos = ["nome", "pontos"]
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        for jogador in leaderboard:
            escritor.writerow(jogador)


def adicionar_pontuacao(nome, pontos):
    leaderboard = carregar_leaderboard()
    leaderboard.append({"nome": nome, "pontos": pontos})
    leaderboard = sorted(leaderboard, key=lambda x: x["pontos"], reverse=True)
    leaderboard = leaderboard[:10]
    salvar_leaderboard(leaderboard)