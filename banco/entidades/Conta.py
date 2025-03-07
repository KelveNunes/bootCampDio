
from entidades import Cliente
from servicos import Historico


class Conta():
    
    def __init__(self, saldo, numero, agencia, cliente: Cliente, historico: Historico):

        
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico
    
    def saldo(self):

        print(f"o seu saldo é {self._saldo}")
        
    @classmethod
    def nova_conta(cls, cliente, numero):
    
        return cls(saldo=0, numero=numero, cliente=cliente, historico=Historico())
    
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
            
        
        