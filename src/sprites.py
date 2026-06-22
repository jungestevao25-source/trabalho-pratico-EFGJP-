"""Carregamento de sprites e classe Carro: sprite, movimentação, hitbox de colisão e renderização."""

import pygame
from src.config import (
    CAMINHO_SPRITE_JOGADOR,
    CAMINHO_SPRITE_OBSTACULO,
    LARGURA_CARRO,
    ALTURA_CARRO,
    LARGURA_OBSTACULO,
    ALTURA_OBSTACULO,
)

# Cache de sprites
_SPRITE_OBSTACULO = None
_SPRITE_OBSTACULO_OK = True


class Carro:
    """Carro controlado pelo jogador."""

    _sprite_base = None  # cache compartilhado entre instâncias

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
        """Move o carro conforme as teclas pressionadas, sem sair da pista."""
        limite_esq, limite_dir, limite_cima, limite_baixo = limite_pista

        if teclas[pygame.K_LEFT] and self.rect.left > limite_esq:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.rect.right < limite_dir:
            self.rect.x += self.velocidade
        if teclas[pygame.K_UP] and self.rect.top > limite_cima:
            self.rect.y -= self.velocidade
        if teclas[pygame.K_DOWN] and self.rect.bottom < limite_baixo:
            self.rect.y += self.velocidade

    def _hitbox(self):
        """Rect encolhido para alinhar a colisão ao contorno visível do carro."""
        margem_x, margem_y = 10, 8
        return pygame.Rect(
            self.rect.x + margem_x,
            self.rect.y + margem_y,
            self.rect.width - margem_x * 2,
            self.rect.height - margem_y * 2,
        )

    def checar_colisao(self, hitboxes_obstaculos):
        """True se a hitbox do carro tocar a de algum obstáculo."""
        hitbox = self._hitbox()
        margem_obs = 8
        hitboxes_reduzidas = [
            pygame.Rect(
                r.x + margem_obs, r.y + margem_obs,
                r.width - margem_obs * 2, r.height - margem_obs * 2,
            )
            for r in hitboxes_obstaculos
        ]
        return hitbox.collidelist(hitboxes_reduzidas) != -1

    def desenhar(self, tela):
        tela.blit(self.sprite, self.rect)


def obter_sprite_obstaculo():
    """Carrega (com cache) o sprite do obstáculo; None se falhar."""
    global _SPRITE_OBSTACULO, _SPRITE_OBSTACULO_OK
    if _SPRITE_OBSTACULO is None and _SPRITE_OBSTACULO_OK:
        try:
            imagem = pygame.image.load(CAMINHO_SPRITE_OBSTACULO).convert_alpha()
            _SPRITE_OBSTACULO = pygame.transform.smoothscale(
                imagem, (LARGURA_OBSTACULO, ALTURA_OBSTACULO)
            )
        except Exception:
            _SPRITE_OBSTACULO_OK = False
    return _SPRITE_OBSTACULO


def desenhar_obstaculo_fallback(tela, rect, cor_obstaculo=(200, 30, 30)):
    """Carro obstáculo vetorial, usado quando o sprite não carrega."""
    pygame.draw.rect(tela, cor_obstaculo, rect, border_radius=10)
    pygame.draw.rect(tela, (255, 255, 255), rect, width=2, border_radius=10)

    parabrisa = pygame.Rect(rect.x + 12, rect.y + 14, rect.width - 24, 26)
    pygame.draw.rect(tela, (40, 40, 60), parabrisa, border_radius=6)

    farol_largura = 12
    pygame.draw.rect(tela, (255, 230, 150), (rect.x + 6, rect.bottom - 14, farol_largura, 8), border_radius=3)
    pygame.draw.rect(tela, (255, 230, 150), (rect.right - 18, rect.bottom - 14, farol_largura, 8), border_radius=3)
