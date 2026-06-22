"""Constantes de configuração do jogo: tela, FPS, cores e caminhos de assets."""

LARGURA_TELA = 800
ALTURA_TELA = 600
FPS = 60
TITULO_JOGO = "TOP RACER ULTIMATE"

# Paleta base
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (200, 200, 200)
VERDE = (50, 200, 50)
VERMELHO = (255, 100, 100)

# Paleta da UI (menus e HUD)
COR_DESTAQUE = (255, 196, 0)        # título e pontuação
COR_DESTAQUE_2 = (0, 224, 255)      # brilho, seleção ativa, barra de progresso
COR_PAINEL = (22, 24, 40)           # fundo dos painéis semitransparentes
COR_PAINEL_BORDA = (70, 76, 110)    # borda dos painéis

# Caminhos de assets
CAMINHO_SPRITE_JOGADOR = "assets/imagens/carro_jogador.png"
CAMINHO_SPRITE_OBSTACULO = "assets/imagens/carro_obstaculo.png"

# Estrada
LARGURA_ESTRADA = 450
X_ESTRADA = (LARGURA_TELA - LARGURA_ESTRADA) // 2
COMPRIMENTO_LINHA = 50
ESPACO_LINHA = 35
VELOCIDADE_PISTA = 8

# Obstáculos
LARGURA_OBSTACULO = 70
ALTURA_OBSTACULO = 100
VELOCIDADE_OBSTACULO = 8
INTERVALO_SPAWN = 60

# Dificuldade progressiva
LIMIARES_NIVEL = [0, 10, 20, 35, 55, 80, 110, 145, 185, 230, 280]
INCREMENTO_VELOCIDADE = 1
VELOCIDADE_OBSTACULO_MAX = 16
DECREMENTO_INTERVALO = 4
INTERVALO_SPAWN_MIN = 24
NIVEL_MIN_SPAWN_DUPLO = 2
CHANCE_SPAWN_DUPLO = 0.35
FOLGA_MINIMA_PASSAGEM = 110  # espaço mínimo entre obstáculos de um par

# Carro
LARGURA_CARRO = 70
ALTURA_CARRO = 100
VELOCIDADE_CARRO = 6

# Cores adicionais (pista)
GRAMA_CLARA = (46, 158, 64)
GRAMA_ESCURA = (32, 122, 48)
ASFALTO_CLARO = (90, 92, 100)
ASFALTO_ESCURO = (58, 60, 68)
VERMELHO_OBSTACULO = (200, 30, 30)
