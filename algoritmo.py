from classes import *


def criar_cliente():
    nome = str(input("Digite o nome do cliente: "))
    CPF = int(input("Digite o CPF: "))
    RG = int(input("Digite o RG: "))
    telefone = int(input("Digite o telefone: "))
    email = str(input("Digite o e-mail: "))
    renda = float(input("Digite a renda: "))
    depinicial = float(input("Digite o depósito inicial: "))

    cliente = Cliente( nome, CPF, RG, telefone, email, renda, depinicial)
    return cliente

def excluir_clientes(agencia):
    cliente_excluido = str(input("Digite o nome do cliente: "))
    cliente = agencia.percorrer_lista(cliente_excluido)
    if cliente_excluido in Agencia:
        print(f" O cliente {cliente_excluido} foi excluído")
    else:
        print("Este nome não está registrado")


def main():
    tam = 30
    while True:
        print(f"+{'-'*tam}+")
        print(f"|{'BEM VINDO AO SOFTWARE DO BANCO':^{tam}}")
        print(f"+{'-'* tam}+")
        print("O que deseja fazer? \n [1] Cadastrar cliente \n [2] Excluir cliente \n [3] Alterar cliente \n [4] Transferencia \n [5] Depositar \n [6] Sacar \n [7] Consultar saldo \n [8] Agencia \n [9] Sair")
        escolha1 = int(input("> "))
        if escolha1 == 1:
            print("Você está prestes a criar um novo cliente, insira as informações solicitadas.")
            criar_cliente()
            escolha2 = int(input("O que deseja fazer? \n [1] Voltar ao menu \n [2] Adicionar outro cliente \n [3 Fechar o software] \n > "))
            if escolha2 == 1:
                main()
            elif escolha2 == 2:
                criar_cliente()
            elif escolha2 == 3:
                break


        elif escolha1 == 2:
            print("Você está prestes a excluir um cliente, insira as informações solicitadas.")
            excluir_clientes()
        elif escolha1 == 9:
            break
            
class Transferencia:
    def __init__(self, cliente, saldo, saque, deposito):
        self.cliente = cliente
        self.saldo = saldo
        self.saldo - self.saque == saque
        self.saldo + self.deposito == deposito
