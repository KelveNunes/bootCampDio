from entidades import Cliente, Conta
from servicos import Historico


class Conta_corrente(Conta):

    def __init__(self, saldo, numero, agencia, cliente: Cliente, historico: Historico, limite, limite_saque):
        
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite = limite,
        self._limite_saque = limite_saque