#fonte: https://www.devmedia.com.br/python-tutorial/33274
#coding: utf-8
import sys

##
# Formatação de texto com print
##
print("\n" + "-- Formatação de Dados --" + "\n")
meu_nome = "Sintaxes Python"
meu_nick = 'Devmedia'
print ("Nome: %s, Nick: %s" % (meu_nome.upper(), meu_nick))
print ("Meu nome comeca com a letra ", meu_nome[0])
print ("Meu nome comeca com a letra ", meu_nome[0].lower())
print ("Meu primeiro nome é ", meu_nome[0:7])

##
# Entrada de Dados
##
print("\n" + "-- Entrada de Dados --" + "\n")
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print("Digite seu sexo: ")
sexo = sys.stdin.readline()

print("Nome:"+nome + "\n" + "Sexo: %s Idade: %s" %(sexo,idade))

##
# Condição IF, ELIF, ELSE
##
print("\n" + "-- Condição IF ELIF ELSE --" + "\n")
dedos = int(input("Você tem quantos anos? "))

if dedos == 18:
    print("Você tem 18 anos")
elif dedos > 18:
    print("Você tem mais de 18 anos")
else:
    print("Voce é menor")

##
# Switch Case
##
print("\n" + "-- Condição Switch Case --" + "\n")
var1 = int(input("Digite um Número para var1: "))
var2 = int(input("Digite um Número para var2: "))
if var1 == 1:
  print("Número var1 igual a 1")
elif var1 == 2 or var2 == 3:
  print("var1 diferente de 1 ou var2 diferente de 2")
elif var1 >= 1000 or var2 <= -1000:
  print("var1 maior que 1000 ou var2 menor que -1000")
else:
  print("nenhuma das alternativas anteriores")

##
# Função RANGE()
##
print("\n" + "-- Função Range() --" + "\n")
print (range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print (range(5, 10)) # [5, 6, 7, 8, 9]
print (range(10, 0)) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
i=int(input("Digite um Número: "))
if i in range(0,10):
  print("Está Contido")
else:
  print("Não está Contido")

##
# Laço de Repetição FOR
##
print("\n" + "-- Laço Repetição FOR () --" + "\n")
for fruta in ["banana", "maca ", "uva"]:
    print("Fruta : " + fruta)
print("------------------------------")
for i in range(0, 10):  # (Inclui o Zero, NÃO INCLUI O 10)
    print("i = " + str(i))
print("------------------------------")
for i in range(0, 10):
    print('Não realizado1')
    if i == 0:
        break
print('Realizado')

##
# Laço usando While
#
i = 0
while i < 10:
  print ("i = ",i)
  i += 1

#while True:
#  continue

##
# Exceções e Listas
##
print("\n" + "-- Exceções --" + "\n")
try:
    print(1 + 'st try')
except:
    print("Isto é uma exceção")

##
# Listas
##
print("\n" + "-- Listas --" + "\n")
lista = [1, 2, 3]
print("Tamanho de lista:", len(lista))
lista[0] = 9
print("-----------")
for i in range(len(lista)):
  print(lista[i])

lista = [1, 2, 3]
print(lista[0])
print(lista[1])
print(lista[-1])
print(lista[-2])
print(lista[0:2])
print(lista[:2])
print(lista[1:])

##
# Função Capitalize, Listas e For
##
print("\n" + "-- Capitalize, Listas, For --" + "\n")
frutas = ['laranja', 'banana', 'abacaxi']

frutas.sort()
print(frutas)
frutas[0] = 'framboesa'
for item in frutas:
  print(item.capitalize())

##
# Função remove()
##
print("\n" + "-- Listas e Remove() --" + "\n")
convidados = []  # define uma lista vazia
convidados.append('Exemplo 1')
convidados.append('Exemplo 2')
convidados.append('Exemplo 3')
convidados.append('Exemplo 4')
print("Tenho ", len(convidados), " Convidados")
convidados.sort()
print("Sao eles:")
print(convidados)
print("O primeiro convidado eh o ", convidados[0])
convidados.remove("Exemplo 4")  # aqui tiramos o Exemplo 4 da lista
print("Agora tenho somente ", len(convidados), " Convidados")
print("Sao eles:")
for convidado in convidados:
  print(convidado)

##
# Tuplas
#
print("\n" + "-- Tuplas --" + "\n")
frutas = ('laranja', 'banana', 'abacaxi')
type(frutas)
print(frutas)
#frutas[0]='framboesa';
for item in frutas:
  print(item.capitalize())

##
# Dicionario
##
print("\n" + "-- Dicionario --" + "\n")
veiculo = {}
veiculo['marca'] = 'Puma'
veiculo['modelo'] = 'GTB'
veiculo['ano'] = 1978
print(veiculo['marca'])
dicionario = {"chave": "17,532", "chave2": "17,365"}
print(dicionario["chave"])  # imprime valor (17,532)

##
# Matriz
##
print("\n" + "-- Matriz --" + "\n")
#Criando uma matriz de 5x3 inicializada com 0
lin = 5
col = 3
matriz = []
for i in range(0, lin):
  linha = []
  for j in range(0, col):
    linha.append(j)
matriz.append(linha)
#varrendo a matriz
for i in range(0, len(matriz)):
  for j in range(0, len(matriz[0])):
    print(matriz[i][j])

##
# Funções
##
print("\n" + "-- Funções --" + "\n")
print("\nDoc. da função:\n"+fatorial.__doc__)


def fatorial(numero):  # função recursiva
  """
  Funcao recursiva
  As três aspas duplas é a documentação
  """
  if numero <= 1:
    return 1
  else:
    return (numero * fatorial(numero - 1))


for n in range(1, 11):
  print("Fatorial de", n, " eh ", fatorial(n))

##
# Funções com parametros opcionais
##
print("\n" + "-- Funções com parametros opcionais --" + "\n")


def potencia(base, exp=2):  # função com parâmetro opcional

    if exp == 0:
      return 1
    pot = base
    i = 1
    while i < exp:
      pot = pot*base
      i = i+1
    return pot


print("Começa aqui!")
print("Potencia de 2: ", potencia(2))  # imprime 4
print("Potencia de 2 elevado a 8: ", potencia(2, 8))  # imprime 256

##
# Arquivos no Python
##
print("\n" + "-- Arquivos --" + "\n")
print("\n" + "-- Abertura e Criação --" + "\n")

arq = open('./meuarquivo.txt', 'w')
arq.write('gravando em um arquivo é simples')
arq.close()

print("\n" + "-- Leitura --" + "\n")
arq = open('./meuarquivo.txt')  # r é default
leitura = arq.read(10)
print(leitura)
restante = arq.read()
print(restante)

##
# Trabalhando com Strings
##

nome_1 = "Rodrigo Garcia"
nome_2 = "Ana Flavia"

print(type(nome_1))
print(type(nome_2))

## Indice
nome_1 = "Rodrigo Garcia"
print(nome_1[0]) # R
print(nome_1[0:3]) # Rod
print(nome_1[-2]) # i

## Imutabilidade
nome = 'Eduardo'
print(id(nome))
nome = 'Felipe'
print(id(nome))

nome_1 = 'Rodrigo'
nome_2 = 'Ana'

print(len(nome_1)) # 7
print(len(nome_2)) # 3

##
# Concatenação de Strings
##

nome = 'Daniel'
sobrenome = 'Silva'

nome_completo = nome + ' ' + sobrenome
print(nome_completo) # Daniel Silva

##
# Comparação de Strings
##

nome_1 = 'Eduardo'
nome_2 = 'Eduardo'

if nome_1 == nome_2:
  print('iguais')
else:
  print('diferentes')

if nome_1 is nome_2:
  print('Iguais')
else:
  print('Diferentes')

##
# Principais metodos de Strings
##

## Find()
mensagem = 'string do Python'
print(mensagem.find('Python')) #10
print(mensagem.find('Java')) #-1

## Split()
mensagem = 'Estou aprendendo Python'
lista_mensagem = mensagem.split(' ') # separado ' ' será usado para criar a lista
print(type(mensagem)) # str
print(type(lista_mensagem)) # type 'list'
print(lista_mensagem) # ['Estou', 'aprendendo', 'Python']
print(lista_mensagem[1]) # aprendendo

## Upper()
mensagem = 'Estou aprendendo Python'
nova_mensagem = mensagem.upper()
print(nova_mensagem) #ESTOU APRENDENDO PYTHON

## Metodos Lower)