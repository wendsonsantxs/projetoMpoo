from utils.util import Util
from utils.env import Env
#from Treinamento import Treinamento
import sqlite3
import re
import requests

class Funcionario():
    def __init__(self,nome, email, cpf, telefone, endereco, numero, bairro, 
                                            cidade, cep, cargo, departamento, salario, contratacao, data_nascimento):
        self.__funcionarioId = Util.gerador_id(6, 24)
        self.__nome = self.verificaNome(nome)
        self.__cpf = self.verifica_cpf(cpf)
        self.__email = self.valida_email(email)
        self.__telefone = self.verifica_telefone(telefone)
        self.__dataNascimento = self.verificaDataNascimento(data_nascimento)
        self.cargo = cargo
        self.departamento = departamento
        self.dataContratacao= contratacao
        self.__salario= self.verificarSalario(salario)
        self.__cep = self.verifica_cep(cep)
        self.endereco= endereco
        self.numero= numero
        self.bairro= bairro
        self.cidade= cidade


    # def treinar(self, treinamento_id):
    #     """Adiciona um funcionário ao treinamento."""
    #     treinamento = Treinamento.get_treinamento_by_id(treinamento_id)
    #     treinamento.adicionar_participante(self.funcionarioId)  

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
            ''', (self.funcionarioId, self.nome, self.cpf, self.email, self.data_nascimento, self.telefone, self.cep, self.endereco, 
                  self.numero, self.bairro, self.cidade, self.cargo, self.departamento, self.dataContratacao, self.salario))
            
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
    
    def verificaDataNascimento(self, data):
        if not re.match(r'^\d{2}\/\d{2}\/\d{4}$', data):
            raise ValueError('Data de nascimento inválida')
        return data

    def verificaNome(self, nome):
        if not re.match(r'^[a-zA-Z\s]+$', nome):
            raise ValueError('Nome inválido')
        return nome
    
    def verificarSalario(self, salario):
        if float(salario)<0:
            raise ValueError('Salário inválido')
        return salario
    

    @property
    def endereco(self):
        return {
            'cep': self.__cep,
            'endereco': self.__endereco,
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

            if 'endereco' and 'numero' and 'bairro' and 'cidade' not in novo_enderco:
                raise ValueError('Endereço incompleto')
            else:
                self.__endereco = novo_enderco['endereco']
                self.__numero = novo_enderco['numero']
                self.__bairro = novo_enderco['bairro']
                self.__cidade = novo_enderco['cidade']

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
    
    @property
    def funcionarioId(self):
        return self.__funcionarioId
    
    @funcionarioId.setter
    def funcionarioId(self, novo_id):
        self.__funcionarioId = novo_id

    @property
    def cpf(self):
        return self.__cpf
    
    def valida_email(self, email):
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email): # Verifica se o email é válido
            raise ValueError('Email inválido')
        
        return email
    @cpf.setter
    def cpf(self, novo_cpf):
        temp = self.__cpf
        if temp != novo_cpf:
            self.__cpf = self.verifica_cpf(novo_cpf)
        else:
            raise ValueError('CPF já cadastrado anteriormente')
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

    @property
    def cep(self):
        return self.__cep
    @cep.setter
    def cep(self, novo_cep):
        self.__cep = self.verifica_cep(novo_cep)

    @property
    def endereco(self):
        return self.__endereco
    @endereco.setter
    def endereco(self, nova_endereco):
        self.__endereco = nova_endereco

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, novo_numero):
        self.__numero = novo_numero

    @property
    def bairro(self):
        return self.__bairro
    @bairro.setter
    def bairro(self, novo_bairro):
        self.__bairro = novo_bairro

    @property
    def cidade(self):
        return self.__cidade
    @cidade.setter
    def cidade(self, nova_cidade):
        self.__cidade = nova_cidade

    @property
    def endereco_completo(self):
        return f'{self.__endereco}, {self.__numero} - {self.__bairro}, {self.__cidade}'
    

    @property
    def data_nascimento(self):
        return self.__dataNascimento
    
    @data_nascimento.setter 
    def data_nascimento(self, nova_data):
        self.__dataNascimento = self.verificaDataNascimento(nova_data)

    @property
    def departamento(self):
        return self.__departamento
    
    @departamento.setter
    def departamento(self, novo_departamento):
        self.__departamento = novo_departamento

    @property
    def funcionarioId(self):
        return self.__funcionarioId

    @funcionarioId.setter
    def funcionarioId(self, novoId):
        self.__funcionarioId = novoId

    
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
    
    # def adicionar_historico_trabalho(self, cargo_anterior, departamento_anterior, data_inicio, data_fim):
    #     """Adiciona um registro ao histórico de trabalho do funcionário."""
    #     # historico = HistoricoTrabalho(self.id, cargo_anterior, departamento_anterior, data_inicio, data_fim)
    #     self.historico_trabalho.append(historico)

    # def adicionar_avaliacao(self, data_avaliacao, feedback):
    #     """Adiciona uma avaliação de desempenho ao funcionário."""
    #     avaliacao = AvaliacaoDesempenho(self.id, data_avaliacao, feedback)
    #     self.avaliacoes.append(avaliacao)



