"""Alias de compatibilidade: re-exporta Carro e constantes de sprites/config.

Os testes importam `from src.game import Carro, LARGURA_CARRO, ALTURA_CARRO`.
A implementação real está em src/sprites.py e src/config.py.
"""

from src.sprites import Carro, obter_sprite_obstaculo, desenhar_obstaculo_fallback  # noqa: F401
from src.config import LARGURA_CARRO, ALTURA_CARRO  # noqa: F401
