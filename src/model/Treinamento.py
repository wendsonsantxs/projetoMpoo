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
        self.__participante = {}
        self.__status = Util.status(self.dataInicio, self.dataFim)
    
    def remover_participante(self, funcionario_id):
        """Remove um funcionário do treinamento."""
        if funcionario_id in self.participantes:
            self.participantes.remove(funcionario_id)
            del self.progresso[funcionario_id]
        else:
            raise ValueError('Funcionário não encontrado no treinamento.')
        
    def obter_resumo(self):
        """Retorna um resumo do treinamento, incluindo participantes e seus progressos."""
        resumo = {
            'titulo': self.titulo,
            'descricao': self.descricao,
            'data_inicio': self.data_inicio,
            'data_fim': self.data_fim,
            'status': self.status,
            'participantes': {
                participante: self.progresso[participante] for participante in self.participantes
            }
        }
        return resumo
    
    def criar_tabela_treinamento(self):
        """Cria a tabela de treinamentos no banco de dados."""


        conn = sqlite3.connect(Env.DATABASE_TREINAMENTO)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS treinamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT NOT NULL,
                data_inicio TEXT NOT NULL,
                data_fim TEXT NOT NULL,
                status TEXT NOT NULL
            )
        """)
       
        try:
            cursor.execute('''
                INSERT INTO treinamentos (id, titulo, descricao, data_inicio, data_fim, status)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (self.treinamentoId, self.__titulotitulo, self.__descricao, self.__dataInicio, self.__dataFim, self.__status))
            conn.commit()
            print("Treinamento adicionado com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")

    def get_treinamento_by_id(self, treinamento_id):
        """Recupera um treinamento do banco de dados pelo ID."""
        with sqlite3.connect('funcionarios.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM treinamentos WHERE id=?", (treinamento_id,))
            row = cursor.fetchone()

        if row:
            return self(
                titulo = row[1],
                descricao=row[2],
                data_inicio=row[3],
                data_fim=row[4],
                status=row[5]
            )
        else:
            raise ValueError(f"Treinamento com ID {treinamento_id} não encontrado.")