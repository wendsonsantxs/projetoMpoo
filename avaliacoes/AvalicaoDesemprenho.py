import uuid
import re

class AvaliacaoDesempenho:
    def __init__(self, funcionarioId, dataAvalicao, feedback):
        self.__avaliacaoId= self.gerador_id()
        self.__funcionarioId= funcionarioId
        self.__dataAvaliacao= dataAvalicao
        self.__feedback= feedback
        
    def gerador_id(self):
        id_gerado = uuid.uuid4()
        str_id = str(id_gerado).replace('-','') # Retira os hífens
        troca_id = str_id[:6]
        numero_id = re.sub(r'\D', '', troca_id)
        id = 293 + numero_id
        
        return id
    
    @property
    def avaliacaoId(self):
        return self.__avaliacaoId
    
    @property
    def funcionarioid(self):
        return self.__funcionarioId
    
    @property
    def dataAvaliacao(self):
        return self.__dataAvaliacao
    
    @dataAvaliacao.setter
    def dataAvaliacao(self, novaData):
        temp = self.__dataAvaliacao
        if temp != novaData:
            self.__dataAvaliacao = novaData
        else:
            raise ValueError('O valor não pode ser igual')
        
    @property
    def feedback(self):
        return self.__feedback
    
    @feedback.setter
    def feeedback(self, novoFeedback):
        self.__feedback = novoFeedback