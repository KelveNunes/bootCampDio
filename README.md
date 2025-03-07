## Branch: `feature/modelagem-classes`

### Objetivo
Esta branch foi criada para **modelar as classes** do sistema com base no diagrama fornecido. O foco é estruturar as entidades e seus relacionamentos, garantindo que o código siga os princípios de orientação a objetos e seja escalável.

---

### Classes Modeladas

Abaixo estão as principais classes modeladas nesta branch, com base no diagrama fornecido:

---

#### 1. **Cliente**
Representa um cliente do sistema. Atributos e métodos incluem:
- **Atributos**:
  - `endereco`: Endereço do cliente.
  - `contas`: Lista de contas associadas ao cliente.
- **Métodos**:
  - `realizar_transacao(conta: Conta, transacao: Transacao)`: Realiza uma transação em uma conta específica.
  - `adicionar_conta(conta: Conta)`: Adiciona uma nova conta à lista de contas do cliente.

---

#### 2. **PessoaFisica** (Herda de `Cliente`)
Representa um cliente do tipo pessoa física. Atributos adicionais incluem:
- **Atributos**:
  - `cpf`: CPF do cliente (identificador único).
  - `nome`: Nome completo do cliente.
  - `data_nascimento`: Data de nascimento do cliente.

---

#### 3. **Conta**
Representa uma conta bancária. Atributos e métodos incluem:
- **Atributos**:
  - `saldo`: Saldo atual da conta.
  - `numero`: Número da conta.
  - `agencia`: Agência da conta.
  - `cliente`: Cliente associado à conta.
  - `historico`: Histórico de transações da conta.
- **Métodos**:
  - `saldo()`: Retorna o saldo atual da conta.
  - `nova_conta(cliente: Cliente, numero: int)`: Cria uma nova conta.
  - `sacar(valor: float)`: Realiza um saque na conta.
  - `depositar(valor: float)`: Realiza um depósito na conta.

---

#### 4. **ContaCorrente** (Herda de `Conta`)
Representa uma conta corrente, com limites específicos. Atributos adicionais incluem:
- **Atributos**:
  - `limite`: Limite de saque da conta.
  - `limite_saques`: Número máximo de saques permitidos.

---

#### 5. **Transacao** (Interface)
Representa uma transação genérica. Métodos incluem:
- **Métodos**:
  - `registrar(conta: Conta)`: Registra a transação na conta.

---

#### 6. **Deposito** (Implementa `Transacao`)
Representa uma transação de depósito. Atributos e métodos incluem:
- **Atributos**:
  - `valor`: Valor do depósito.
- **Métodos**:
  - `registrar(conta: Conta)`: Registra o depósito na conta.

---

#### 7. **Saque** (Implementa `Transacao`)
Representa uma transação de saque. Atributos e métodos incluem:
- **Atributos**:
  - `valor`: Valor do saque.
- **Métodos**:
  - `registrar(conta: Conta)`: Registra o saque na conta.

---

#### 8. **Historico**
Representa o histórico de transações de uma conta. Atributos e métodos incluem:
- **Atributos**:
  - `historico`: Lista de transações.
- **Métodos**:
  - `adicionar_transacao(transacao: Transacao)`: Adiciona uma transação ao histórico.

---

### Relacionamentos entre Classes

1. **Cliente** pode ter várias **Contas**.
2. **ContaCorrente** é uma especialização de **Conta**.
3. **Deposito** e **Saque** implementam a interface **Transacao**.
4. **Historico** está associado a uma **Conta** e armazena objetos do tipo **Transacao**.