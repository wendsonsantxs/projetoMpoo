from utils.util import Util
from utils.env import Env

import sqlite3

class FolhaPagamento:
    def __init__(self):
        self._pagamentoId= Util.gerador_id(6, 19)
        self.__funcionarioId = None
        self.__dataPagamento = None
        self.__bonus = None
        self.__deducoes = None
        self.__salarioBase = None
        self.__deducoes = None
        self.__salarioLiquido = None

    def get_dados(self, funcionarioId, dataPagamento, bonus, deducoes, salarioBase): #salarioLiquido
        self.funcionarioId = funcionarioId
        self.dataPagamento = dataPagamento
        self.bonus = bonus
        self.deducoes = deducoes
        self.salarioBase = salarioBase
        self.deducoes = self.calcularHoraExtra()

    @property
    def funcionarioId(self):
        return self.__funcionarioId
    
    @funcionarioId.setter
    def funcionarioId(self, funcionarioId):
        verify = Util.verify_existence(Env.DATABASE_FUNCIONARIO, 'funcionario', 'funcionarioId', funcionarioId)
        if verify:
            raise ValueError('Funcionário não existe')
        else:
            self.__funcionarioId = funcionarioId

    @property
    def dataPagamento(self):
        return self.__dataPagamento
    
    @dataPagamento.setter
    def dataPagamento(self, dataPagamento):
        self.__dataPagamento = Util.verify_data(dataPagamento)

    @property
    def bonus(self):
        return self.__bonus
    
    @bonus.setter
    def bonus(self, bonus):
        self.__bonus = bonus

    @property
    def deducoes(self):
        return self.__deducoes
    
    @deducoes.setter
    def deducoes(self, deducoes):
        self.__deducoes = deducoes

    @property
    def salarioBase(self):
        return self.__salarioBase
    
    @salarioBase.setter
    def salarioBase(self, salarioBase):
        self.__salarioBase = salarioBase

    @property
    def salarioLiquido(self):
        return self.__salarioLiquido
    
    @salarioLiquido.setter
    def salarioLiquido(self):
        self.__salarioLiquido = self.calcular_salario()


    def adicionar_folha_pagamento(self):
        conn = sqlite3.connect(Env.DATABASE_PAGAMENTO)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Folha_Pagamento( 
                Pagamento-Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Funcionario-Id TEXT NOT NULL,
                Data_Pagamento TEXT NOT NULL,
                salario_Base TEXT NOT NULL,
                Bonus TEXT NOT NULL,
                Deduções TEXT NOT NULL,
                Salario_Liquido TEXT NOT NULL
            )
        ''')
        try:
            cursor.execute('''
                INSERT INTO funcionarios (Pagamento-Id, Funcionario-Id, Data_Pagamento, salario_Base, Bonus, Deduções, Salario_Liquido)
                VALUES (?,?,?,?,?,?,?)
            ''',(self._pagamentoId, self.__funcionarioId, self.__dataPagamento, self.__salarioBase, self.__bonus, self.__deducoes, self.__salarioLiquido))
            
            conn.commit()
            conn.close()

            print("Candidato adicionado com sucesso!")

        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")

    def calcularHoraExtra(self):
        valorhora=self.salarioBase/220

        if self.horas > 8:
            return (self.horas - 8) * (valorhora * 1.5)
        else:
            return 0
        
    def calcular_salario(self):
        salarioLiquido = self.salarioBase + self.bonus - self.deducoes
        return salarioLiquido  
    

    @classmethod
    def get_folha_pagamento_by_id(cls, folha_pagamento_id):
        """Recupera uma folha de pagamento do banco de dados pelo ID."""
        conn = sqlite3.connect(Env.DATABASE_PAGAMENTO)
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
