# EXERCICIO 1

# Faça um script que peca o seu nome
# e imprima a seguinte saudação
# ola meu nome é

# nome = input("Digite seu nome: ")
# print('meu nome é',nome)

# EXERCICIO 2

# dado a lista:

# imprima na tela as seguintes mensagens:

# time: (nome do time), cores: (cores)

# times = [["corinthians", "palmeiras", "sao paulo"],["preto", 'branco', "verde", 'vermelho']]

# print("time: ",times[0][2])
# print('cores: ',times[1][0],times[1][1],times[1][3])
# ou
# print('time: {} Cores: {} {}'.format(times[0][1], times[1][2], times[1][1]))
# ou
# print(f'time: {times[0][1]} Cores: {times[1][2]} e {times[1][1]} ')

# EXERCICIO 3

# Dado o dicionario

# dados = {
#     'estados': {
#         'sp': {
#             'nome': 'Sao Paulo',
#             'municipios': 645,
#             'populacao': 44.04
#         },
#         'rj': {
#             'nome': 'Rio de Janeiro',
#             'municipios': 92,
#             'populacao': 16.72
#         },
#         'mg': {
#             'nome': 'Minas Gerais',
#             'municipios': 31,
#             'populacao': 20.87
#         }
#     }
# }

# Imprima na tela as seguintes mensagens:

# Estado: <nome>
# Municipio: <qnt>
# Populacao: <qnt>

# print(dados['estados']['sp']['nome'])
# print(dados['estados']['sp']['municipios'])
# print(dados['estados']['sp']['populacao'])


# print(f"Estado: {dados['estados']['sp']['nome']}")
# print(f"Estado: {dados['estados']['sp']['municipios']}")
# print(f"Estado: {dados['estados']['sp']['populacao']}")

# for estado in dados['estados'].keys():
#     print(f"estado: {dados['estados'][estado]['nome']}")
#     print(f"municipios: {dados['estados'][estado]['municipios']}")
#     print(f"populacao: {dados['estados'][estado]['populacao']}")
#     print(' ')


# EXERCICIO 4

# faça um programa que receba 4 notas de aluno:

# n1
# n2
# n3
# n4

# calcule a media
# caso seja menos que 7 imprima reprovado
# caso seja maior que 5 e menor que 7 - recuperacao



# n1 = float(input('nota 1: '))
# n2 = float(input('nota 2: '))
# n3 = float(input('nota 3: '))
# n4 = float(input('nota 4: '))

# media = (n1+n2+n3+n4)/4

# if media >= 7:
#     print("aprovado")
#     print(media)

# elif media >= 5 and media < 7:
#     print(f' media: {media}')
#     print(f' aluno em recuperação')

# else:
#     print("reprovado")
#     print(media)

   

# faça um programa que receba dois valores e retorne o maior valores
# caso sejam iguais imprima valores iguais

# n1 = float(input('digite 1 valor: '))
# n2 = float(input('digite 2 valor: '))

# if n1 > n2:
#     print(f' valor: {n1}')

# elif n1 == n2:
#     print(f' valores iguais: {n1}')

# else:
#     print(f' valor {n2}')

# if n1 == n2:
#      print(f' valores iguais: {n1}')

# else:
#     print(max(n1, n2))


v = float(input('digite valor da hora: '))
h = float(input('digite horas trabalhadas: '))

s = v * h
print(f' salario bruto: {s}')

if s <= 1900:
    ir = 0
elif s > 1900 and s <= 2800:
    ir = float(0.07)
elif s > 2800 and s <= 3700:
    ir = float(0.15)
elif s > 3700 and s <= 4600:
    ir = float(0.22)
else:
    ir = float(0.27)

d1 = ir * s
print(f' IR ({ir*100}%) : {d1}')

d2 = s * 0.03
print(f' sindicato (3%) : {d2} ')

fgts = s * 0.11
print(f' FGTS (11%) : {fgts}')

dt = d1 + d2
print(f' desconto total : {dt}')

sl = s - d1 - d2
print(f' salario liquido : {sl}')

















