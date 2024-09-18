from utils.util import Util
from utils.env import Env
from model.Treinamento import Treinamento
from model.RegistroPonto import RegistroPonto
from model.FolhaPagamento import FolhaPagamento

import sqlite3
import re
import requests

class Funcionario():
    def __init__(self):
        self._funcionarioId = Util.gerador_id(7, 27)
        self.__nome = None
        self.__cpf = None
        self.__email = None
        self.__telefone = None
        self.__dataNascimento = None
        self.__cargo = None
        self.__departamento = None
        self.__dataContratacao = None
        self.__salario = None
        self.__cep = None
        self.__endereco= None
        self.__numero= None
        self.__bairro= None
        self.__cidade= None

    def get_dados(self, nome, email, cpf, telefone, endereco, numero, bairro,
                  cidade, cep, cargo, departamento, salario, contratacao, data_nascimento):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep
        self.cargo = cargo
        self.departamento = departamento
        self.salario = salario
        self.dataContratacao = contratacao 
        self.dataNascimento = data_nascimento

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = self.verify_email(email)

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = Util.verify_cpf(cpf)

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = Util.verify_telefone(telefone)
    
    @property
    def cep(self):
        return self.__cep
    
    @cep.setter
    def cep(self, cep):
        self.__cep = self.verify_cep(cep)

    @property
    def dataNascimento(self):
        return self.__dataNascimento
    
    @dataNascimento.setter
    def dataNascimento(self, data_nascimento):
        self.__dataNascimento = Util.verify_data(data_nascimento)

    @property
    def cargo(self):
        return self.__cargo
    
    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo

    @property
    def departamento(self):
        return self.__departamento
    
    @departamento.setter
    def departamento(self, departamento):
        self.__departamento = departamento

    @property
    def dataContratacao(self):
        return self.__dataContratacao
    
    @dataContratacao.setter
    def dataContratacao(self, data_contratacao):
        self.__dataContratacao = Util.verify_data(data_contratacao)

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def bairro(self):
        return self.__bairro
    
    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    @property
    def cidade(self):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    def adicionar_funcionario(self):

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
            ''',(self._funcionarioId, self.__nome, self.__cpf, self.__email, self.__dataNascimento, self.__telefone, self.__cep,
                    self.__endereco, self.__numero, self.__bairro, self.__cidade, self.__cargo,
                    self.__departamento, self.__dataContratacao, self.__salario))
            
            conn.commit()
            conn.close()

            print("Funcionário adicionado com sucesso!")

        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")

    def verify_cep(self, cep):
        if not re.match(r'^\d{5}\-\d{3}$', cep):
            raise ValueError(f'CEP Inválido - {cep}')
        
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/') # Faz uma requisição para a API do ViaCEP para validar se o CEP é real
        if response.status_code != 200 or 'erro' in response.json():
            raise ValueError('CEP Inválido')

        return cep
    
        
    def verify_email(self, email):
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email): # Verifica se o email é válido
            raise ValueError('Email inválido')
        
        return email
                  
    @classmethod
    def get_funcionario(cls, funcionario_id):
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

    def folhaPagamento(self, dataPagamento, salarioBase, bonus, deducoes):
        if not self.verificarExistenciaId(self.funcionarioId):
            raise ValueError('Funcionário não encontrado')
        else:
            folhaPagamento = FolhaPagamento(self.funcionarioId, dataPagamento, salarioBase, bonus, deducoes)
            folhaPagamento.calcular_salario_liquido()
            folhaPagamento.adicionar_folha_pagamento_bd()


    def regstroPonto(self):
        if not self.verificarExistenciaId(self.funcionarioId):
            raise ValueError('Funcionário não encontrado')
        else:
            ponto = RegistroPonto(self.funcionarioId)
            ponto.registrar_entrada()
            ponto.registrar_saida()
            ponto.calcular_horas_trabalhadas()
            ponto.adicionarPontoBd()


    def treinar(self,titulo, descricao, participantes, data_inicio, data_fim, duracao):
        if not self.verificarExistenciaId(self.funcionarioId):
            raise ValueError('Funcionário não encontrado')
        else:
            treinamento = Treinamento(titulo, descricao, participantes, data_inicio, data_fim, duracao)
            treinamento.adicionar_participante(self.funcionarioId)  

    def delete_funcionario(self, id):
        conn = sqlite3.connect(Env.DATABASE_FUNCIONARIO)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM funcionarios WHERE funcionarioId=?", (id,))
        conn.commit()
        conn.close()

        #apaga os registros de ponto
        connPonto = sqlite3.connect(Env.DATABASE_PONTO)
        cursorPonto = connPonto.cursor()
        cursorPonto.execute("DELETE FROM pontos WHERE funcionario_id=?", (id,))
        connPonto.commit()
        connPonto.close()

        #apaga os registros de folha de pagamento
        connFolha = sqlite3.connect(Env.DATABASE_PAGAMENTO)
        cursorFolha = connFolha.cursor()
        cursorFolha.execute("DELETE FROM folha_pagamento WHERE funcionario_id=?", (id,))
        connFolha.commit()
        connFolha.close()

        #apaga os registros de treinamento
        connTreinamento = sqlite3.connect(Env.DATABASE_TREINAMENTOS)
        cursorTreinamento = connTreinamento.cursor()
        cursorTreinamento.execute("DELETE FROM treinamentos WHERE funcionario_id=?", (id,))
        connTreinamento.commit()
        connTreinamento.close()

        print("Funcionário deletado com sucesso!")
