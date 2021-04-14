from pessoa import Pessoa
from fisica import Fisica
from juridica import Juridica

divisao = "----------------"

p1 = Pessoa(1, "Alessandra", "Rua Santa Úrsula", 123456789)
p1.imprimir_dados()
print (divisao)

f1 = Fisica(2, "Moisés", "Rua Emília", 124578963, "321.654.987-11", 24, 80, 1.78)
f1.imprime_cpf()
print (divisao)

j1 = Juridica(3, "Nitro", "Rua Coronel", 111222333, "44.555.666/77", 80, 100)
j1.imprime_cnpj()