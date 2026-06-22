# Testes

Suíte de testes automatizados (pytest) do projeto, organizada em um arquivo
por módulo de `src/`.

## Arquivos

- `conftest.py`: fixtures compartilhadas — inicializa o pygame em modo
  headless (driver `dummy`) e garante que os imports e os caminhos relativos
  de assets funcionem independente de onde o pytest for chamado.
- `test_config.py`: valida as constantes em `src/config.py` (dimensões, cores, caminhos de assets).
- `test_game.py`: testa a classe `Carro` (posição, movimentação, limites da pista, colisão).
- `test_leaderboard.py`: testa a persistência do placar em `src/leaderboard.py` (CSV temporário, top 10, ordenação).
- `test_street.py`: testa `src/street.py` — nível e dificuldade, geração/movimento/remoção de obstáculos, animação da pista.

`main.py` não é coberto por testes unitários: é um script que abre a janela e
roda o loop do jogo ao ser importado, sem funções isoladas para testar sem
de fato rodar a partida.

## Como executar

```bash
python -m pytest
```

Para ver a cobertura por arquivo:

```bash
python -m pytest -v
```

## Boas práticas

- Cada módulo novo em `src/` deve ganhar seu `test_<modulo>.py` correspondente.
- Testes que mexem em arquivos (ex.: leaderboard) devem usar `tmp_path` e
  `monkeypatch`, nunca o arquivo real em `data/`.
