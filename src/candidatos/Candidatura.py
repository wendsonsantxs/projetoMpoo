import uuid
import re

class Candidatura:
    def __init__(self, vagaId, candidatoNome, status):
        self.__candidatoId= self.gerador_id()
        self.__vagaId= vagaId
        self.__candidatoNome= candidatoNome
        self.__status= status
        
    def gerador_id(self):
        id_gerado = uuid.uuid4()
        str_id = str(id_gerado).replace('-','') # Retira os hífens
        troca_id = str_id[:6]
        numero_id = re.sub(r'\D', '', troca_id)
        id = 74 + int(numero_id)
        
        return id
    
    def publicar_vaga(self):
        pass

    @property
    def candidatoId(self):
        return self.__candidatoId
    @candidatoId.setter
    def candidatoId(self, novoId):
        self.__candidatoId = novoId

    @property
    def vagaId(self):
        return self.__vagaId
    @vagaId.setter
    def vagaId(self, novoId):
        self.__vagaId = novoId

    @property
    def candidatoNome(self):
        return self.__candidatoNome
    @candidatoNome.setter
    def candidatoNome(self, novoNome):
        self.__candidatoNome = novoNome

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, novoStatus):
        self.__status = novoStatus
    