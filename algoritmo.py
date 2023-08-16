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

def excluir_clientes():
    cliente_excluido = str(input("Digite o nome do cliente: "))
    if cliente_excluido in Agencia:
        Agencia.pop(cliente_excluido)
        print(f" O cliente {cliente_excluido} foi excluído")
    else:
        print("Este nome não está registrado")
        
class Transferencia:
    def __init__(self, cliente, saldo, saque, deposito):
        self.cliente = cliente
        self.saldo = saldo
        self.saldo - self.saque == saque
        self.saldo + self.deposito == deposito
