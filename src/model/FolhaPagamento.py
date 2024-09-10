from utils.util import Util

class FolhaPagamento:
    def __init__(self, funcionarioId, dataPagamento, salarioBase, bonus, deducoes):
        self.__pagamentoId= Util.gerador_id(6, 19)
        self.__funcionarioId= funcionarioId
        self.__dataPagamento= dataPagamento
        self.__bonus= bonus
        self.__deducoes= deducoes
        self.__salarioBase= salarioBase
        self.__salarioLiquido = self.calcular_salario()

    def calcularHoraExtra(self):
        valorhora=self.salarioBase/220

        if self.horas > 8:
            return (self.horas - 8) * (valorhora * 1.5)
        else:
            return 0
        
    def calcular_salario(self):
        salarioLiquido = self.salarioBase + self.bonus - self.deducoes
        return salarioLiquido  
    

    @property
    def pagamentoId(self):
        return self.__pagamentoId
    @pagamentoId.setter
    def pagamentoId(self, novoId):
        self.__pagamentoId = novoId

    @property
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
    
    @property
    def deducoes(self):
        return self.__deducoes
    
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
