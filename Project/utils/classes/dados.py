class Conta:
    def __init__(self, nome='Usuário', numero=0, saldo=0):
        """
        Representa uma conta bancária simples.
        Armazena o nome do titular, o número da conta e o saldo.
        Permite fazer depósitos e saques.
        """
        #attributes
        """Inicializa a conta com os dados informados."""
        self.nome = nome
        self.numero = numero
        self.saldo = saldo
    #methods
    def deposito(self, valor):
        """Adiciona `valor` ao saldo da conta."""
        self.saldo += valor
        
    def saque (self, valor):
        """Subtrai `valor` do saldo da conta."""
        self.saldo -= valor
        
    def __str__(self):
        return f'Usuário: {self.nome}\ncom número da conta: {self.numero}\npossui saldo: {self.saldo}'
    
    def __getstate__(self):
        return f'Estado: \nNome = {self.nome}\nNúmero = {self.numero}\nSaldo = {self.saldo}'