class Cliente:
    # criação do cliente contendo uas informações
    def __init__(self, nome, CPF, RG, telefone, email, renda, depinicial, saldo=0):
        self.nome = nome
        self.CPF = CPF
        self.RG = RG
        self.telefone = telefone
        self.email = email
        self.renda = renda
        self.depinicial = depinicial
        self.saldo = saldo

    # retorna todas as informações do cliente
    def getCliente(self):
        return self.nome, self.CPF, self.RG, self.telefone, self.email, self.renda, self.depinicial, self.saldo
    
    # edita a informação "nome" do cliente
    def setNome(self, x):
        self.nome = x

    # edita a informação "CPF" do cliente
    def setCPF(self, x):
        self.CPF = x

    # edita a informação "RG" do cliente
    def setRG(self, x):
        self.RG = x

    # edita a informação "telefone" do cliente
    def setTelefone(self, x):
        self.telefone = x

    # edita a informaçã "email" do cliente 
    def setEmail(self, x):
        self.email = x

    # edita o valor da renda do cliente
    def setRenda(self, x):
        self.renda = x

    # edita a iformação do depósito inicial do cliente
    def setDepinicial(self, x):
        self.depinicial = x

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

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



# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////



class Agencia:
    def __init__(self):
        self._cliente = []

    def novo_cliente(self, cliente):
        self._cliente.append(cliente)
        print("fulano foi adicionado")

    def excluir_cliente(self, cliente):
        if cliente in self._cliente:
            self._cliente.remove(cliente)
            print(f"O cliente {cliente} foi excluído")
        else:
            print("nome não registrado")

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Transferencia:
    
    def __init__(self, cliente, saldo):
        self._cliente = cliente
        self._saldo = saldo

    def detalhes(self):
        print(f'Cliente: {self._cliente} \nSaldo: {self._saldo} \nDeposito:{self._saldo}')

    def setSaldo(self, x):
        self._saldo = x
