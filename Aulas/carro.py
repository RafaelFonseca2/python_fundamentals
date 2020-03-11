# -*- coding: UTF-8 -*-

# class automovel():

#     def __init__(self):
#         self.motor = 'combustão'
#     def ligar(self):
#         print('carro ligado')

# class Carro(automovel):

#     def __init__(self):
#         automovel.__init__(self)
#         self.rodas = 4
#         self.porta_mala = 'Normal'
#         self.volante = True
#         self.tanque = True

#     def desligar(self):
#         print('carro desligado')

#     def acelerar(self):
#         print('acelerando')

#     def frear(self):
#         print('freando')

# class Fiat147(Carro):

#     def __init__(self):
#         super().__init__()
#         self.porta_mala = 'Com agua'


# c001 = Fiat147()

# print(c001.motor)
# c001.ligar()


class Pai():
    hobby = 'programar'
    def __init__(self):
        self.profissao = 'advogado'

    def mudarProfissao(self, nova_profissao):
        self.profissao = nova_profissao
 
    def mudarHobby(self):
        self.hobby = 'jardineiro'

joao = Pai()

joao.mudarHobby()
print(joao.hobby)



# class Mae():

#     def __init__(self):
#         self.profissao = 'medica'

# class Filho(Pai, Mae):

#     def __init__(self):
#         Mae.__init__(self)
#         self.profissao = "programação"

# jose = Filho()

# print(jose.profissao)












