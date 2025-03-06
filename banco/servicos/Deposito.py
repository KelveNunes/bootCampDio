from interfaces import Transacao


class Deposito(Transacao):

    def __init__(self, valor):
        
        self._valor = valor