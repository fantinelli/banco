from classes import *


def criar_cliente(self):
    nome = str(input("Digite o nome do cliente: "))
    CPF = int(input("Digite o CPF: "))
    RG = int(input("Digite o RG: "))
    telefone = int(input("Digite o telefone: "))
    email = str(input("Digite o e-mail: "))
    renda = float(input("Digite a renda: "))
    depinicial = float(input("Digite o depósito inicial: "))

    cliente = Cliente( nome, CPF, RG, telefone, email, renda, depinicial)
    return cliente


class Transferencia:
    def __init__(self, cliente, saldo, saque, deposito):
        self.cliente = cliente
        self.saldo = saldo
        self.saldo - self.saque == saque
        self.saldo + self.deposito == deposito
