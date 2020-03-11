# Crie uma classe Mamifero com os atributos
#         bebe leite

# Crie uma classe homosapiens com os atributos:

#         polegares = True
#         formaCaminhar = 'bipede'

# Metodos:
#     Caça
#     Comer
#     Dormir
#     Construir



class Mamifero():
        def __init__(self):
                self.alimentacao = 'bebe leite'

class homosapiens(Mamifero):
        def __init__(self):
                Mamifero.__init__(self)
                self.polegares = True
                self.caminhar = 'bipede'

        def Caca(self):
                print('Caça')

        def Comer(self):
                print('Comer')

        def Dormir(self):
                print('Dormir')

        def Construir(self):
                print('Construir')


animal = homosapiens()
animal.Caca()
print(animal.polegares)
print(animal.alimentacao)
























