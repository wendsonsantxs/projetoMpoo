import uuid
import re

class Treinamento:
    def __init__(self, titulo, descricao, dataInicio, dataFim, status):
        self.id= self.gerador_id()
        self.titulo = titulo
        self.descricao= descricao
        self.dataInicio= dataInicio
        self.dataFim= dataFim
        self.status= status

    def gerador_id(self):
        id_gerado = uuid.uuid4()
        str_id = str(id_gerado).replace('-','') # Retira os hífens
        troca_id = str_id[:8]
        numero_id = re.sub(r'\D', '', troca_id)
        id = 41 + numero_id
        
        return id
        