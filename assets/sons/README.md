# Sons (`assets/sons/`)

Pasta com os efeitos sonoros do jogo.

## Conteúdo atual

| Arquivo | Uso no jogo | Técnica de síntese |
|---|---|---|
| `motor.wav` | Loop contínuo durante a partida; volume cresce com a pontuação | Soma de harmônicos senoidais graves (85 Hz × 1–6) + ruído passa-baixa |
| `colisao.wav` | Toca ao colidir com um obstáculo | Bump grave (60/120 Hz) com decay exponencial + burst de ruído |
| `level_up.wav` | Toca ao subir de nível | Três notas ascendentes (C5 → E5 → G5) com envelope exponencial |
| `menu_confirm.wav` | Toca ao confirmar número de jogadores ou nome no menu | Tom agudo (880/1320 Hz) com decay rápido |

## Origem

**Todos os sons foram gerados sinteticamente pelo grupo apartir do criador de música FL Studio**, sem uso de arquivos ou bibliotecas de áudio externas. Não há assets de terceiros nesta pasta.
## Licença

Por serem gerados pelo grupo, os arquivos de som são de **autoria própria** — não há restrições de uso, distribuição ou modificação.
