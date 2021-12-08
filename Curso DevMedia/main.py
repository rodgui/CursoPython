from typing import ClassVar
from pessoa_juridica import PessoaJuridica
from pessoa_fisica import PessoaFisica

a = PessoaFisica('111.222.333-44', nome='Alfredo', idade=22)

print(a.getCPF())
print(a.getNome())
print(a.getIdade())

b = PessoaJuridica('64.614.527/0001-99', nome='Empresa X', idade=22)

print(b.getCNPJ())
print(b.getNome())
print(b.getIdade())
