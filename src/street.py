"""Alias de compatibilidade: re-exporta funções de pista (src/funcoes.py) e
constantes de dificuldade (src/config.py).

Os testes importam `from src import street` e acessam:
  - street.calcular_nivel / calcular_dificuldade / atualizar_pista
  - street.criar_obstaculo / criar_par_obstaculos / atualizar_obstaculos
  - street.obter_limites_pista / obter_hitboxes_obstaculos
  - street.desenhar_pista / desenhar_obstaculos
  - constantes: X_ESTRADA, LARGURA_ESTRADA, ALTURA_TELA, VELOCIDADE_PISTA,
                COMPRIMENTO_LINHA, ESPACO_LINHA, VELOCIDADE_OBSTACULO_MAX,
                INTERVALO_SPAWN_MIN, FOLGA_MINIMA_PASSAGEM
"""

from src.funcoes import (  # noqa: F401
    calcular_nivel,
    calcular_dificuldade,
    atualizar_pista,
    criar_obstaculo,
    criar_par_obstaculos,
    atualizar_obstaculos,
    obter_limites_pista,
    obter_hitboxes_obstaculos,
    desenhar_pista,
    desenhar_obstaculos,
)
from src.config import (  # noqa: F401
    X_ESTRADA,
    LARGURA_ESTRADA,
    ALTURA_TELA,
    VELOCIDADE_PISTA,
    COMPRIMENTO_LINHA,
    ESPACO_LINHA,
    VELOCIDADE_OBSTACULO_MAX,
    INTERVALO_SPAWN_MIN,
    FOLGA_MINIMA_PASSAGEM,
)
