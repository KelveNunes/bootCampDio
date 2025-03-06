from interfaces import Transacao


class Saque(Transacao):

    def __init__(self, valor):
        
        self._valor = valor