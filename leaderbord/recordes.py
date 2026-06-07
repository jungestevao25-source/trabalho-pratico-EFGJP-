import csv
import os
import pygame

pygame.init()

tela  = pygame.display.set_mode((400, 500))
clock = pygame.time.Clock()
fonte = pygame.font.SysFont("Arial", 28)


def salvar(lista):
    with open("recordes.csv", "w", newline="") as arquivo:
        colunas = ["nome", "pontos"]
        writer  = csv.DictWriter(arquivo, fieldnames=colunas)
        writer.writeheader()
        writer.writerows(lista)


def carregar():
    if not os.path.exists("recordes.csv"):
        return []
    with open("recordes.csv", "r") as arquivo:
        reader = csv.DictReader(arquivo)
        lista  = []
        for linha in reader:
            jogador = {"nome": linha["nome"], "pontos": int(linha["pontos"])}
            lista.append(jogador)
        return lista


def atualizar(jogadores_de_agora):
    historico = carregar()
    todos     = historico + jogadores_de_agora
    todos.sort(key=lambda j: j["pontos"], reverse=True)
    top5      = todos[:5]
    salvar(top5)
    return top5


def mostrar(jogadores_de_agora):
    top5 = atualizar(jogadores_de_agora)

    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return
            if ev.type == pygame.KEYDOWN:
                return

        tela.fill((0, 0, 0))

        for i, j in enumerate(top5):
            texto = f"{i+1}. {j['nome']} - {j['pontos']}"
            img   = fonte.render(texto, True, (255, 255, 255))
            tela.blit(img, (30, 80 + i * 50))

        pygame.display.flip()
        clock.tick(60)

jogadores = [
    {"nome": "Carlos",  "pontos": 2000},
    {"nome": "Beatriz", "pontos": 1500},
    {"nome": "Marcos",  "pontos": 800},
]

mostrar(jogadores)

pygame.quit()