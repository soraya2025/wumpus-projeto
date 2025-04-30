def sensores(mundo, pos):
    x, y = pos
    mensagens = []
    vizinhos = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
    for i, j in vizinhos:
        if 0 <= i < len(mundo) and 0 <= j < len(mundo):
            if mundo[i][j] == "P":
                mensagens.append("Você sente uma brisa...")
            if mundo[i][j] == "W":
                mensagens.append("Você sente um fedor terrível...")
    for msg in mensagens:
        print(msg)