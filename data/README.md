# Dados (`data/`)

Esta pasta guarda arquivos de persistência simples em texto.

## Arquivos

- `leaderboard.csv`: ranking persistente gerado automaticamente pelo jogo, com campos `nome` e `pontos` ordenados do maior para o menor (top 10). Este arquivo é criado na primeira partida e **não é versionado** (ver `.gitignore`).
- `.gitkeep`: arquivo vazio que mantém esta pasta rastreada pelo Git mesmo sem o CSV.

## Observação

Evite versionar dados pessoais reais dos jogadores.
