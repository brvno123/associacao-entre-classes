class Musica:
    def __init__(self, titulo, cantor):
        self.titulo = titulo
        self.cantor = cantor

    def __str__(self):
        return f'{self.titulo} - {self.cantor}'


class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar_musica(self, musica):
        self.musicas.append(musica)

    def listar_musicas(self):
        print(f"Playlist: {self.nome}")
        for musica in self.musicas:
            print(musica)


musica1 = Musica("Blinding Lights", "The Weeknd")
musica2 = Musica("Shape of You", "Ed Sheeran")
musica3 = Musica("Levitating", "Dua Lipa")

musica4 = Musica("Bohemian Rhapsody", "Queen")
musica5 = Musica("Imagine", "John Lennon")
musica6 = Musica("Smells Like Teen Spirit", "Nirvana")

playlist1 = Playlist("Pop Hits")
playlist2 = Playlist("Rock Classics")

playlist1.adicionar_musica(musica1)
playlist1.adicionar_musica(musica2)
playlist1.adicionar_musica(musica3)

playlist2.adicionar_musica(musica4)
playlist2.adicionar_musica(musica5)
playlist2.adicionar_musica(musica6)

playlist1.listar_musicas()
print()
playlist2.listar_musicas()