import re
import uuid

class FolhaPagamento:
    def __init__(self, funcionarioId, dataPagamento, salarioBase, bonus, deducoes):
        self.__pagamentoId= self.gerador_id()
        self.__funcionarioId= funcionarioId
        self.__dataPagamento= dataPagamento
        self.__bonus= bonus
        self.__deducoes= deducoes
        self.__salarioBase= salarioBase
        self.__salarioLiquido= 0

    def gerador_id(self):
        id_gerado = uuid.uuid4()
        str_id = str(id_gerado).replace('-','') # Retira os hífens
        troca_id = str_id[:6]
        numero_id = re.sub(r'\D', '', troca_id)
        id = 19 + int(numero_id)
        
        return id
    


    def calcularHoraExtra(self):
        valorhora=self.salarioBase/220

        if self.horas > 8:
            return (self.horas - 8) * (valorhora * 1.5)
        else:
            return 0
        
    def calcular_salario(self):
        self.salarioLiquido = self.salarioBase + self.bonus - self.deducoes
        return self.salarioLiquido  
    

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