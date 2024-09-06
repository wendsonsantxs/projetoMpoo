import uuid
import re

class Treinamento:
    def __init__(self):
        self.__treinamentoId = self.gerador_id()
        self.__titulo = None
        self.__descricao = None
        self.__dataInicio = None
        self.__dataFim = None
        self.__duracao = None
        self.__participante = {}
        self.__status = self.status()

    def gerador_id(self):
        id_gerado = uuid.uuid4()
        str_id = str(id_gerado).replace('-','') # Retira os hífens
        troca_id = str_id[:8]
        numero_id = re.sub(r'\D', '', troca_id)
        id = 41 + int(numero_id)
        
        return id
    
    def gerenciarTreinamento(self):
        pass


    
    @property
    def treinamentoId(self):
        return self.__treinamentoId
    
    @treinamentoId.setter
    def treinamentoId(self, novoId):
        self.__treinamentoId = novoId

    @property
    def status(self):
        if self.__dataFim > self.__dataInicio:
            return 'Em andamento'
        else:
            return 'Encerrado'
              
    @status.setter
    def status(self, novoStatus):
        self.__status = novoStatus

    @property
    def duracao(self):
        return self.__duracao
    
    @duracao.setter
    def duracao(self, novaDuracao):
        self.__duracao = novaDuracao

    @property
    def participante(self):
        return self.__participante
    
    @participante.setter
    def participante(self, novoParticipante):
        self.__participante = novoParticipante

        
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