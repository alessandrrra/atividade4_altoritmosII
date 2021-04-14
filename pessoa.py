# Pessoa
# codigo: int
# nome: string
# endereco: string
# telefone: string
# - imprime_dados(): string
# - imprime_telefone(): void

class Pessoa:
    def __init__(self, codigo = None, nome = None, endereco = None, telefone = None):
        self._codigo = codigo
        self.nome = nome
        self.__endereco = endereco
        self._telefone = telefone
    
    def imprimir_dados(self):
        print("Código: ", self._codigo)
        print("Nome: ", self.nome)
        print("Endereço: ", self.__endereco)
        print("Telefone: ", self._telefone)