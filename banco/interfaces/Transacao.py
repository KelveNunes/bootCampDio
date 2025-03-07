from abc import ABC, abstractclassmethod, abstractmethod, abstractproperty
from entidades import Conta

class Transacao(ABC):

    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta: Conta): 
        pass
        
        