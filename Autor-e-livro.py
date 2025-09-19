class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade

    def __str__(self):
        return self.nome


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f'Título: {self.titulo}, Autor: {self.autor}'


autor1 = Autor("Gabriel García Márquez", "Colombiano")
autor2 = Autor("J.K. Rowling", "Britânica")

livro1 = Livro("Cem Anos de Solidão", autor1)
livro2 = Livro("O Amor nos Tempos do Cólera", autor1)
livro3 = Livro("Harry Potter e a Pedra Filosofal", autor2)

livros = [livro1, livro2, livro3]

for livro in livros:
    print(livro)
