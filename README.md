# Sistema Bancário Simples

Este projeto é um sistema bancário simples desenvolvido em Python, que permite ao usuário realizar operações básicas de depósito, saque, consulta de extrato, criação de usuários e criação de contas correntes. O código foi estruturado para simular o funcionamento de uma conta bancária, com regras como limite de saques diários e valor máximo por saque.

## Funcionalidades

1. **Depósito**:
   - Permite ao usuário depositar valores na conta.
   - Valores devem ser maiores que zero.
   - O saldo da conta é atualizado e o depósito é registrado.

2. **Saque**:
   - Permite ao usuário sacar valores da conta, respeitando as seguintes regras:
     - Saldo disponível na conta.
     - Limite de 3 saques por dia.
     - Valor máximo de R$ 500,00 por saque e R$ 500,00 no total diário.
   - O saldo da conta é atualizado e o saque é registrado.

3. **Extrato**:
   - Exibe o saldo atual da conta.
   - Lista todos os depósitos e saques realizados.

4. **Criação de Usuário**:
   - Permite ao usuário cadastrar um novo usuário no sistema.
   - As informações solicitadas são: nome, data de nascimento, CPF e endereço.
   - O CPF é usado como identificador único do usuário.

5. **Criação de Conta Corrente**:
   - Permite ao usuário criar uma nova conta corrente vinculada a um CPF cadastrado.
   - Cada conta possui um número único, agência padrão "0001", e registros de saldo, saques e depósitos.
   - O limite de saques e o valor máximo diário são aplicados por conta.

6. **Menu Interativo**:
   - Oferece ao usuário um menu para escolher entre as operações disponíveis (depósito, saque, extrato, criação de usuário, criação de conta) ou encerrar o programa.

## Como Usar

1. Execute o script `python banco.py`.
2. Escolha uma das opções do menu:
   - **1**: Para depositar um valor.
   - **2**: Para sacar um valor.
   - **3**: Para visualizar o extrato.
   - **4**: Para criar um novo usuário.
   - **5**: Para criar uma nova conta corrente.
   - **0**: Para encerrar o programa.
3. Siga as instruções exibidas no terminal para realizar as operações desejadas.

