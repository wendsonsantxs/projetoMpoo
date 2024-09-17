from utils.util import Util
from utils.env import Env

import sqlite3

class Treinamento:
    def __init__(self):
        self.treinamentoId = Util.gerador_id(7, 41)
        self.__titulo = None
        self.__descricao = None
        self.__dataInicio = None
        self.__dataFim = None
        self.__duracao = None
        self.__participantes = {}
        self.__status = Util.status(self.dataInicio, self.dataFim)

    def get_dados(self, titulo, descricao, dataInicio, dataFim, duracao):
        self.titulo = titulo
        self.descricao = descricao
        self.dataInicio = dataInicio
        self.dataFim = dataFim
        self.duracao = duracao
        
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def dataInicio(self):
        return self.__dataInicio
    
    @dataInicio.setter
    def dataInicio(self, dataInicio):
        self.__dataInicio = Util.verify_data(dataInicio)

    @property
    def dataFim(self):
        return self.__dataFim
    
    @dataFim.setter
    def dataFim(self, dataFim):
        self.__dataFim = Util.verify_data(dataFim)

    @property
    def duracao(self):
        return self.__duracao
    
    @duracao.setter
    def duracao(self, duracao):
        self.__duracao = duracao

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def participantes(self):
        return self.__participantes
    
    @participantes.setter
    def participantes(self, participantes):
        self.__participantes = participantes

    def inserir_treinamento(self):
       
        conn = sqlite3.connect(Env.DATABASE_TREINAMENTO)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Treinamentos (
                Treinamento-id INTEGER PRIMARY KEY AUTOINCREMENT,
                Titulo TEXT NOT NULL,
                Descrição TEXT NOT NULL,
                Data_inicio TEXT NOT NULL,
                Data_inicio TEXT NOT NULL,
                DuraçãoTEXT NOT NULL,
                Data_fim TEXT NOT NULL,
                Status TEXT NOT NULL
            )
        """)
       
        try:
            cursor.execute('''
                INSERT INTO Treinamentos (Treinamento-id, Titulo, Descrição, Data_inicio, Duração, Data_fim, Status)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (self.treinamentoId, self.__titulotitulo, self.__descricao, self.__dataInicio, self.__duracao, self.__dataFim, self.__status))
            conn.commit()
            conn.close()

            print("Treinamento adicionado com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")

    # def get_treinamento_by_id(self, treinamento_id):
    #     """Recupera um treinamento do banco de dados pelo ID."""
    #     with sqlite3.connect('funcionarios.db') as conn:
    #         cursor = conn.cursor()
    #         cursor.execute("SELECT * FROM treinamentos WHERE id=?", (treinamento_id,))
    #         row = cursor.fetchone()

    #     if row:
    #         return self(
    #             titulo = row[1],
    #             descricao=row[2],
    #             data_inicio=row[3],
    #             data_fim=row[4],
    #             status=row[5]
    #         )
    #     else:
    #         raise ValueError(f"Treinamento com ID {treinamento_id} não encontrado.")