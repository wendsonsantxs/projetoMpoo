import sqlite3
import re
import uuid
import requests
class Funcionario():
    def __init__(self,nome, cpf, email, telefone, cep, rua, numero, bairro, cidade, cargo, data_contratacao, salario):
        self.funcionarioId = self.gerador_id()
        self.__nome= nome
        self.__cpf = self.verifica_cpf(cpf)
        self.__email= self.valida_email(email)
        self.__telefone= self.verifica_telefone(telefone)
        self.__cargo= cargo
        self.__dataContratacao= data_contratacao
        self.__salario= salario
        self.__cep = self.verifica_cep(cep)
        self.__rua= rua
        self.__numero= numero
        self.__bairro= bairro
        self.__cidade= cidade
        
    def gerador_id(self):
        id_gerado = uuid.uuid4()
        str_id = str(id_gerado).replace('-','') # Retira os hífens
        troca_id = str_id[:7]
        numero_id = re.sub(r'\D', '', troca_id)
        id = 201 + numero_id
        
        return id
    
    def verifica_cep(self, cep):
        if not re.match(r'^\d{5}\-\d{3}$', cep):
            raise ValueError(f'CEP inválido - {cep}')
        
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/') # Faz uma requisição para a API do ViaCEP para validar se o CEP é real
        if response.status_code != 200 or 'erro' in response.json():
            raise ValueError('CEP não encontrado')

        return cep
    
    @property
    def endereco(self):
        return {
            'cep': self.__cep,
            'rua': self.__rua,
            'numero': self.__numero,
            'bairro': self.__bairro,
            'cidade': self.__cidade
        }
    
    @endereco.setter
    def endereco(self, novo_enderco):
        if not novo_enderco:
            raise ValueError('Endereço não pode ser vazio')
        
        if 'cep' not in novo_enderco:
            raise ValueError('CEP não pode ser vazio')
        else:
            self.__cep = self.verifica_cep(novo_enderco['cep'])

            if 'rua' and 'numero' and 'bairro' and 'cidade' not in novo_enderco:
                raise ValueError('Endereço incompleto')
            else:
                self.__rua = novo_enderco['rua']
                self.__numero = novo_enderco['numero']
                self.__bairro = novo_enderco['bairro']
                self.__cidade = novo_enderco['cidade']

    def verifica_cpf(self, cpf):
        temp_cpf = re.sub(r'\D', '', cpf)

        if len(temp_cpf) != 11: # Verifica se o CPF tem 11 dígitos
            raise ValueError('CPF deve ter 11 dígitos')
        
        if temp_cpf == temp_cpf[0] * 11: # Verifica se os dígitos são iguais
            raise ValueError('CPF inválido')
        
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        primeiro_digito = (soma * 10 % 11) % 10
    
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        segundo_digito = (soma * 10 % 11) % 10

        if not temp_cpf[-2:] == f"{primeiro_digito}{segundo_digito}":
            raise ValueError('CPF inválido')
        else:
            return cpf
        
    @property
    def cpf(self):
        return self.__cpf
    
    def valida_email(self, email):
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email): # Verifica se o email é válido
            raise ValueError('Email inválido')
        
        return email
        
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, novo_email):
        temp = self.__email
        if temp != novo_email:
            self.__email = self.valida_email(novo_email)
        else:
            raise ValueError('E-mail já cadastrado anteriormente')

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        temp = self.__nome
        if temp != novo_nome:
            self.__nome = novo_nome
        else:
            raise ValueError('Nome já cadastrado anteriormente')
        
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, novo_telefone):
        temp = self.__telefone
        if temp != self.__telefone:
            self.__telefone = self.verifica_telefone(novo_telefone)
        else:
            raise ValueError('telefone já cadastrado anteriormente')
        
    def verifica_telefone(self, telefone):
        temp = re.sub(r'\D', '', telefone)

        if len(temp) == 11:
            if temp == temp[0]* 11:
                raise ValueError('O número de telefone não pode ser de um número só')
            else:
                return telefone
        else:
            raise ValueError('O número de telefone deve conter 11 dígitos')
        
    @property
    def cargo(self):
        return self.__cargo
    
    @cargo.setter
    def cargo(self, novo_cargo):
        self.__cargo = novo_cargo

    @property
    def data_contratacao(self):
        return self.__dataContratacao
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, novo_salario):
        self.__salario = novo_salario