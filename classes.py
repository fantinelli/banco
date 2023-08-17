class Cliente:
    # Criação do cliente contendo suas informações
    def __init__(self, nome, CPF, RG, telefone, email, renda, depinicial, saldo=0):
        self.nome = nome
        self.CPF = CPF
        self.RG = RG
        self.telefone = telefone
        self.email = email
        self.renda = renda
        self.depinicial = depinicial
        self.saldo = saldo

    # Retorna todas as informações do cliente
    def getCliente(self):
        return self.nome, self.CPF, self.RG, self.telefone, self.email, self.renda, self.depinicial, self.saldo
    
    # Edita a informação "nome" do cliente
    def setNome(self, x):
        self.nome = x

    # Edita a informação "CPF" do cliente
    def setCPF(self, x):
        self.CPF = x

    # Edita a informação "RG" do cliente
    def setRG(self, x):
        self.RG = x

    # Edita a informação "telefone" do cliente
    def setTelefone(self, x):
        self.telefone = x

    # Edita a informação "email" do cliente 
    def setEmail(self, x):
        self.email = x

class Agencia:
    def __init__(self):
        self._cliente = []

    def novo_cliente(self, cliente):
        self._cliente.append(cliente)
        print(f"{cliente} foi adicionado")

    def excluir_cliente(self, cliente):
        if cliente in self._cliente:
            self._cliente.remove(cliente)
            print(f"O cliente {cliente} foi excluído")
        else:
            print("nome não registrado")




# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # Método para depositar dinheiro na conta
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

    # Método para sacar dinheiro da conta
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")
    
        # Método para consultar o saldo atual da conta
    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Transferencia:
    
    def __init__(self, cliente, saldo):
        self._cliente = cliente
        self._saldo = saldo
        self._enviado = 0
        self._recebido = 0
        
        # Metodo para receber o dinheiro
    def deposito(self, valor):
        self._saldo += valor 
        self._recebido += valor
        
        # Metodo para enviar o dinheiro
    def saque(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            self._enviado += valor
        else:
            print("Saldo Insuficiente")
            
        # Metodo para mostrar os detalhes da transação/transferência
    def detalhes(self):
        print(f'Cliente: {self._cliente}\nSaldo: {self._saldo}')
        if self._enviado > 0:
            print(f"Sua transferência foi enviada! - {self._enviado}")
        if self._recebido > 0:
            print(f"Sua transferência foi recebida! - {self._recebido}")
        print()
