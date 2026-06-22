# TOP RACER ULTIMATE

Jogo de corrida top-down desenvolvido em Python com Pygame como projeto prático da disciplina.

O jogador controla um veículo em uma pista vista de cima e deve desviar de obstáculos pelo maior tempo possível. A dificuldade aumenta progressivamente: obstáculos surgem mais rápido e em maior número à medida que a pontuação cresce.

---

## Como rodar

**1. Instale as dependências** (recomendado criar um ambiente virtual):

```bash
pip install -r requirements.txt
```

**2. Execute o jogo a partir da raiz do projeto:**

```bash
python main.py
```

---

## Controles

| Tecla | Ação |
|---|---|
| ↑ Seta para cima | Mover para frente |
| ↓ Seta para baixo | Mover para trás |
| ← Seta para esquerda | Mover para a esquerda |
| → Seta para direita | Mover para a direita |
| ESC | Encerrar a rodada atual |
| TAB (no menu) | Ver o leaderboard |

---

## Regras

- O jogador acumula **1 ponto por segundo** sobrevivido.
- Colidir com um obstáculo **encerra a rodada** e registra a pontuação.
- Suporte a múltiplos jogadores em sequência: cada um joga sua rodada e o ranking é atualizado ao final.
- O leaderboard mantém os **10 melhores tempos** em `data/leaderboard.csv`.

---

## Estrutura do projeto

```
TOP_RACER_ULTIMATE/
├── main.py                  # Ponto de entrada: menus, HUD e fluxo de telas
├── requirements.txt         # Dependências (pygame, pytest)
├── pytest.ini               # Configuração do pytest
├── .gitignore
│
├── src/                     # Módulos do jogo
│   ├── config.py            # Constantes globais (tela, FPS, cores, assets)
│   ├── game.py              # Classe Carro (movimentação, colisão, sprite)
│   ├── street.py            # Pista, obstáculos e dificuldade progressiva
│   ├── leaderboard.py       # Persistência do ranking em CSV
│   └── sounds.py            # Efeitos sonoros (motor, colisão, level up, menu)
│
├── tests/                   # Testes automatizados (pytest)
│   ├── conftest.py          # Fixtures: pygame headless, sys.path, cwd
│   ├── test_config.py       # Valida constantes de configuração
│   ├── test_game.py         # Testa classe Carro
│   ├── test_leaderboard.py  # Testa persistência do leaderboard
│   └── test_street.py       # Testa pista, obstáculos e dificuldade
│
├── assets/
│   ├── imagens/
│   │   ├── carro_jogador.png
│   │   └── carro_obstaculo.png
│   ├── sons/                # Efeitos sonoros gerados sinteticamente (domínio público)
│   │   ├── motor.wav        # Loop de motor (harmônicos graves + ruído)
│   │   ├── colisao.wav      # Impacto ao bater em obstáculo
│   │   ├── level_up.wav     # Jingle de subida de nível (C5→E5→G5)
│   │   └── menu_confirm.wav # Clique de confirmação nos menus
│   └── fontes/              # Reservado para expansão futura
│
├── data/
│   └── leaderboard.csv      # Gerado automaticamente na primeira partida
│
└── docs/
    └── proposta.MD          # Proposta inicial do jogo (Semana 1)
```

---

## Testes

Execute a suíte completa de testes a partir da raiz do projeto:

```bash
python -m pytest
```

Para ver detalhes por teste:

```bash
python -m pytest -v
```

Os testes rodam em modo headless (sem abrir janela) e usam arquivos temporários — não afetam o leaderboard real.

---

## Dependências

- **pygame** — janela, eventos, renderização e controles
- **pytest** — execução dos testes automatizados

---

## Origem dos assets

| Asset | Origem | Licença |
|---|---|---|
| `assets/imagens/carro_jogador.png` | Banco de imagens gratuito para uso não-comercial | docs/license-jogo-de-três-carros-em-quatro-cores-diferentes-do-vetor-isolado-objetos-985770.pdf |
| `assets/imagens/carro_obstaculo.png` | Banco de imagens gratuito para uso não-comercial | docs/license-jogo-de-três-carros-em-quatro-cores-diferentes-do-vetor-isolado-objetos-985770.pdf |
| `assets/sons/motor.wav` | Criado pelo grupo pelo FL Studio | Autoria própria |
| `assets/sons/colisao.wav` | Criado pelo grupo pelo FL Studio | Autoria própria |
| `assets/sons/level_up.wav` | Criado pelo grupo pelo FL Studio | Autoria própria |
| `assets/sons/menu_confirm.wav` | Criado pelo grupo pelo FL Studio | Autoria própria |

Os sons foram criados pelo grupo no FL Studio — não há dependência de bibliotecas de áudio externas nem de arquivos de terceiros.

---

## Integrantes

- Estevão de Castro Jung
- Fernando Pereira de Vasconcellos
- Guilherme Gonçalves Meireles
- João Pedro Spósito Pereira Cézar
- Paulo Henrique Pereira de Sousa
