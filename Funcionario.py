from Endereco import *
class Funcionario(Endereco):
    def __init__(self,nome, email, telefone, rua, numero, bairro, cidade, cargo, dataContratacao, salario):
        super().__init__(rua, numero, bairro, cidade)
        self.nome= nome
        self.email= email
        self.telefone= telefone
        self.cargo= cargo
        self.dataContratacao= dataContratacao
        self.salario= salario