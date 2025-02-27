lista_user = {}
contas = {}

def deposito(valor, cpf, numero_conta):
    if valor <= 0:
        print('Você não pode depositar valores iguais ou menores que 0!!')
    else:
        if cpf in lista_user and numero_conta in contas:
            contas[numero_conta]["saldo"] += valor
            contas[numero_conta]["depositos"].append(valor)
            print(f'Depósito de R${valor:.2f} realizado com sucesso!')
        else:
            print('CPF ou número da conta inválido.')

def saque(valor_saque, cpf, numero_conta):
    if cpf in lista_user and numero_conta in contas:
        conta = contas[numero_conta]

        if conta["saldo"] <= 0:
            print('Essa conta não possui saldo. Impossível sacar!!')
        elif conta["limite_saque"] == 0:
            print('Limite de saque diário atingido.')
        elif valor_saque > 500:
            print('Não é permitido sacar mais que R$ 500 por dia.')
        elif valor_saque > conta["saldo"]:
            print(f'O valor do saque é maior que o saldo disponível em conta. Saldo: R${conta["saldo"]:.2f}')
        elif conta["limite_valor_saldo"] < valor_saque:
            print('Você só pode sacar R$ 500 por dia.')
        else:
            conta["saldo"] -= valor_saque
            conta["limite_saque"] -= 1
            conta["limite_valor_saldo"] -= valor_saque
            conta["saques"].append(valor_saque)
            print('Saque feito com sucesso.')
    else:
        print('CPF ou número da conta inválido.')

def extrato(cpf, numero_conta):
    if cpf in lista_user and numero_conta in contas:
        conta = contas[numero_conta]
        print(f'Saldo: R${conta["saldo"]:.2f}')
        print('Depósitos:')
        for deposito in conta["depositos"]:
            print(f'R${deposito:.2f}')
        print('Saques:')
        for saque in conta["saques"]:
            print(f'R${saque:.2f}')
    else:
        print('CPF ou número da conta inválido.')

def exibir_menu_conta():
    return int(input('''
        Escolha uma das opções da conta:
        1 - Depositar
        2 - Sacar
        3 - Extrato
        4 - Criar usuário
        5 - Criar conta
        0 - Parar operação
    '''))

def new_user():
    print('Digite as informações do usuário:\n')
    nome = input('Nome: \n')
    data_nascimento = input('Data de nascimento: \n')
    cpf = input('CPF: \n')  
    endereco = input('Endereço: \n')

    new_user = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco,
    }
    lista_user[cpf] = new_user
    print('Usuário cadastrado com sucesso!')

def nova_conta_corrente(cpf):
    if cpf in lista_user:
        numero_conta = len(contas) + 1
        agencia = '0001'
        nome = lista_user[cpf]["nome"]

        new_acount = {
            "agencia": agencia,
            "nome": nome,
            "saques": [],
            "depositos": [],
            "saldo": 0,
            "limite_saque": 3,
            "limite_valor_saldo": 500
        }
        contas[numero_conta] = new_acount
        print(f'Conta corrente {numero_conta} criada com sucesso para o CPF {cpf}.')
    else:
        print('Você precisa cadastrar um usuário antes.')

def main():
    while True:
        opcao = exibir_menu_conta()

        if opcao == 1:
            cpf = input('Qual o seu CPF? ')
            numero_conta = int(input('Qual o número da conta? '))
            valor = float(input('Quanto você deseja depositar? '))
            deposito(valor, cpf, numero_conta)
        elif opcao == 2:
            cpf = input('Qual o seu CPF? ')
            numero_conta = int(input('Qual o número da conta? '))
            valor = float(input('Quanto você deseja sacar? '))
            saque(valor, cpf, numero_conta)
        elif opcao == 3:
            cpf = input('Qual o seu CPF? ')
            numero_conta = int(input('Qual o número da conta? '))
            extrato(cpf, numero_conta)
        elif opcao == 4:
            new_user()
        elif opcao == 5:
            cpf = input('Digite o CPF para criar uma nova conta: ')
            nova_conta_corrente(cpf)
        elif opcao == 0:
            print('Finalizado.')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()