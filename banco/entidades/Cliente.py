from servicos import Deposito
from servicos import Saque
from entidades import Conta
from interfaces import Transacao


class Cliente():

    def __init__(self, endereco):
        
        self._endereco = endereco,
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)      
            
    def adicionar_conta(self, conta:Conta):
        self._contas.append(conta)