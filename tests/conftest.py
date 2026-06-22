"""Configuração compartilhada dos testes.

Garante que:
- a raiz do projeto esteja no sys.path, para `from src import ...` funcionar
  não importa de onde o pytest seja chamado;
- o diretório de trabalho seja a raiz do projeto, já que os módulos carregam
  sprites por caminho relativo (ex.: "assets/imagens/carro_jogador.png");
- o pygame rode em modo "headless" (sem janela real), usando o driver de
  vídeo dummy do SDL — necessário em CI e em ambientes sem display.
"""

import os
import sys

RAIZ_PROJETO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ_PROJETO)
os.chdir(RAIZ_PROJETO)

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")

import pygame
import pytest


@pytest.fixture(scope="session", autouse=True)
def _pygame_headless():
    """Inicializa o pygame e cria uma superfície de tela única para a sessão."""
    pygame.init()
    pygame.display.set_mode((800, 600))
    yield
    pygame.quit()
