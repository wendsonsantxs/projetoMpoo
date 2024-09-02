import uuid
import re

class Treinamento:
    def __init__(self, titulo, descricao, dataInicio, duracao, dataFim):
        self.__treinamentoId = self.gerador_id()
        self.__titulo = titulo
        self.__descricao = descricao
        self.__dataInicio = dataInicio
        self.__dataFim = dataFim
        self.__duracao = duracao
        self.__participante = {}
        self.__status = self.status()

    def gerador_id(self):
        id_gerado = uuid.uuid4()
        str_id = str(id_gerado).replace('-','') # Retira os hífens
        troca_id = str_id[:8]
        numero_id = re.sub(r'\D', '', troca_id)
        id = 41 + numero_id
        
        return id
        
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, novaDescricao):
        self.__descricao = novaDescricao

    @property
    def dataInicio(self):
        return self.__dataInicio
    
    @property
    def dataFim(self):
        return self.__dataFim
    
    @property
    def descricao(self):
        return self.__descricao