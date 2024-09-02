import re
import uuid

class FolhaPagamento:
    def __init__(self, funcionarioId, dataPagamento, salarioBase, bonus, deducoes, salarioLiquido):
        self.__pagamentoId= self.gerador_id()
        self.__funcionarioId= funcionarioId
        self.__dataPagamento= dataPagamento
        self.__bonus= bonus
        self.__deducoes= deducoes
        self.__salarioBase= salarioBase
        #self.__salarioLiquido= salarioLiquido

    def gerador_id(self):
        id_gerado = uuid.uuid4()
        str_id = str(id_gerado).replace('-','') # Retira os hífens
        troca_id = str_id[:6]
        numero_id = re.sub(r'\D', '', troca_id)
        id = 19 + numero_id
        
        return id
    
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