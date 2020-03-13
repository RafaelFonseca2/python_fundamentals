from unittest import 


def somar(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

class Testes(TestCase):

    def test_soma(self):
        self.assertEqual(somar(5, 5), 10)
        self.assertEqual(type(somar(5, 5), int))
        self.assertIsNotNone(somar(5, 5), None)
        self.assertLess(somar(5, 5), 11)

    def test_sub(self):
        self.assertEqual(subtracao(5, 5), 10)
        self.assertEqual(type(subtracao(5, 5), int))
        self.assertIsNotNone(subtracao(5, 5), None)
        self.assertLess(subtracao(5, 5), 11)


        
    


# # Testar funcao somar
# assert somar(2,2) == 4, f"Obtido: {somar(2,2)} Esperado: 4"
# assert somar(3,2) == 5, f"Obtido: {somar(2,3)} Esperado: 5"

# assert subtracao(3,2) == 1, f"Obtido: {subtracao(3,2)} Esperado: 1"

