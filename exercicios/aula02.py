# EX1
# dada o dicionario:

# produtos = dict(produtos=dict(p1=dict(nome="Camiseta Star Wars", preco=99.90), p2=dict(nome='Caneca Ricky&Morty', preco=49.90), p3=dict(nome='Camiseta SpiderMan', preco=69.90)))

# Apatir de id do produto mostraremos o nome e o preco
# Caso o produto nao exista mostraremos a seguinte mensagem:
# Produto inexistente

# try:
#     id_produto = input('Digite o id do produto: ' )
#     if id_produto not in produtos['produtos']:
#         raise ValueError('Produto inexistente!')
#     else:
#         print(f"Produto: {produtos['produtos'][id_produto]['nome']}")
#         print(f"Preço: {produtos['produtos'][id_produto]['preco']}")

# except ValueError as v:
#     print(f'Erro: {v}')

# EX2
# with open('nome_arquivo', 'w') as f:
#     f.write('Meu primeiro arquivo')


# EX3
# def dobra(valor):
#     return valor * 2


# print(dobra(122))


# EX4
# produtos = []

# def cadastraProduto(produto):
#     return produtos.append(produto)

# def listaProduto():
#     print(produtos)

# def deletaProduto(produto):
#     if produto in produtos:
#         produtos.remove(produto)
#     else:
#         print('produto inexistente')



# cadastraProduto('tenis')
# cadastraProduto('sapato')
# cadastraProduto('calca')
# listaProduto()
# deletaProduto('sapato')
# listaProduto()


# EX5
# nome = 'python'

# def linux():
#     global nome
#     nome = 'linux'
#     return nome

# linux()
# print(nome)

# usuarios = []

# def cadastra_Pessoa(add=None):
#     # pessoa = dict(nome='Rafael', sobrenome='Fonseca', idade=26)
#     if add is None:
#         pass
#     else:
#         usuarios.append(add)
    
# cadastra_Pessoa('Rafael')
# print(usuarios)


# EX6

# frutas = []

# def inserFrutas(*args):
#     for f in args:
#         frutas.append(f)

# inserFrutas('abacaxi', 'laranja', 'limao', 'banana')

# print(frutas)


# EX7

# camiseta = {}

# def insereCamiseta(**kwargs):
#     global camiseta
#     camiseta = kwargs
#     return camiseta

# insereCamiseta(camiseta01='Star Wars',camiseta02='Batman')
# print(camiseta)



# EX8

# dobro = lambda x: x * 2

# print(dobro(10))

# EX9
# faca uma funcao lambda que receba 3 valores e retorne a soma 

# soma = lambda x, y, z: x + y + z

# print(soma(2, 3, 4))

# EX10
from functools import reduce

numeros = [2,3,4,5,6,7,8,9,10,11]

dobro = list(map(lambda x: x * 2, numeros))
numeros_par = list(filter(lambda x: x % 2 == 0, numeros))
soma = reduce(lambda x, y: x + y, numeros)

print(soma)
# print(numeros_par)
# print(dobro)

# ou

# for i in numeros:
#     dobro.append(i*2)
































































































