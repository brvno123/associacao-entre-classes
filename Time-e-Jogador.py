class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

    def __str__(self):
        return f'{self.nome} - {self.posicao}'


class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def listar_jogadores(self):
        print(f"Jogadores do time {self.nome}:")
        for jogador in self.jogadores:
            print(jogador)


jogador1 = Jogador("Neymar Jr.", "Atacante")
jogador2 = Jogador("Marquinhos", "Zagueiro")
jogador3 = Jogador("Alisson Becker", "Goleiro")

jogador4 = Jogador("Cristiano Ronaldo", "Atacante")
jogador5 = Jogador("Bruno Fernandes", "Meio-campo")
jogador6 = Jogador("David De Gea", "Goleiro")

time1 = Time("Brasil")
time2 = Time("Portugal")

time1.adicionar_jogador(jogador1)
time1.adicionar_jogador(jogador2)
time1.adicionar_jogador(jogador3)

time2.adicionar_jogador(jogador4)
time2.adicionar_jogador(jogador5)
time2.adicionar_jogador(jogador6)

time1.listar_jogadores()
print()
time2.listar_jogadores()
