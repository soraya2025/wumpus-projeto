class Agente:
    def __init__(self):
        self.pos = [0, 0]
        self.flechas = 1
        self.ouro = False

    def mover(self, direcao):
        x, y = self.pos
        if direcao == "cima" and x > 0:
            self.pos[0] -= 1
        elif direcao == "baixo" and x < 3:
            self.pos[0] += 1
        elif direcao == "esquerda" and y > 0:
            self.pos[1] -= 1
        elif direcao == "direita" and y < 3:
            self.pos[1] += 1
        else:
            print("Movimento inválido!")

    def pegar_ouro(self, mundo):
        x, y = self.pos
        if mundo[x][y] == "O":
            self.ouro = True
            mundo[x][y] = "-"
            print("Você pegou o ouro!")

    def atirar(self, mundo, direcao):
        if self.flechas == 0:
            print("Sem flechas!")
            return
        x, y = self.pos
        self.flechas -= 1
        if direcao == "cima":
            for i in range(x-1, -1, -1):
                if mundo[i][y] == "W":
                    mundo[i][y] = "-"
                    print("Você matou o Wumpus!")
                    return
        elif direcao == "baixo":
            for i in range(x+1, 4):
                if mundo[i][y] == "W":
                    mundo[i][y] = "-"
                    print("Você matou o Wumpus!")
                    return
        elif direcao == "esquerda":
            for j in range(y-1, -1, -1):
                if mundo[x][j] == "W":
                    mundo[x][j] = "-"
                    print("Você matou o Wumpus!")
                    return
        elif direcao == "direita":
            for j in range(y+1, 4):
                if mundo[x][j] == "W":
                    mundo[x][j] = "-"
                    print("Você matou o Wumpus!")
                    return