from entidades import Conta
from interfaces import Transacao


class Deposito(Transacao):

    def __init__(self, valor):
        
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta:Conta):
        transacao_realizada = conta.depositar(self.valor)

        if transacao_realizada:
            conta.historico.adicionar_transacao(self)