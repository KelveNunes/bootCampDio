from abc import ABC, abstractmethod
from entidades import Conta

class Transacao(ABC):

    @abstractmethod
    def registrar(self, conta: Conta):
        pass
        