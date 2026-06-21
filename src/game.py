import pygame

from src.config import CAMINHO_SPRITE_JOGADOR

LARGURA_CARRO = 40
ALTURA_CARRO = 72


class Carro:
    _sprite_base = None
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, LARGURA_CARRO, ALTURA_CARRO)
        self.velocidade = 6
        self.sprite = Carro._carregar_sprite()
    
    @classmethod
    def _carregar_sprite(cls):
        if cls._sprite_base is None:
            imagem = pygame.image.load(CAMINHO_SPRITE_JOGADOR).convert_alpha()
            cls._sprite_base = pygame.transform.smoothscale(
                imagem, (LARGURA_CARRO, ALTURA_CARRO)
            )
        return cls._sprite_base

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
        tela.blit(self.sprite, self.rect)