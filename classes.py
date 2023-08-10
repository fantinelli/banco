class Cliente:
    def __init__(self, nome, sobrenome, CPF, RG, telefone, email, renda, depinicial):
        self.nome = nome
        self.sobrenome = sobrenome
        self.CPF = CPF
        self.RG = RG
        self.telefone = telefone
        self.email = email
        self.renda = renda
        self.depinicial = depinicial

    def getCliente(self):
        return self.nome, self.sobrenome, self.CPF, self.RG, self.telefone, self.email, self.renda, self.depinicial

    def setNome(self, x):
        self.nome = x

    def setSobrenome(self, x):
        self.sobrenome = x

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
