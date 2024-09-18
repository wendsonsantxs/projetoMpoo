from utils.util import Util
from utils.env import Env

import sqlite3
class AvaliacaoDesempenho:
    def __init__(self, funcionarioId, dataAvalicao, feedback):
        self.avaliacaoId= Util.gerador_id()
        self.__funcionarioId= funcionarioId
        self.__dataAvaliacao= dataAvalicao
        self.__feedback= feedback
        
    
    
    @property
    def funcionarioid(self):
        return self.__funcionarioId
    
    @funcionarioid.setter
    def funcionarioId(self, novoId):
        verify = Util.verify_existence(Env.DATABASE_FUNCIONARIO, 'funcionario', 'funcionarioId', novoId)
        if verify:
            raise ValueError('Funcionário não existe')
        else:
            self.__funcionarioId = novoId
        
    @property
    def dataAvaliacao(self):
        return self.__dataAvaliacao
    
    @dataAvaliacao.setter
    def dataAvaliacao(self, novaData):
        self.__dataAvaliacao = Util.verify_data(novaData)
                
    @property
    def feedback(self):
        return self.__feedback
    
    @feedback.setter
    def feeedback(self, novoFeedback):
        self.__feedback = novoFeedback


    def adicinar_avaliacao(self):
        conn = sqlite3.connect(Env.DATABASE_TALENTOS)
        cursor = conn.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS Avaliações(
                       Avaliação-Id INTEGER PRIMARY KEY AUTOINCREMENT,
                       Funcionario-id TEXT NOT NULL,
                       Data_avaliação TEXT NOT NULL,
                       Feedback TEXT NOT NULL)
                       ''')

        try:
            cursor.execute('''
                INSERT INTO funcionarios (Avaliação-Id, funcionario-id, data_avaliação, Feedback)
                VALUES (?,?,?,?)
            ''',(self.avaliacaoId, self.__funcionarioId, self.__dataAvaliacao, self.__feedback))
            
            conn.commit()
            conn.close()

            print("Avaliação adicionado com sucesso!")

        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")
         
 