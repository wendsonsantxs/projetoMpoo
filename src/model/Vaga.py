from utils.util import Util
from utils.env import Env
from model.Candidatura import Candidatura

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
        self.__candidaturas = []  # Lista para armazenar as candidaturas associadas à vaga


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
                INSERT INTO vagas (id, titulo, descricao, requisitos, data_publicacao, data_selecao, status)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (self.__vagaId, self.__titulo, self.__descricao, self.__requisitos, self.__dataPublicacao, self.__dataSelecao, self.__status))
            conn.commit()
            print("Vaga adicionada com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")
        finally:
            conn.close()

    @classmethod
    def get_vaga_by_id(cls, vaga_id):
        """Recupera uma vaga do banco de dados pelo ID."""
        with sqlite3.connect(Env.DATABASE_VAGAS) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vagas WHERE id=?", (vaga_id,))
            row = cursor.fetchone()

        if row:
            return cls(
                titulo=row[1],
                descricao=row[2],
                requisitos=row[3],
                dataPublicacao=row[4],
                dataSelecao=row[5]
            )
        else:
            raise ValueError(f"Vaga com ID {vaga_id} não encontrada.")

    def gerar_relatorio(self):
        """Gera um relatório com estatísticas sobre a vaga."""
        total_candidaturas = len(self.__candidaturas)
        candidaturas_aprovadas = sum(1 for c in self.__candidaturas if c.status == 'Aprovado')
        candidaturas_rejeitadas = sum(1 for c in self.__candidaturas if c.status == 'Rejeitado')
        return {
            'total_candidaturas': total_candidaturas,
            'aprovadas': candidaturas_aprovadas,
            'rejeitadas': candidaturas_rejeitadas
        }
    
    def adicionar_candidatura(self, candidatura):
        """Adiciona uma candidatura a esta vaga."""
        if isinstance(candidatura, Candidatura):
            self.__candidaturas.append(candidatura)
        else:
            raise ValueError("O parâmetro deve ser uma instância de Candidatura")

    def listar_candidaturas(self):
        """Retorna a lista de candidaturas associadas à vaga."""
        return self.__candidaturas
    
    
    def get_entrevistas_agendadas(self):
        """Recupera entrevistas agendadas para esta candidatura."""
        conn = sqlite3.connect(Env.DATABASE_TALENTOS)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM entrevistas WHERE candidatura_id=?", (self.candidatoId,))
        rows = cursor.fetchall()

        conn.close()

        entrevistas = []
        for row in rows:
            entrevista = {
                'data': row[2],  # Supondo que a coluna 2 seja a data da entrevista
                'horario': row[3],  # Supondo que a coluna 3 seja o horário
                'entrevistador': row[4]  # Supondo que a coluna 4 seja o nome do entrevistador
            }
            entrevistas.append(entrevista)

        self.entrevistas = entrevistas  # Atualiza a lista local de entrevistas
        return entrevistas
    
