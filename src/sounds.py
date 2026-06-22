"""Gerenciamento de sons do jogo - VERSÃO SIMPLIFICADA.

Fácil de modificar: adicione/remova sons no dicionário SONS abaixo!
"""

import os
import pygame

SONS = {
    "motor":         ("motor.wav", 0.45, True),       # Loop contínuo
    "colisao":       ("colisao.wav", 0.80, False),    # Toca uma vez
    "level_up":      ("level_up.wav", 0.65, False),   # Toca uma vez
    "menu_confirm":  ("menu_confirm.wav", 0.50, False),  # Toca uma vez
}

# Configuração de canal para sons de loop
CANAL_MOTOR = 0

# Configuração do mixer
MIXER_CONFIG = {
    "frequency": 44100,
    "size": -16,
    "channels": 1,
    "buffer": 512,
    "num_channels": 8,
}

_RAIZ = os.path.join(os.path.dirname(__file__), "..", "assets", "sons")
_disponivel = False
_sons_carregados = {}


def inicializar() -> None:
    """Inicializa o mixer e carrega todos os sons do dicionário SONS."""
    global _disponivel, _sons_carregados

    try:
        if not pygame.mixer.get_init():
            pygame.mixer.init(**MIXER_CONFIG)
        else:
            pygame.mixer.set_num_channels(MIXER_CONFIG["num_channels"])

        # Carrega todos os sons do dicionário
        for nome_som, (arquivo, volume, _) in SONS.items():
            caminho = os.path.join(_RAIZ, arquivo)
            if os.path.exists(caminho):
                som = pygame.mixer.Sound(caminho)
                som.set_volume(volume)
                _sons_carregados[nome_som] = som
            else:
                _sons_carregados[nome_som] = None

        _disponivel = True

    except Exception:
        _disponivel = False


def _tocar(nome_som: str, loop: bool = False) -> None:
    """Toca um som pelo nome (uso interno)."""
    if not _disponivel or nome_som not in _sons_carregados:
        return
    
    som = _sons_carregados[nome_som]
    if som is None:
        return

    if loop:
        canal = pygame.mixer.Channel(CANAL_MOTOR)
        if not canal.get_busy():
            canal.play(som, loops=-1, fade_ms=200)
    else:
        som.play()


def iniciar_motor() -> None:
    """Inicia o loop de som de motor."""
    _tocar("motor", loop=True)


def parar_motor(fade_ms: int = 300) -> None:
    """Para o loop do motor com fade out."""
    if not _disponivel:
        return
    pygame.mixer.Channel(CANAL_MOTOR).fadeout(fade_ms)


def atualizar_volume_motor(pontos: int, pontos_max: int = 280) -> None:
    """Aumenta o volume do motor conforme a pontuação cresce."""
    if not _disponivel or "motor" not in _sons_carregados:
        return
    t = min(pontos / max(pontos_max, 1), 1.0)
    volume = 0.45 + 0.30 * t  # 0.45 → 0.75
    pygame.mixer.Channel(CANAL_MOTOR).set_volume(volume)


def tocar_colisao() -> None:
    """Toca o efeito de colisão e para o motor."""
    parar_motor(fade_ms=50)
    _tocar("colisao")


def tocar_level_up() -> None:
    """Toca o jingle de subida de nível."""
    _tocar("level_up")


def tocar_menu_confirm() -> None:
    """Toca o clique de confirmação nos menus."""
    _tocar("menu_confirm")


def parar_tudo() -> None:
    """Para todos os sons (usar ao sair do jogo)."""
    if _disponivel:
        pygame.mixer.stop()
