from banco.entidades import Conta
from banco.interfaces import Transacao


class Cliente():

    def __init__(self, endereco, contas):
        
        self._endereco = endereco,
        self._contas = contas

    def realizar_transacao(conta:Conta, transacao: Transacao):
        pass

    def adicionar_conta(conta:Conta):
        pass