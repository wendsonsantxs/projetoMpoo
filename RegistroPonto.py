import uuid
import re

class RegistroPonto:
    def __init__(self, funcionarioId, data, horaEntrada, horaSaida, horasTrabalhadas):
        self.id= self.gerador_id()
        self.funcionarioId= funcionarioId
        self.data= data
        self.horaEntrada= horaEntrada
        self.horaSaida= horaSaida
        self.horasTrabalhadas= horasTrabalhadas
        
    def gerador_id(self):
        id_gerado = uuid.uuid4()
        str_id = str(id_gerado).replace('-','') # Retira os hífens
        troca_id = str_id[:6]
        numero_id = re.sub(r'\D', '', troca_id)
        id = 83 + numero_id
        
        return id