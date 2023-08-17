from classes import *
agencia = Agencia()

def criar_cliente():

    x = 0
    while x == 0:
        nome = str(input("Digite o nome do cliente: "))
        for i in nome:
            if i.isdigit():
                print("Valor inválido")
                break
            else:
                x = 1

    x = 2
    while x == 2:
        email = str(input("Digite o email do cliente: "))
        for a in email:
             if a.isdigit():
                  print("Valor inválido")
                  break
             else: x = 4



    CPF = float(input("Digite o CPF do cliente: "))
    RG = float(input("Digite o RG do cliente: "))
    telefone = float(input("Digite o telefone do cliente: "))
    renda = float(input("Digite a renda do cliente: "))    
    depinicial= float(input("Digite o depósito inicial do cliente: ")) 
    cli = nome, email, CPF, RG, telefone, renda, depinicial
    agencia.novo_cliente(nome)
    return cli
        

def excluir():
    cliente= str(input("Digite o nome do cliente a ser excluído: "))
    agencia.excluir_cliente(cliente)


def alterar():
     
   while True:
   
        escolha2 = int(input("O que deseja fazer? \n [1] Alterar Nome \n [2] Alterar CPF \n [3] Alterar RG \n [4] Alterar telefone \n [5] Alterar Email \n [6] Alterar Renda > "))
        if escolha2 == 1:
            agencia.setNome (input("qual seria a alteração?"))

        elif escolha2 == 2:
            agencia.setCPF (input("qual seria a alteração?"))

        elif escolha2 == 3:
            agencia.setRG (input("qual seria a alteração?"))

        elif escolha2 == 4:
            agencia.setTelefone (input("qual seria a alteração"))

        elif escolha2 == 5:
            agencia.setEmail (input("qual seria a alteração?"))

        elif escolha2 == 6:
            agencia.setRenda (input("qual seria a alteração"))

        elif escolha2 == 7:
            break
     
def transferencia():
    nome_cliente = str( input("Digite o nome do cliente: "))
    nome_destino = str( input("Digite o nome do Destinatário: "))
    valor_envio = float(input("Digite o valor a depositar: "))
    

    for cliente in agencia._clientes:
        if cliente.nome == nome_cliente:
            cliente_encontrado = cliente
            break    

        if cliente_encontrado:
            cliente_encontrado.depositar(valor_envio)
            valor_envio + self.saldo(nome_destino)
        else:
            print("Transferência Incompleta")

def deposito():
    nome = input("Digite o Nome do cliente: ")
            cliente = sistema.buscar_cliente(nome)
            if cliente:
                valor = float(input("Digite o valor do depósito: "))
                cliente.deposito(valor)

def sacar():
    nome = input("Digite o Nome do cliente: ")
            cliente = sistema.buscar_cliente(nome)
            if cliente:
                valor = float(input("Digite o valor do saque: "))
                cliente.saque(valor)

def main():
    tam = 30
    while True:
            try:
            
                print(f"+{'-'*tam}+")
                print(f"|{'BEM VINDO AO SOFTWARE DO BANCO':^{tam}}")
                print(f"+{'-'* tam}+")
                print("O que deseja fazer? \n [1] Cadastrar cliente \n [2] Excluir cliente \n [3] Alterar cliente \n [4] Transferencia \n [5] Depositar \n [6] Sacar \n [7] Consultar saldo \n [8] Agencia \n [9] Sair")
                match menu == int(input("> ")):
                    case 1:
                        print("Você está prestes a criar um novo cliente, insira as informações solicitadas.")
                        criar_cliente()
                        escolha2 = int(input("O que deseja fazer? \n [1] Voltar ao menu \n [2] Adicionar outro cliente \n [3 Fechar o software] \n > "))
                        if escolha2 == 1:
                            main()
                        elif escolha2 == 2:
                            criar_cliente()
                        elif escolha2 == 3:
                                break

                    case 2:
                            print("Você está prestes a excluir um cliente, insira as informações solicitadas.")
                            excluir()

                    case 3:
                        print("Você está prestes a alterar um cliente")
                        alterar()

                    case 4:
                        print("Realizar Transferência ")
                        Transferencia()

                    case 5:
                        print("Realizar depósito")
                        deposito()

                    case 6:
                        print("Sacar")
                        sacar()

                    case 7:
                        print("Consultar saldo")
                        consultar_saldo()
                        
                    case _:
                            break
                        
            except Exception:
                print('Problema: Digito não correspondente')    
                    

