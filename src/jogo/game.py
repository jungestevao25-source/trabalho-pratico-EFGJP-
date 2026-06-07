import pygame


class Carro:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 70)
        self.cor = (0, 128, 255)
        self.velocidade = 6

    def mover(self, teclas, limite_pista):
        limite_esq, limite_dir, limite_cima, limite_baixo = limite_pista

        if teclas[pygame.K_LEFT] and self.rect.left > limite_esq:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.rect.right < limite_dir:
            self.rect.x += self.velocidade
        if teclas[pygame.K_UP] and self.rect.top > limite_cima:
            self.rect.y -= self.velocidade
        if teclas[pygame.K_DOWN] and self.rect.bottom < limite_baixo:
            self.rect.y += self.velocidade

    def checar_colisao(self, hitboxes_obstaculos):
        return self.rect.collidelist(hitboxes_obstaculos) != -1

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, self.rect)
