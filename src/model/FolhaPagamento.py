from utils.util import Util
from utils.env import Env

import sqlite3

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
