# Projeto Mundo de Wumpus

Este repositório contém a implementação da Etapa 1 do Projeto de Desenvolvimento do jogo Mundo de Wumpus para a dicplina de Inteligência Artificial, que consiste na geração de ambientes aleatórios com interação do usuário.

## Etapa 1 - Geração do Ambiente

- Geração de uma matriz `n x n` com `n ≥ 3`.
- Posicionamento automático de poços (P), Wumpus (W) e ouro (O), com regras:
  - A célula (0,0) é a posição inicial do agente e nunca recebe objetos.
  - Objetos não se sobrepõem.
  - Ouro e Wumpus não são colocados em células com poço.
- Atribuição de percepções:
  - Brisa ao redor de poços.
  - Fedor ao redor do Wumpus.

## Arquivos principais

- `mundo.py`: cria o ambiente e posiciona os objetos.
- `agente.py`: define o agente, seus movimentos, ações e estado.
- `sensores.py`: gera percepções com base nos objetos vizinhos.
- `main.py`: integra tudo, executando o jogo por meio de interação (input do usuário).

## Execução

Para rodar o jogo localmente:

```bash
python main.py
```

Ou rode em um ambiente como Google Colab, copiando o conteúdo dos arquivos em células separadas.

##  Próximas etapas

- Etapa 2: automatizar o agente com base em regras (sem input manual).
- Etapa 3: adicionar memória e estratégia ao agente.
- Etapa 4: implementar agente com aprendizado via Algoritmo Genético.
- Etapa 5: avaliar o desempenho com gráficos e métricas.

---

PCCA 2025.
