# Sistema Bancário Simples

Este projeto é um sistema bancário simples desenvolvido em Python, que permite ao usuário realizar operações básicas de depósito, saque e consulta de extrato. O código foi estruturado para simular o funcionamento de uma conta bancária, com regras como limite de saques diários e valor máximo por saque.

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

4. **Menu Interativo**:
   - Oferece ao usuário um menu para escolher entre as operações disponíveis (depósito, saque, extrato) ou encerrar o programa.

## Como Usar

1. Execute o script `main.py`.
2. Escolha uma das opções do menu:
   - **1**: Para depositar um valor.
   - **2**: Para sacar um valor.
   - **3**: Para visualizar o extrato.
   - **0**: Para encerrar o programa.
3. Siga as instruções exibidas no terminal para realizar as operações desejadas.

## Exemplo de Uso

```bash
Escolha uma das opções da conta:
1 - Depositar
2 - Sacar
3 - Extrato
0 - Parar operação
1
Quanto você deseja depositar? 300
Depósito de R$300.00 realizado com sucesso!
