from utils.util import Util
from utils.env import Env

import sqlite3

class Vaga:
    def __init__(self):
        self.vagaId = Util.gerador_id(6, 12)
        self.__titulo = None
        self.__descricao = None
        self.__requisitos = None
        self.__dataPublicacao = None
        self.__dataSelecao = None
        self.__status = None

    def get_dados(self, titulo, descricao, requisitos, dataPublicacao, dataSelecao):
        self.titulo = titulo
        self.descricao = descricao
        self.requisitos = requisitos
        self.dataPublicacao = dataPublicacao
        self.dataSelecao = dataSelecao

        status = Util.status(dataPublicacao, dataSelecao)
        self.status = status 
        

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
    def requisitos(self):
        return self.__requisitos
    
    @requisitos.setter
    def requisitos(self, requisitos):
        self.__requisitos = requisitos

    @property
    def dataPublicacao(self):
        return self.__dataPublicacao
    
    @dataPublicacao.setter
    def dataPublicacao(self, dataPublicacao):
        self.__dataPublicacao = Util.verify_data(dataPublicacao)

    @property
    def dataSelecao(self):
        return self.__dataSelecao
    
    @dataSelecao.setter
    def dataSelecao(self, dataSelecao):
        self.__dataSelecao = Util.verify_data(dataSelecao)

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status):
        self.__status = status
    
    def adicionar_vaga(self):
       
        conn = sqlite3.connect(Env.DATABASE_VAGAS)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Vagas( 
                Vaga_id INTEGER PRIMARY KEY AUTOINCREMENT,
                Titulo TEXT NOT NULL,
                Descrição TEXT NOT NULL,
                Requisitos TEXT NOT NULL,
                Data_publicação TEXT NOT NULL,
                Data_seleção TEXT NOT NULL,
                Status TEXT NOT NULL
            )
        ''')

        try:
            cursor.execute('''
                INSERT INTO Vagas (vaga_id, Titulo, Descrição, Requisitos, Data_publicação, Data_seleção, Status)
                VALUES (?, ?, ?, ?, ?, ? ,?)
            ''', (self.vagaId, self.__titulo, self.__descricao, self.__requisitos, self.__dataPublicacao, self.__dataSelecao, self.__status))
            conn.commit()
            
            print("Vaga adicionada com sucesso!")

        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")

    # @classmethod
    # def get_vaga_by_id(cls, vaga_id):
    #     """Recupera uma vaga do banco de dados pelo ID."""
    #     with sqlite3.connect('funcionarios.db') as conn:
    #         cursor = conn.cursor()
    #         cursor.execute("SELECT * FROM vagas WHERE id=?", (vaga_id,))
    #         row = cursor.fetchone()

    #     if row:
    #         return cls(
    #             titulo=row[1],
    #             descricao=row[2],
    #             requisitos=row[3],
    #             data_publicacao=row[4],
    #             status=row[5]
    #         )
    #     else:
    #         raise ValueError(f"Vaga com ID {vaga_id} não encontrada.")

    