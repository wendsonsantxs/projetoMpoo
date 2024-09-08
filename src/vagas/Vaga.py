import uuid
import re

class Vaga:
    def __init__(self, titulo, descricao, requisitos, dataPublicacao, dataSelecao):
        self._vagaId = self.gerador_id()
        self.__titulo = titulo
        self.__descricao = descricao
        self.__requisitos = requisitos
        self.__dataPublicacao = dataPublicacao
        self.__dataSelecao = dataSelecao
        self.__status= self.status()

    def gerador_id(self):
        id_gerado = uuid.uuid4()
        str_id = str(id_gerado).replace('-','') # Retira os hífens
        troca_id = str_id[:6]
        numero_id = re.sub(r'\D', '', troca_id)
        id = 12 + numero_id
        
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
    def dataPublicacao(self):
        return self.__dataPublicacao
    
    @property
    def requisitos(self):
        return self.__requisitos
    
    @requisitos.setter
    def requisitos(self, novosRequisitos):
        self.__requisitos = novosRequisitos