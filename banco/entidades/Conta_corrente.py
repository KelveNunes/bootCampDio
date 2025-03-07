from servicos import Saque
from entidades import Conta



class Conta_corrente(Conta):

    def __init__(self, numero, cliente):

        
    
        super().__init__( numero, cliente)
        self._limite_numero_saque = 5
        self._limite_saque = 500
        

    def sacar(self, valor):

        numero_saque = len(
            [transacao for  transacao in self.historico.
            transacoes if transacao["tipo"] == Saque.__name__]
        )

        if valor > self._limite_saque:
            print(f'o limite de valor de saque da conta corrente é {self._limite_saque}')
        
        elif numero_saque == self._limite_numero_saque:
            print('você ja exedeu o numero de saques dessa conta por dia!!')
        
        else:
            super().sacar(valor)

        
        self._numero_saque += 1
        print(f'Novo saldo: R${self._saldo:.2f}')
        return False