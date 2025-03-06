
from banco.entidades import Cliente
from banco.servicos import Historico


class Conta():
    
    def __init__(self, saldo, numero, agencia, cliente: Cliente, historico: Historico):

        self._saldo = saldo,
        self._numero = numero,
        self._agencia = agencia,
        self._cliente = cliente,
        self._historico = historico,
    
    def saldo(self): float
        
    def nova_conta(self): Conta
    
    def sacar(self): bool

    def depositar(self): bool

        
        
        