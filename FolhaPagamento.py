import re
import uuid

class FolhaPagamento:
    def __init__(self, funcionarioId, dataPagamento, salarioBase, bonus, deducoes, salarioLiquido):
        self.id= self.gerador_id()
        self.funcionarioId= funcionarioId
        self.dataPagamento= dataPagamento
        self.bonus= bonus
        self.deducoes= deducoes
        self.salarioBase= salarioBase
        self.salarioLiquido= salarioLiquido

    def gerador_id(self):
        id_gerado = uuid.uuid4()
        str_id = str(id_gerado).replace('-','') # Retira os hífens
        troca_id = str_id[:6]
        numero_id = re.sub(r'\D', '', troca_id)
        id = 19 + numero_id
        
        return id