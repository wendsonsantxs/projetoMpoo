from utils.util import Util
from utils.env import Env
from model.Vaga import Vaga
from model.funcionario import *
import sqlite3

class Candidatura:
    def __init__(self, vagaId, candidatoNome):
        self.__candidatoId= Util.gerador_id(6, 74)
        self.__vagaId= self.verificarVagaId(vagaId)
        self.candidatoNome= candidatoNome
        self.status= Util.status()
     
    def associar_vaga(self, vaga):
        """Associa a candidatura a uma vaga e registra a candidatura."""
        self.__vagaId = vaga.vagaId
        vaga.adicionar_candidatura(self.__candidatoId)

    def verificarVagaId(self, vagaId):
        if vagaId > 0:
            return vagaId
        else:
            raise ValueError("Vaga inválida.")
        
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
    
    def adicionar_candidato(self):
        conn = sqlite3.connect(Env.DATABASE_TALENTOS)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO candidaturas (id, vaga_id, nome, status)
        VALUES (?, ?, ?, ?)
        """, (self.candidatoId, self.vagaId, self.candidatoNome, self.status))

        conn.commit()
        conn.close()

        

    def remover_candidato(self):
        conn = sqlite3.connect(Env.DATABASE_TALENTOS)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM candidaturas WHERE id=?", (self.candidatoId,))
        conn.commit()
        conn.close()


    def get_entrevistas_agendadas(self):
        """Recupera entrevistas agendadas do banco de dados e atualiza a lista local."""
        conn = sqlite3.connect('funcionarios.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM entrevistas WHERE candidatura_id=?", (self.id,))
        rows = cursor.fetchall()

        conn.close()

        entrevistas = []
        for row in rows:
            entrevista = {
                'data': row[2],  # Supondo que a coluna 2 seja a data
                'horario': row[3],  # Supondo que a coluna 3 seja o horário
                'entrevistador': row[4]  # Supondo que a coluna 4 seja o entrevistador
            }
            entrevistas.append(entrevista)

        self.entrevistas = entrevistas  # Atualiza a lista local de entrevistas
        return entrevistas