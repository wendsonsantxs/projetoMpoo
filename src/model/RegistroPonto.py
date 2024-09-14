from utils.util import Util
from datetime import datetime 

class RegistroPonto:
    def __init__(self, funcionarioId, data, horaEntrada, horaSaida, horasTrabalhadas):
        self.__pontoId= Util.gerador_id(6, 839)
        self.__funcionarioId= self.verificar_funcionario(funcionarioId)
        self.data= data
        self.__horaEntrada= horaEntrada
        self.__horaSaida= horaSaida
        self.__horasTrabalhadas= horasTrabalhadas
 

    def registrar_entrada(self):
        self.entrada = datetime.now()

    def registrar_saida(self):
        self.saida = datetime.now()

    def calcular_horas_trabalhadas(self):
        if self.entrada and self.saida:
            self.horasTrabalhadas = (self.saida - self.entrada).total_seconds() / 3600

    def verificar_funcionario(self):
        if self.funcionarioId > 0:
            return True
        else:
            return False
        

    def verificarHoraEntrada(self):
        if self.horaEntrada:
            return True
        else:
            return False
        
    def verificarHoraSaida(self):
        if self.horaSaida:
            return True
        else:
            return False
        
    @property
    def pontoId(self):
        return self.__pontoId
    
    @pontoId.setter
    def pontoId(self, novoId):
        self.__pontoId = novoId

    @property
    def horasTrabalhadas(self):
        return self.__horasTrabalhadas
    
    @horasTrabalhadas.setter
    def horasTrabalhadas(self, novaHora):
        self.__horasTrabalhadas = novaHora
    @property
    def funcionarioId(self):
        return self.__funcionarioId
    
    @funcionarioId.setter
    def funcionarioId(self, novoId):
        self.__funcionarioId = novoId

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, novaData):
        self.__data = novaData
    
    @property
    def horaEntrada(self):
        return self.__horaEntrada
    @horaEntrada.setter
    def horaEntrada(self, novaHora):
        self.__horaEntrada = novaHora
    
    @property
    def horaSaida(self):
        return self.__horaSaida
    @horaSaida.setter
    def horaSaida(self, novaHora):
        self.__horaSaida = novaHora
        