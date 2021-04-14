from pessoa import Pessoa

# Fisica
# cpf: string
# idade: int
# peso: double
# altura: double
# - imprime_cpf(): string
# - calcula_imc():

class Fisica(Pessoa):
    def __init__(self, codigo = None, nome = None, endereco = None, telefone = None, cpf = None, idade = None, peso = None, altura = None):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self._cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def imprime_cpf(self):
        Pessoa.imprimir_dados(self)
        print("CPF: ", self._cpf)
        print("IMC: ", {round(self.peso/(self.altura**2), 2)})
