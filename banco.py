from tokenize import Double


conta = 1000
depositos = []
limite_saque = 0
limite_valor_saque = 0
saques = []

def deposito(valor,cpf,numero_conta):
    global conta
    if valor <= 0:
        print('Você não pode depositar valores iguais ou menores que 0!!')
    else:
        conta += valor
        depositos.append(valor)
        print(f'Depósito de R${valor:.2f} realizado com sucesso!')
    return conta
        

def saque(valor_saque,cpf,numero_conta):

    global conta
    global limite_saque
    global limite_valor_saque

    if conta <=0:
        print('essa conta não possui saldo. Impossivel sacar!!')
    elif limite_saque==3:
        print('limite de saque diario atingido')
    elif valor_saque >500:
        print('não é permitido sacar mais que 500 por dia')    
    elif valor_saque >conta:
        print(f'o valor do saque é maior que o saldo disponivel em conta. saldo=  {conta}')
    elif limite_valor_saque>=500:
        print('Você só pode sacar 500 por dia')
    
    else:
        conta-=valor_saque
        limite_saque+=1
        limite_valor_saque+=valor_saque
        saques.append(valor_saque)

    
    return limite_saque,conta,limite_valor_saque
    
   
def extrato(cpf,numero_conta):
    print(f'Saldo: R${conta:.2f}')
    print('Depósitos:')
    for deposito in depositos:
        print(f'R${deposito:.2f}')
    print('Saques:')
    for saque in saques:
        print(f'R${saque:.2f}')

def exibir_menu_conta():
    return int(input( '''
        escolha umas das opções da conta:
        1 - depositar
        2 - sacar
        3 - extrato
        4 - criar usuario
        5 - criar conta
        0 - parar operação
    '''))

lista_user = {}
def new_user():

    print('digite as informações de usuario!\n' )
    nome = input('nome: \n' )
    data_nascimento = input('data de nascimento: \n' )
    cpf = int(input('CPF: \n' ))
    endereco = input('endereço: \n' )

    new_user = {
        "nome":nome,
        "data_nascimento":data_nascimento,
        "endereco":endereco,
    }
    lista_user[cpf] = new_user
    print('Usuário cadastrado com sucesso!')

contas = {}
def nova_conta_corrente(cpf):

    if cpf in lista_user:
    
        numero_conta = len(contas)+1
        agencia = '0001'
        nome = lista_user[cpf]["nome"]

        new_acount = {
           "agencia": agencia,
           "nome": nome,
        }
        contas[numero_conta] = new_acount
        print(f'Conta corrente {numero_conta} criada com sucesso para o CPF {cpf}.')
    else:
        print('Você precisa cadastrar um usuario antes')


def main():
    
    while True:
        opcao = exibir_menu_conta()

        if opcao == 1:
            valor = float(input('Quanto você deseja depositar? '))
            deposito(valor)
        elif opcao == 2:
            valor = float(input('Quanto você deseja sacar? '))
            saque(valor)
        elif opcao == 3:
            extrato()
        elif opcao == 4:
            new_user()
        elif opcao == 5:
            cpf = int(input('digite o cpf para criar uma nova conta: '))
            nova_conta_corrente(cpf)
        elif opcao == 0:
            print('finalizado.')
            break
        else:
            print('Opção inválida. Tente novamente.')
            

if __name__ == "__main__":
    main()
