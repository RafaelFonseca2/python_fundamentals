# import sys
# import string

# arquivo = open(sys.argv[1], 'r').read().lower()
# rotacao = input(sys.argv[2])

# alfabeto = string.ascii_lowercase
# resultado = ''

# for letra in alfabeto:
#     if letra in alfabeto:
#         posicao = alfabeto.find(letra)
#         posicao = (posicao + rotacao) % 26
#         resultado += alfabeto[posicao]

# print(resultado)

# with open('dados_cifrados', 'w') as d:
#     d.write(reultado)
 


from module import mod, mod2
# from math import sqrt
# import pandas as pd

from module import *

mod()

mod2()