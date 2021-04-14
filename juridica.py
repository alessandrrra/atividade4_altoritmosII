from pessoa import Pessoa

# Juridica
# cnpj: string
# inscricao_estadual: string
# quantidade_funcionarios: int
# - imprime_cnpj(): void
# - emitir_nf

class Juridica(Pessoa):
    def __init__(self, codigo = None, nome = None, endereco = None, telefone = None, cnpj = None, inscricaoEst = None, qtd_funcionarios = None):
        Pessoa.__init__(self, codigo = None, nome = None, endereco = None, telefone = None)
        self._cnpj = cnpj
        self._inscricaoEst = inscricaoEst
        self.qtd_funcionarios = qtd_funcionarios

    def imprime_cnpj(self):
        Pessoa.imprimir_dados(self)
        print("CNPJ: ", self._cnpj)
        print("Inscrição Estadual: ", self._inscricaoEst)
        print("Quantidade de funcionários: ", self.qtd_funcionarios)

    def emitir_nf(self):
        return None