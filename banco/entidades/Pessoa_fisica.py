from entidades import Cliente


class Pessoa_fisica(Cliente):
    
    def __init__(self, endereco, contas, cpf, nome, data_nascimento):
        
        super().__init__(endereco, contas)
        self._cpf = cpf,
        self._nome = nome
        self._data_nascimento = data_nascimento
    
