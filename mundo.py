import random

class Mundo:
    def __init__(self, n=4, qtd_pocos=3):
        self.n = n
        self.matriz = [["-" for _ in range(n)] for _ in range(n)]
        self.pocos = []

        # Adiciona poços e registra suas posições
        for _ in range(qtd_pocos):
            self.colocar_elemento("P")

        # Adiciona ouro e Wumpus, evitando posições com poços
        self.colocar_elemento("O", evitar=self.pocos)
        self.colocar_elemento("W", evitar=self.pocos)

    def colocar_elemento(self, elemento, evitar=[]):
        while True:
            x = random.randint(0, self.n - 1)
            y = random.randint(0, self.n - 1)
            if self.matriz[x][y] == "-" and (x, y) != (0, 0) and (x, y) not in evitar:
                self.matriz[x][y] = elemento
                if elemento == "P":
                    self.pocos.append((x, y))
                break

