# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

> Corrida de carro

Exemplo:

Corrida dos Obstáculos

## 2. Integrantes do grupo

Liste os integrantes do grupo.

> - Estevão de Castro Jung
> - Fernando Pereira de Vasconcellos
> - Guilherme Gonçalves Meireles
> - João Pedro Spósito Pereira Cézar
> - Paulo Henrique Pereira de Sousa

## 3. Tipo de jogo

Indique o tipo de jogo que será desenvolvido.

Exemplos:

- jogo de desviar de obstáculos;
- jogo de coleta de itens;
- labirinto simples;
- jogo de perguntas e respostas;
- jogo de memória;
- Pong;
- Snake;
- Breakout;
- nave desviando de meteoros;
- corrida simples com obstáculos;
- jogo de clique rápido;
- jogo de sobrevivência simples.

Tipo escolhido pelo grupo:

> Jogo de corrida arcade de sobrevivência com rotação progressiva de cenário (Top-Down Racer).

## 4. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará.

Procure responder:

- O que aparece na tela?
- O que o jogador controla?
- O que o jogador precisa fazer?
- Quais desafios aparecem durante a partida?

Descrição:

> O jogador controla um veículo em uma pista pré-construída vista de cima. A movimentação é feita através do teclado (virar esquerda e direita). Conforme o cronômetro avança, a câmera ou o mapa inteiro começa a girar continuamente na tela, e a velocidade dessa rotação aumenta com o tempo. O desafio é adaptar a coordenação motora para dirigir corretamente, mesmo quando o mapa estiver de lado ou de cabeça para baixo

## 5. Objetivo do jogador

Explique qual é o objetivo principal do jogador.

Exemplos:

- coletar o maior número possível de itens;
- sobreviver pelo maior tempo possível;
- chegar até o final do labirinto;
- acertar alvos;
- responder perguntas corretamente;
- evitar obstáculos;
- quebrar todos os blocos.

Objetivo:

> - Ficar o maior tempo possível
> - Não atingir obstáculos
> - Manter o controle do veículo enquanto o mapa progride aumentando a dificuldade

## 6. Regras principais

Liste as principais regras do jogo.

Exemplo:

- O jogador começa com 3 vidas.
- Cada moeda coletada vale 10 pontos.
- Cada colisão com obstáculo remove 1 vida.
- A partida termina quando as vidas chegam a zero.
- O jogador vence se alcançar 100 pontos.

Regras do grupo:

> - Regra 1: O jogador começa com 3 vidas e 0 segundos no cronômetro.
> - Regra 2: A velocidade de rotação do mapa na tela é proporcional ao tempo do cronômetro (ex: a cada 10 segundos, o giro fica mais rápido).
> - Regra 3: Colidir com os obstáculos elimina uma vida
> - Regra 4: Somente um jogador joga por vez

## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

Exemplos:

- atingir determinada pontuação;
- chegar ao final da fase;
- sobreviver até o tempo acabar;
- responder uma quantidade mínima de perguntas;
- quebrar todos os blocos.

Condição de vitória:

> Ter o melhor tempo na tabela de ranking

## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

Exemplos:

- perder todas as vidas;
- acabar o tempo;
- colidir com determinado obstáculo;
- errar muitas perguntas;
- deixar a bola cair, no caso de Breakout ou Pong.

Condição de derrota ou encerramento:

> Ficar um primeiro no ranking

## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

## Jogador ou elemento principal

Exemplo:

Um personagem controlado pelas setas do teclado.

Descrição:

> - Jogador: O veículo principal que corre pela pista.

## Obstáculos, inimigos ou desafios

Exemplo:

Obstáculos aparecem em posições aleatórias e devem ser evitados.

Descrição:

> - Cenário: Um mapa pré-desenhado com obstáculos (ex: asfalto) cercado por limites rígidos (paredes ou grama)

## Itens, alvos ou objetos de interação

Exemplo:

Moedas aparecem na tela e aumentam a pontuação quando coletadas.

Descrição:

> - Progresso e HUD: Um cronômetro visível, um contador de 3 vidas (corações)

## Pontuação, vidas, tempo ou progresso

Exemplo:

O jogador começa com 3 vidas e ganha 10 pontos por item coletado.

Descrição:

> - Progresso e HUD: Um cronômetro visível, um contador de 3 vidas (corações)

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Exemplo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

Controles do grupo:

- Tecla/comando:
- Tecla/comando:
- Tecla/comando:

## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Exemplo:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

Organização planejada:

> Escreva aqui.


## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Exemplo:

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência;
- fonte personalizada.

Recursos previstos:

> Escreva aqui.

Caso não pretenda utilizar recursos externos, escreva:

> Não pretendemos utilizar recursos externos.

## 13. Principais dificuldades esperadas

Liste as dificuldades que o grupo acredita que poderá enfrentar.

Exemplos:

- movimentação do jogador;
- colisão entre objetos;
- controle de tempo;
- criação do ranking;
- organização do código;
- uso do GitHub;
- testes;
- exibição de textos na tela.

Dificuldades previstas:

- Dificuldade 1:
- Dificuldade 2:
- Dificuldade 3:

## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Exemplo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.

Escopo mínimo:

> Escreva aqui.

## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Exemplos:

- tela inicial;
- sons;
- fases;
- aumento de dificuldade;
- ranking;
- animações;
- novos tipos de obstáculos;
- diferentes personagens;
- menu de pausa.

Melhorias possíveis:

- Melhoria 1:
- Melhoria 2:
- Melhoria 3: