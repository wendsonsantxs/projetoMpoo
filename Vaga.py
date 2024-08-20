import uuid
import re

class Vaga:
    def __init__(self, titulo, descricao, requisitos, dataPublicacao, status):
        self.id= self.gerador_id()
        self.titulo= titulo
        self.descricao= descricao
        self.requisitos= requisitos
        self.dataPublicacao= dataPublicacao
        self.status= status

    def gerador_id(self):
        id_gerado = uuid.uuid4()
        str_id = str(id_gerado).replace('-','') # Retira os hífens
        troca_id = str_id[:6]
        numero_id = re.sub(r'\D', '', troca_id)
        id = 12 + numero_id
        
        return id
        