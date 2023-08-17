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
    def __init__(self, cliente):
        self._cliente = []

    def novo_cliente(self, cliente):
        self._cliente.append(cliente)

    def excluir_cliente(self, cliente):
        if cliente in self._cliente:
            self._cliente.pop(cliente)


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

    # Método para sacar dinheiro da conta
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")
    

    
        # Método para consultar o saldo atual da conta
    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")
