
from classes import Livro, Pessoa

galatas = Livro("Gálatas")
alexandre = Pessoa("Alexandre")
resultado = alexandre.alugar_livro(galatas)
print(resultado)
resultado = alexandre.devolver_livro(galatas)
print(resultado)
