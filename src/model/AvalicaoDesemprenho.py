from utils.util import Util

class AvaliacaoDesempenho:
    def __init__(self, funcionarioId, dataAvalicao, feedback):
        self.__avaliacaoId= Util.gerador_id()
        self.__funcionarioId= funcionarioId
        self.__dataAvaliacao= dataAvalicao
        self.__feedback= feedback
        
    
    @property
    def avaliacaoId(self):
        return self.__avaliacaoId
    @avaliacaoId.setter
    def avaliacaoId(self, novoId):
        self.__avaliacaoId = novoId
    
    @property
    def funcionarioid(self):
        return self.__funcionarioId
    @funcionarioid.setter
    def funcionarioId(self, novoId):
        self.__funcionarioId = novoId
        
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


    
    # @classmethod
    # def get_avaliacao_by_id(cls, avaliacao_id):
    #     """Busca uma avaliação de desempenho no banco de dados pelo ID."""
    #     conn = sqlite3.connect('funcionarios.db')
    #     cursor = conn.cursor()

    #     cursor.execute("SELECT * FROM avaliacao WHERE id=?", (avaliacao_id,))
    #     row = cursor.fetchone()

    #     conn.close()

    #     if row:
    #         avaliacao = cls(
    #             funcionario_id=row[1],
    #             data_avaliacao=row[2],
    #             feedback=row[3]
    #         )
    #         avaliacao.id = row[0]  # Atribui o ID recuperado do banco
    #         return avaliacao
    #     else:
    #         raise ValueError(f"Avaliação com ID {avaliacao_id} não encontrada.")

    # def salvar_avaliacao(self):
    #     """Salva a avaliação de desempenho no banco de dados."""
    #     conn = sqlite3.connect('funcionarios.db')
    #     cursor = conn.cursor()

    #     cursor.execute("""
    #         INSERT INTO avaliacao (id, funcionario_id, data_avaliacao, feedback)
    #         VALUES (?, ?, ?, ?)
    #     """, (self.id, self.funcionario_id, self.data_avaliacao, self.feedback))

    #     conn.commit()
    #     conn.close()

    # def atualizar_avaliacao(self):
    #     """Atualiza uma avaliação de desempenho existente no banco de dados."""
    #     conn = sqlite3.connect('funcionarios.db')
    #     cursor = conn.cursor()

    #     cursor.execute("""
    #         UPDATE avaliacao
    #         SET funcionario_id = ?, data_avaliacao = ?, feedback = ?
    #         WHERE id = ?
    #     """, (self.funcionario_id, self.data_avaliacao, self.feedback, self.id))

    #     conn.commit()
    #     conn.close()