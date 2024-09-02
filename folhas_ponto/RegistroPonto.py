import uuid
import re

class RegistroPonto:
    def __init__(self, funcionarioId, data, horaEntrada, horaSaida, horasTrabalhadas):
        self.__pontoId= self.gerador_id()
        #self.__funcionarioId= funcionarioId
        self.__data= data
        self.__horaEntrada= horaEntrada
        self.__horaSaida= horaSaida
        self.__horasTrabalhadas= horasTrabalhadas
        
    def gerador_id(self):
        id_gerado = uuid.uuid4()
        str_id = str(id_gerado).replace('-','') # Retira os hífens
        troca_id = str_id[:6]
        numero_id = re.sub(r'\D', '', troca_id)
        id = 83 + numero_id
        
        return id
    
    @property
    def data(self):
        return self.__data
    
    @property
    def horaEntrada(self):
        return self.__horaEntrada
    
    @property
    def horaSaida(self):
        return self.__horaSaida