
class Livro:
    def __init__(self, nome):
        self.nome = nome
        self.alugado = False
    
    
    def alugar(self):
        if not self.alugado:
            self.alugado = True
            return f"Livro {self.nome} alugado com sucesso"
        else:
            return f"Livro {self.nome} indisponível para alugar"
    
    
    def devolver(self):
        if self.alugado:
            self.alugado = False
            return f"Livro {self.nome} devolvido com sucesso"
        else:
            return f"Livro {self.nome} não está alugado"


class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.livros_alugados = []
    
    
    def alugar_livro(self, livro):
        resultado = livro.alugar()
        if "sucesso" in resultado:
            self.livros_alugados.append(livro)
            return f"{self.nome} alugou o livro {livro.nome}"
        else:
            return f"Desculpe {self.nome}, resultado"
    
    
    def devolver_livro(self, livro):
        if livro in self.livros_alugados:
            livro.devolver()
            self.livros_alugados.remove(livro)
            return f"{self.nome} devolveu o livro {livro.nome}"
        else:
            return f"{self.nome} não está com este livro"
