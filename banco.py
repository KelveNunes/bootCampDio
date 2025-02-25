conta = 0
depositos = []
def deposito(deposito):

    global conta

    if deposito <=0:
        print('você não pode depositar valores iguais ou menores que 0!!')
    else:
        conta+deposito
        depositos.append(deposito)
    return conta    
        

def saque(valor_saque):

    global conta

    if conta <=0:
        print('essa conta não possui saldo. Impossivel sacar!!')
    elif valor_saque >conta:
        print('o valor do saque é maior que o saque. disponivel em conta = {conta}')
    else:
        conta-valor_saque
    return conta
   
def estrato(conta):

    print('saldo= {conta}')
    print('depositos= ')
    for deposito in depositos:
        print(deposito'\n')
