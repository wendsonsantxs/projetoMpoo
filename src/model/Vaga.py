from utils.util import Util
from utils.env import Env

import sqlite3

class Vaga:
    def __init__(self, titulo, descricao, requisitos, dataPublicacao, dataSelecao):
        self.__vagaId = self.gerarVagaId()
        self.titulo = titulo
        self.descricao = descricao
        self.requisitos = requisitos
        self.dataPublicacao = dataPublicacao
        self.dataSelecao = dataSelecao
        self.__status= Util.status(dataPublicacao, dataSelecao)




    def gerarVagaId(self):
        return Util.gerador_id(6, 74)
    
    @property
    def vagaId(self):
        return self.__vagaId
    @vagaId.setter
    def vagaId(self, novoId):
        self.__vagaId = novoId

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

    @property
    def dataSelecao(self):
        return self.__dataSelecao
    
    @dataSelecao.setter
    def dataSelecao(self, novaData):
        self.__dataSelecao = novaData

    def adicionar_vaga(self):
        """Adiciona uma nova vaga ao banco de dados."""
        conn = sqlite3.connect(Env.DATABASE_VAGAS)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS vagas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT NOT NULL,
                requisitos TEXT NOT NULL,
                data_publicacao TEXT NOT NULL,
                data_selecao TEXT NOT NULL,
                status TEXT NOT NULL
            )
        """)

        try:
            cursor.execute('''
                INSERT INTO vagas (id, titulo, descricao, requisitos, data_publicacao, status)
                VALUES (?, ?, ?, ?, ?)
            ''', (self.vagaId, self.__titulo, self.__descricao, self.__requisitos, self.__dataPublicacao, self.__dataSelecao, self.__status))
            conn.commit()
            print("Vaga adicionada com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")

    @classmethod
    def get_vaga_by_id(cls, vaga_id):
        """Recupera uma vaga do banco de dados pelo ID."""
        with sqlite3.connect('funcionarios.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vagas WHERE id=?", (vaga_id,))
            row = cursor.fetchone()

        if row:
            return cls(
                titulo=row[1],
                descricao=row[2],
                requisitos=row[3],
                data_publicacao=row[4],
                status=row[5]
            )
        else:
            raise ValueError(f"Vaga com ID {vaga_id} não encontrada.")

    def gerar_relatorio(self):
            """Gera um relatório com estatísticas sobre a vaga."""
            total_candidaturas = len(self.candidaturas)
            candidaturas_aprovadas = sum(1 for c in self.candidaturas if c.status == 'Aprovado')
            candidaturas_rejeitadas = sum(1 for c in self.candidaturas if c.status == 'Rejeitado')
            return {
                'total_candidaturas': total_candidaturas,
                'aprovadas': candidaturas_aprovadas,
                'rejeitadas': candidaturas_rejeitadas
            }