from utils.util import Util
from utils.env import Env

import sqlite3
import re
import requests

class Funcionario():
    def __init__(self,nome, email, cpf, telefone, endereco, numero, bairro, 
                                            cidade, cep, cargo, departamento, salario, contratacao, data_nascimento):
        self.funcionarioId = Util.gerador_id(7, 27)
        self.__nome = nome
        self.__cpf = self.verifica_cpf(cpf)
        self.__email = self.valida_email(email)
        self.__telefone = self.verifica_telefone(telefone)
        self.__dataNascimento = data_nascimento
        self.__cargo = cargo
        self.__departamento = departamento
        self.__dataContratacao= contratacao
        self.__salario= salario
        self.__cep = self.verifica_cep(cep)
        self.__endereco= endereco
        self.__numero= numero
        self.__bairro= bairro
        self.__cidade= cidade

    def adicionar_funcionario(self):
       # print(f'{self.funcionarioId}, {self.__nome}, {self.__cpf}, {self.__email}, {self.__telefone}, {self.__dataNascimento}, {self.__cargo}, {self.__departamento}, {self.__dataContratacao}, {self.__salario}, {self.__cep}, {self.__endereco}, {self.__bairro}')

        conn = sqlite3.connect(Env.DATABASE_FUNCIONARIO)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS funcionarios( 
                funcionarioId INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL,
                email TEXT NOT NULL,
                data_nascimento TEXT NOT NULL,
                telefone TEXT NOT NULL,
                cep TEXT NOT NULL,
                endereco TEXT NOT NULL,
                numero INTEGER NOT NULL,
                bairro TEXT NOT NULL,
                cidade TEXT NOT NULL,
                cargo TEXT NOT NULL,
                departamento TEXT NOT NULL,
                data_contratacao TEXT NOT NULL,
                salario REAL NOT NULL
            )
        ''')

        try:
            cursor.execute('''
                INSERT INTO funcionarios (funcionarioId, nome, cpf, email, data_nascimento, telefone, cep, endereco, 
                           numero, bairro, cidade, cargo, departamento, data_contratacao, salario)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            ''',(self.funcionarioId, self.__nome, self.__cpf, self.__email, self.__dataNascimento, self.__telefone, self.__cep,
                    self.__endereco, self.__numero, self.__bairro, self.__cidade, self.__cargo,
                    self.__departamento, self.__dataContratacao, self.__salario))
            
            conn.commit()
            conn.close()

            print("Funcionário adicionado com sucesso!")

        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")

    def verifica_cep(self, cep):
        if not re.match(r'^\d{5}\-\d{3}$', cep):
            raise ValueError(f'CEP inválido - {cep}')
        
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/') # Faz uma requisição para a API do ViaCEP para validar se o CEP é real
        if response.status_code != 200 or 'erro' in response.json():
            raise ValueError('CEP não encontrado')

        return cep
    
    
    def verifica_cpf(self, cpf):
        temp_cpf = re.sub(r'\D', '', cpf)
        try:

            if len(temp_cpf) != 11: # Verifica se o CPF tem 11 dígitos
                raise ValueError('CPF deve ter 11 dígitos')
            
            if temp_cpf == temp_cpf[0] * 11: # Verifica se os dígitos são iguais
                raise ValueError('CPF inválido')
            
            soma = sum(int(temp_cpf[i]) * (10 - i) for i in range(9))
            primeiro_digito = (soma * 10 % 11) % 10
        
            soma = sum(int(temp_cpf[i]) * (11 - i) for i in range(10))
            segundo_digito = (soma * 10 % 11) % 10

            if not temp_cpf[-2:] == f"{primeiro_digito}{segundo_digito}":
                raise ValueError('CPF inválido')
            else:
                return cpf
        except ValueError as e:
            print(e)
            return None
    
    
    def valida_email(self, email):
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email): # Verifica se o email é válido
            raise ValueError('Email inválido')
        
        return email
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def email(self):
        return self.__email
    

    @property
    def nome(self):
        return self.__nome
    
                
    def verifica_telefone(self, telefone):
        temp = re.sub(r'\D', '', telefone)

        if len(temp) == 11:
            if temp == temp[0]* 11:
                raise ValueError('O número de telefone não pode ser de um número só')
            else:
                return telefone
        else:
            raise ValueError('O número de telefone deve conter 11 dígitos')
        
   
    @classmethod
    def get_funcionario_by_id(cls, funcionario_id):
        """Recupera um funcionário do banco de dados pelo ID."""
        with sqlite3.connect('funcionarios.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM funcionarios WHERE funcionarioId=?", (funcionario_id,))
            row = cursor.fetchone()

        if row:
            funcionario = cls(
                nome=row[1],
                cpf=row[2],
                email=row[3],
                telefone=row[4],
                cep=row[5],
                rua=row[6],
                numero=row[7],
                bairro=row[8],
                cidade=row[9],
                cargo=row[10],
                data_contratacao=row[11],
                salario=row[12]
            )
            funcionario.id = row[0]
            return funcionario
        else:
            raise ValueError("Funcionário não encontrado")

    # def adicionar_avaliacao(self, data_avaliacao, feedback):
    #     """Adiciona uma avaliação de desempenho ao funcionário."""
    #     avaliacao = AvaliacaoDesempenho(self.id, data_avaliacao, feedback)
    #     self.avaliacoes.append(avaliacao)
    
    @property
    def cargo(self):
        return self.__cargo
    

    @property
    def data_contratacao(self):
        return self.__dataContratacao
    
    @property
    def salario(self):
        return self.__salario
    

    @property
    def cep(self):
        return self.__cep

    @property
    def endereco(self):
        return self.__endereco

    @property
    def numero(self):
        return self.__numero


    @property
    def bairro(self):
        return self.__bairro


    @property
    def cidade(self):
        return self.__cidade


    @property
    def endereco_completo(self):
        return f'{self.__endereco}, {self.__numero} - {self.__bairro}, {self.__cidade}'
    
    @property
    def departamento(self):
        return self.__departamento
    
    @departamento.setter
    def departamento(self, novo_departamento):
        self.__departamento = novo_departamento

    @property
    def data_nascimento(self):
        return self.__dataNascimento
    
    @property
    def endereco(self):
        return {
            'cep': self.__cep,
            'endereco': self.__endereco,
            'numero': self.__numero,
            'bairro': self.__bairro,
            'cidade': self.__cidade
        }

    @property
    def telefone(self):
        return self.__telefone
