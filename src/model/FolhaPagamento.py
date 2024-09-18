import re
import sqlite3
from utils.env import Env
from utils.util import Util

class FolhaPagamento:
    def __init__(self, funcionarioId, dataPagamento, salarioBase, bonus, deducoes):
        self.__pagamentoId= Util.gerador_id(6, 19)
        self.__funcionarioId= self.verificarFuncionario(funcionarioId)
        self.dataPagamento= self.verificaData(dataPagamento)
        self.bonus= bonus
        self.deducoes= deducoes
        self.__salarioBase= self.verificarSalario(salarioBase)
        self.__salarioLiquido = self.calcular_salario()


    def adicionarFolhaPagamentoBd(self):
        conn= sqlite3.connect(Env.DATABASE_PAGAMENTO)
        cursor= conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS folha_pagamento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pagamento_id TEXT NOT NULL,
                funcionario_id TEXT NOT NULL,
                data_pagamento TEXT NOT NULL,
                salario_base TEXT NOT NULL,
                bonus TEXT NOT NULL,
                deducoes TEXT NOT NULL,
                salario_liquido TEXT NOT NULL
                       
            )
        """)
        try:
            cursor.execute('''
                INSERT INTO folha_pagamento (pagamento_id, funcionario_id, data_pagamento, salario_base, bonus, deducoes, salario_liquido)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (self.pagamentoId, self.funcionarioId, self.dataPagamento, self.salarioBase, self.bonus, self.deducoes, self.salarioLiquido))
            conn.commit()
            conn.close()
            print("Folha de pagamento adicionada com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")


    def verificarSalario(self, salarioBase):
        if salarioBase > 0:
            return salarioBase
        else:
            raise ValueError("Salário inválido")
    
    def calcularHoraExtra(self):
        valorhora=self.salarioBase/220

        if self.horas > 8:
            return (self.horas - 8) * (valorhora * 1.5)
        else:
            return 0
        
    def calcular_salario(self):
        salarioLiquido = self.salarioBase + self.bonus - self.deducoes
        return salarioLiquido  
    
    def verificaData(self, data):
        if not re.match(r'^\d{2}\/\d{2}\/\d{4}$', data):
            raise ValueError('Data inválida')
        return data
    
    def verificarPagamento(self):
        if self.salarioLiquido > 0:
            return True
        else:
            return False
        
    def verificarFuncionario(self):
        if self.funcionarioId > 0:
            return True
        else:
            return False
        

    def verificarSalario(self):
        if self.salarioBase > 0:
            return True
        else:
            return False


    @property
    def pagamentoId(self):
        return self.__pagamentoId
    
    @pagamentoId.setter
    def pagamentoId(self, novoId):
        self.__pagamentoId = novoId

    def funcionarioId(self):
        return self.__funcionarioId
    
    @funcionarioId.setter
    def funcionarioId(self, novoId):
        self.__funcionarioId = novoId

    @property
    def bonus(self):
       return self.__bonus
    
    @property
    def dataPagamento(self):
        return self.__dataPagamento
    
    @dataPagamento.setter
    def dataPagamentoi(self, novaData):
        self.__dataPagamento = novaData

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def salarioBase(self):
        return self.__salarioBase
    
    @salarioBase.setter
    def salarioBase(self, novoSalario):
        self.__salarioBase = novoSalario
    
    # @property
    # def deducoes(self):
    #     return self.__deducoes
    
    @salarioLiquido.setter
    def salarioLiquido(self, novoSalario):
        self.__salarioLiquido = novoSalario

    @property   
    def salarioLiquido(self):
        return self.__salarioLiquido
    
    @classmethod
    def get_folha_pagamento_by_id(cls, folha_pagamento_id):
        """Recupera uma folha de pagamento do banco de dados pelo ID."""
        conn = sqlite3.connect('funcionarios.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM folha_pagamento WHERE id=?", (folha_pagamento_id,))
        row = cursor.fetchone()

        conn.close()

        if row:
            folha_pagamento = cls(
                funcionario_id=row[1],
                data_pagamento=row[2],
                salario_base=row[3],
                bonus=row[4],
                deducoes=row[5]
            )
            folha_pagamento.id = row[0]
            return folha_pagamento
        else:
            raise ValueError(f"Folha de pagamento com ID {folha_pagamento_id} não encontrada.")
