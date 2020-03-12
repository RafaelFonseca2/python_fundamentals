
print('digite o numero da conta: \n')
numero_conta = int(input('>>> '))
print('nome do titular:\n ')
nome = (input('>>> '))
saldo = 0.0

class banco():
    def __init__(self):
        self.banco = '999'
        self.conta = numero_conta
        self.agencia = '08'
        self.nome = nome

    def saque(self):
        s = int(input('Valor de saque = '))
        self.sacar = saldo - s
        print(f'Saldo = {self.sacar}')

    def deposito(self):
        d = int(input('Valor do deposito = '))
        self.depositar = saldo + d
        print(f'Saldo = {self.depositar}')

    def extrato(self):
        self.extrato = {'Numero do banco: ': self.banco, 'Numero da agencia: ': self.agencia, 'Nome do cliente: ': nome, 'Saldo: ': saldo}
        print(self.extrato)



print('\nOla OldBank')
print('Bem vindo!')
print('Selecione a opcao abaixo: ')
print('\tPara extrato digite 1')
print('\tPara saque digite 2')
print('\tPara deposito digite 3')
opcao = int(input('>>> '))
cliente = banco()
try:
    if opcao == 1:
        cliente.extrato()
    elif opcao == 2:
        cliente.saque()
    elif opcao == 3:
        cliente.deposito()
    else:
        raise ValueError('Opção invalida')
except ValueError as v:
    print(v)





