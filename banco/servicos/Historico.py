import datetime
from interfaces import Transacao


class Historico(Transacao):
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao: Transacao):
        self.trasacoes.append(
            {
                'tipo': transacao.__class__.__name__,
                'valor': transacao.valor,
            }
        )