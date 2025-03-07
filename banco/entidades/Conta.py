
from entidades import Cliente
from servicos import Historico


class Conta():
    
    def __init__(self, numero, cliente):

        
        self._saldo = 0
        self._numero = numero
        self._agencia = '001'
        self._cliente = cliente
        self._historico = Historico()
   
    @classmethod
    def nova_conta(cls, numero, cliente):
    
        return cls(numero, cliente)
    
    @property
    def saldo(self):

        return self._saldo
    
    @property
    def numero(self):

        return self._numero
    
    @property
    def agencia(self):

        return self._agencia
    
    @property
    def cliente(self):

        return self._cliente
    
    @property
    def historico(self):

        return self._historico
    
    def sacar(self, valor): 

        if valor <= 0:
            print('você não pode sacar valores menores que 0!!')
            return False
           
        elif valor > self._saldo:
            print(f'O valor do saque é maior que o saldo disponível em conta." O seu saldo é: {self._saldo}")')
            return False
            
        else:
            self._saldo -= valor
            return True

    def depositar(self, valor):

        if valor <= 0:
            print('Você não pode depositar valores iguais ou menores que 0!!')
            return False
        else:
            self._saldo += valor
            return True
            
        
        