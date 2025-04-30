from mundo import Mundo
from agente import Agente
from sensores import sensores

# Pergunta ao usuário o tamanho da matriz
n = int(input("Digite o tamanho da matriz (n >= 3): "))
while n < 3:
    n = int(input("Valor inválido. Digite um número >= 3: "))

ambiente = Mundo(n)
jogador = Agente()

print("Bem-vindo ao Mundo de Wumpus!")

while True:
    sensores(ambiente.matriz, jogador.pos)
    acao = input("Escolha uma ação (mover, pegar, atirar): ").lower()

    if acao == "mover":
        direcao = input("Direção (cima, baixo, esquerda, direita): ").lower()
        jogador.mover(direcao)
    elif acao == "pegar":
        jogador.pegar_ouro(ambiente.matriz)
    elif acao == "atirar":
        direcao = input("Direção para atirar (cima, baixo, esquerda, direita): ").lower()
        jogador.atirar(ambiente.matriz, direcao)
    else:
        print("Ação inválida!")

    x, y = jogador.pos
    if ambiente.matriz[x][y] == "W":
        print("Você encontrou o Wumpus! Game Over!")
        break
    if ambiente.matriz[x][y] == "P":
        print("Você caiu em um poço! Game Over!")
        break
    if jogador.ouro and jogador.pos == [0,0]:
        print("Parabéns! Você venceu com o ouro!")
        break