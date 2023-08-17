from classes import *

agencia = Agencia()


def main():

    while True:
        try:
            print("+------------------------------+")
            print("| BEM VINDO AO SOFTWARE DO BANCO |")
            print("+------------------------------+")
            print("[1] Cadastrar cliente")
            print("[2] Excluir cliente")
            print("[3] Alterar cliente")
            print("[4] Transferência")
            print("[5] Depositar")
            print("[6] Sacar")
            print("[7] Consultar saldo")
            print("[8] Sair")

            escolha1 = int(input("> "))

            if escolha1 == 1:
                print("Você está prestes a criar um novo cliente, insira as informações solicitadas.")
                cliente = criar_cliente()
                agencia.novo_cliente(cliente)
            elif escolha1 == 2:
                print("Você está prestes a excluir um cliente, insira as informações solicitadas.")
                excluir(agencia)
            elif escolha1 == 3:
                print("Você está prestes a alterar um cliente")
                alterar(agencia)
            elif escolha1 == 4:
                print("Realizar Transferência")
                transferencia(agencia)
            elif escolha1 == 5:
                print("Realizar depósito")
                deposito(agencia)
            elif escolha1 == 6:
                print("Sacar")
                sacar(agencia)
            elif escolha1 == 7:
                print("Consultar saldo")
                consultar_saldo(agencia)
            elif escolha1 == 8:
                break
            else:
                print("Opção inválida.")

        except ValueError:
            print('Problema: Digito não correspondente')

def criar_cliente():
    while True:
        nome = input("Digite o nome do cliente: ")
        if nome.isalpha():
            break
        else:
            print("Valor inválido")

    while True:
        email = input("Digite o email do cliente: ")
        if not any(c.isdigit() for c in email):
            break
        else:
            print("Valor inválido")

    CPF = input("Digite o CPF do cliente: ")
    RG = input("Digite o RG do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    renda = input("Digite a renda do cliente: ")
    depinicial = input("Digite o depósito inicial do cliente: ")

    cliente = Cliente(nome, CPF, RG, telefone, email, renda, depinicial)
    return cliente

def excluir(agencia):
    nome_cliente = input("Digite o nome do cliente a ser excluído: ")
    agencia.excluir_cliente(nome_cliente)

def alterar(agencia):
    nome_atual = input("Digite o nome atual do cliente: ")
    cliente = agencia.buscar_cliente(nome_atual)
    if cliente:
        while True:
            escolha2 = int(input("O que deseja fazer?\n[1] Alterar Nome\n[2] Alterar CPF\n[3] Alterar RG\n[4] Alterar telefone\n[5] Alterar Email\n[6] Sair\n> "))
            if escolha2 == 1:
                novo_nome = input("Novo nome: ")
                cliente.setNome(novo_nome)
            elif escolha2 == 2:
                novo_CPF = input("Novo CPF: ")
                cliente.setCPF(novo_CPF)
            elif escolha2 == 3:
                novo_RG = input("Novo RG: ")
                cliente.setRG(novo_RG)
            elif escolha2 == 4:
                novo_telefone = input("Novo telefone: ")
                cliente.setTelefone(novo_telefone)
            elif escolha2 == 5:
                novo_email = input("Novo email: ")
                cliente.setEmail(novo_email)
            elif escolha2 == 6:
                break

def transferencia(agencia):
    nome_cliente = input("Digite o nome do cliente: ")
    nome_destino = input("Digite o nome do Destinatário: ")
    valor_envio = float(input("Digite o valor a depositar: "))

    cliente_encontrado = agencia.buscar_cliente(nome_cliente)
    if cliente_encontrado:
        cliente_destino = agencia.buscar_cliente(nome_destino)
        if cliente_destino:
            cliente_encontrado.saldo -= valor_envio
            cliente_destino.saldo += valor_envio
            print(f"Transferência de R${valor_envio:.2f} realizada de {cliente_encontrado.nome} para {cliente_destino.nome}")
        else:
            print("Destinatário não encontrado")
    else:
        print("Remetente não encontrado")

def deposito(agencia):
    nome = input("Digite o Nome do cliente: ")
    cliente = agencia.buscar_cliente(nome)
    if cliente:
        valor = float(input("Digite o valor do depósito: "))
        cliente.saldo += valor
        print("Depósito realizado com sucesso!")

def sacar(agencia):
    nome = input("Digite o Nome do cliente: ")
    cliente = agencia.buscar_cliente(nome)
    if cliente:
        valor = float(input("Digite o valor do saque: "))
        if valor <= cliente.saldo:
            cliente.saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente")

def consultar_saldo(agencia):
    nome = input("Digite o Nome do cliente: ")
    cliente = agencia.buscar_cliente(nome)
    if cliente:
        print(f"Saldo de {cliente.nome}: R${cliente.saldo:.2f}")
