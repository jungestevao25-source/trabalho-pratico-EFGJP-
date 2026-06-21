import pygame

def calcular_pontos(pontos_atual, ganho):
    """Retorna a soma dos pontos atuais com os pontos ganhos."""
    return pontos_atual + ganho


def jogador_perdeu(vidas):
    """Retorna True quando o jogador não tem mais vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Limita `valor` ao intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(rect_a, rect_b):
    """Verifica colisão entre dois rects do pygame.

    Accepta tanto um `pygame.Rect` quanto objetos que exponham `colliderect`.
    """
    try:
        return rect_a.colliderect(rect_b)
    except Exception:
        # Se forem listas ou retângulos simples, tente comparar via collidelist
        try:
            return rect_a.collidelist(rect_b) != -1
        except Exception:
            return False


def tomar_dano(vidas, dano=1):
    """Subtrai `dano` de `vidas` e retorna o novo total não-negativo."""
    return max(vidas - dano, 0)
