import sqlite3
from utils.util import Util

class AvaliacaoDesempenho:
    def __init__(self, funcionarioId, dataAvalicao, feedback):
        self.__avaliacaoId= Util.gerador_id(7, 24)
        self.__funcionarioId= self.validarFuncionario(funcionarioId)
        self.__dataAvaliacao= dataAvalicao
        self.feedback= feedback
        
    
    def validarFuncionario(self, funcionarioId):
        if funcionarioId > 0:
            return funcionarioId
        else:
            raise ValueError("Funcionário inválido")

    @property
    def funcionarioId(self):
        return self.__funcionarioId

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
    def feedback(self, novoFeedback):
        self.__feedback = novoFeedback

    def adicionar_avaliacao(funcionarioId, dataAvaliacao, feedback):
        conn = sqlite3.connect('avaliacoes_funcionario.db')
        cursor = conn.cursor()
        
        # Verifica se o funcionário existe
        cursor.execute("SELECT * FROM funcionario WHERE id=?", (funcionarioId,))
        funcionario = cursor.fetchone()
        
        if funcionario is None:
            conn.close()
            raise ValueError(f"Funcionário com ID {funcionarioId} não encontrado.")
        
        # Cria uma nova avaliação de desempenho
        nova_avaliacao = AvaliacaoDesempenho(funcionarioId, dataAvaliacao, feedback)
        
        # Insere a avaliação no banco de dados
        cursor.execute("""
            INSERT INTO avaliacao (id, funcionario_id, data_avaliacao, feedback)
            VALUES (?, ?, ?, ?)
        """, (nova_avaliacao.avaliacaoId, nova_avaliacao.funcionarioId, nova_avaliacao.dataAvaliacao, nova_avaliacao.feedback))
        
        conn.commit()
        conn.close()

        print(f"Avaliação adicionada para o funcionário {funcionarioId} com sucesso.")

    
    @classmethod
    def get_avaliacao_by_id(cls, avaliacao_id):
        """Busca uma avaliação de desempenho no banco de dados pelo ID."""
        conn = sqlite3.connect('avaliacoes_funcionario.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM avaliacao WHERE id=?", (avaliacao_id,))
        row = cursor.fetchone()

        conn.close()

        if row:
            avaliacao = cls(
                funcionario_id=row[1],
                data_avaliacao=row[2],
                feedback=row[3]
            )
            avaliacao.id = row[0]  # Atribui o ID recuperado do banco
            return avaliacao
        else:
            raise ValueError(f"Avaliação com ID {avaliacao_id} não encontrada.")

    def salvar_avaliacao(self):
        """Salva a avaliação de desempenho no banco de dados."""
        conn = sqlite3.connect('avaliacoes_funcionario.db')
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO avaliacao (id, funcionario_id, data_avaliacao, feedback)
            VALUES (?, ?, ?, ?)
        """, (self.id, self.funcionario_id, self.data_avaliacao, self.feedback))

        conn.commit()
        conn.close()

    def atualizar_avaliacao(self):
        """Atualiza uma avaliação de desempenho existente no banco de dados."""
        conn = sqlite3.connect('avaliacoes_funcionario.db')
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE avaliacao
            SET funcionario_id = ?, data_avaliacao = ?, feedback = ?
            WHERE id = ?
        """, (self.funcionario_id, self.data_avaliacao, self.feedback, self.id))

        conn.commit()
        conn.close()
