from utils.util import Util
from utils.env import Env

import sqlite3

class Candidatura:
    def __init__(self, vagaId, candidatoNome, status):
        self.candidatoId= Util.gerador_id(6, 74)
        self.__vagaId= vagaId
        self.__candidatoNome= candidatoNome
        #self.__status= Util.status()
     
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
        

    def remover_candidato(self):
        pass

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

    """Classe que armazena o histórico de uma candidatura, incluindo status e entrevistas realizadas."""

    def __init__(self, candidatura_id):
        super().__init__()
        self.id = self.gerador_id(85)
        self.candidatura_id = candidatura_id
        self.eventos = []

    def adicionar_evento(self, descricao, data=None):
        """Adiciona um evento ao histórico da candidatura (Ex: Entrevista realizada, Feedback dado)."""
        # if data is None:
        #     data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        evento = {
            'descricao': descricao,
            'data': data
        }
        self.eventos.append(evento)

        # Inserir no banco de dados
        conn = sqlite3.connect('funcionarios.db')
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO eventos (historico_id, descricao, data)
            VALUES (?, ?, ?)
        """, (self.id, descricao, data))

        conn.commit()
        conn.close()

    def get_eventos(self):
        """Recupera os eventos do banco de dados e atualiza a lista de eventos."""
        conn = sqlite3.connect('funcionarios.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM eventos WHERE historico_id=?", (self.id,))
        rows = cursor.fetchall()

        conn.close()

        eventos = []
        for row in rows:
            evento = {
                'descricao': row[2],  # Supondo que a coluna 2 seja a descrição
                'data': row[3]  # Supondo que a coluna 3 seja a data
            }
            eventos.append(evento)

        self.eventos = eventos  # Atualiza a lista local de eventos com os dados do banco
        return eventos
