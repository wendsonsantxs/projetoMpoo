import uuid
import re

class AvaliacaoDesempenho:
    def __init__(self, funcionarioId, dataAvalicao, feedback):
        self.id= self.gerador_id()
        self.funcionarioId= funcionarioId
        self.dataAvaliacao= dataAvalicao
        self.feedback= feedback
        
    def gerador_id(self):
        id_gerado = uuid.uuid4()
        str_id = str(id_gerado).replace('-','') # Retira os hífens
        troca_id = str_id[:6]
        numero_id = re.sub(r'\D', '', troca_id)
        id = 293 + numero_id
        
        return id