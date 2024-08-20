import uuid
import re

class Candidatura:
    def __init__(self, vagaId, candidatoNome, status):
        self.id= self.gerador_id()
        self.vagaId= vagaId
        self.candidatoNome= candidatoNome
        self.status= status
        
    def gerador_id(self):
        id_gerado = uuid.uuid4()
        str_id = str(id_gerado).replace('-','') # Retira os hífens
        troca_id = str_id[:6]
        numero_id = re.sub(r'\D', '', troca_id)
        id = 74 + numero_id
        
        return id