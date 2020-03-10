# EXEMPLO 1

# while True:

#     try:
#         x = int(input('digite o primeiro numero: '))
#         y = int(input('digite o segundo numero: '))
#         print(x + y)
#         break
#     except TypeError as e:
#         print('TypeError')
#         continue
#     except:
#         print('Calculando...')
#         continue

# EXEMPL 2

# try:
#     produto_id = [1111,1112,1113,1114,1115]
#     id_desejado = int(input('digite o ID do produto: '))
#     if id_desejado not in produto_id:
#         raise ValueError('Produto não cadastrado!')
#     else:
#         print('produto cadastrado')

# except ValueError as e:
#     print(e)




























