class Cliente:
    def __init__(self, nome, CPF, RG, telefone, email, renda, depinicial):
        self.nome = nome
        self.CPF = CPF
        self.RG = RG
        self.telefone = telefone
        self.email = email
        self.renda = renda
        self.depinicial = depinicial

    def getCliente(self):
        return self.nome, self.CPF, self.RG, self.telefone, self.email, self.renda, self.depinicial

    def setNome(self, x):
        self.nome = x

    def setCPF(self, x):
        self.CPF = x

    def setRG(self, x):
        self.RG = x

    def setTelefone(self, x):
        self.telefone = x

    def setEmail(self, x):
        self.email = x

    def setRenda(self, x):
        self.renda = x

    def setDepinicial(self, x):
        self.depinicial = x
class Agencia:
    def __init__(self, nome):
        self.Cliente = []

    def novo_cliente(self, nome, saldo_inicial = 0):
        registrar_cliente = Cliente(nome, saldo_inicial)
        self.Cliente.append(registrar_cliente)


class ContaBancaria:
    # Construtor da classe, inicia com o nome do titular e saldo (opcional, padrão 0)
    def __init__(self, nome, saldo=0):
        self.nome = nome 
        self.saldo = saldo 

    # Método para depositar dinheiro na conta
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Valor de depósito inválido.")
