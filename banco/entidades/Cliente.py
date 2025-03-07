from entidades import Conta
from interfaces import Transacao


class Cliente():

    def __init__(self, endereco, contas: list):
        
        self._endereco = endereco,
        self._contas = contas

    def realizar_transacao(self, conta:Conta, transacao: Transacao):
        
        


    def adicionar_conta(self, conta:Conta):
        pass