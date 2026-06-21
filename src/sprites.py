import os
import pygame


def pegar_sprite(caminho_spritesheet, x, y, width, height, scale=1.0):
    """Retorna uma Surface recortada do spritesheet.

    Se o arquivo não existir, retorna uma surface placeholder com o tamanho pedido.
    """
    try:
        if os.path.exists(caminho_spritesheet):
            sheet = pygame.image.load(caminho_spritesheet).convert_alpha()
            rect = pygame.Rect(x, y, width, height)
            imagem = sheet.subsurface(rect).copy()
        else:
            imagem = pygame.Surface((width, height), pygame.SRCALPHA)
            imagem.fill((150, 150, 150))

        if scale != 1.0:
            nova_larg = max(1, int(width * scale))
            nova_alt = max(1, int(height * scale))
            imagem = pygame.transform.smoothscale(imagem, (nova_larg, nova_alt))

        return imagem
    except Exception:
        # fallback simples
        surf = pygame.Surface((max(1, int(width * scale)), max(1, int(height * scale))), pygame.SRCALPHA)
        surf.fill((200, 50, 50))
        return surf
