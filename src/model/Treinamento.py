import sqlite3
from utils.env import Env
from utils.util import Util
from utils.env import Env

class Treinamento:
    def __init__(self, titulo, descricao, participantes, data_inicio, data_fim, duracao):
        self.__treinamentoId = Util.gerador_id(7, 41)
<<<<<<< HEAD
        self.__titulo = None
        self.__descricao = None
        self.__dataInicio = None
        self.__dataFim = None
        self.__duracao = None
        self.__participante = {}
        self.__status = Util.status(self.dataInicio, self.dataFim)
        self.__participantes = [] # Lista de IDS de funcionários participantes

    def adicionar_participante(self, funcionario_id):
        """Adiciona um funcionário ao treinamento e salva no banco de dados."""
        if funcionario_id not in self.__participantes:
=======
        self.__titulo = self.veriricarTitulo(titulo)
        self.descricao = descricao
        self.participantes = participantes
        self.duracao = duracao
        self.__dataInicio = self.verificarData(data_inicio)
        self.__dataFim = self.verificarData(data_fim)
        self.participante = {}
        self.__status = Util.status('pendente')
    
    def verificarData(self, data):
        if not Util.validar_data(data):
            raise ValueError("Data inválida.")
        return data

    def veriricarTitulo(self, titulo):
        if len(titulo) < 5:
            raise ValueError("O título deve ter no mínimo 5 caracteres.")
        return titulo

    def adicionar_participante(self, funcionario_id):
        """Adiciona um funcionário ao treinamento e salva no banco de dados."""
        
        if funcionario_id not in self.participantes:
>>>>>>> f918f67d18b6eeb713fa5836cbe5b14d5d3e4e0b
            self.participantes.append(funcionario_id)
            conn =sqlite3.connect(Env.DATABASE_TREINAMENTOS)
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS treinamentos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    treinamento_id TEXT NOT NULL,
                    funcionario_id TEXT NOT NULL,
                    titulo TEXT NOT NULL,
                    cargo TEXT NOT NULL,
                    duracao TEXT NOT NULL,
                )
            """)
    
        try:
            cursor.execute('''
                INSERT INTO treinamentos (treinamento_id, funcionario_id, titulo, cargo, duracao)
                VALUES (?, ?, ?, ?, ?)
            ''', (self.treinamentoId, self.funcionarioId, self.titulo, self.cargo, self.duracao))
            conn.commit()
            conn.close()
            print("Treinamento adicionado com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")

        



    
    @property
    def treinamentoId(self):
        return self.__treinamentoId
    
    @treinamentoId.setter
    def treinamentoId(self, novoId):
        self.__treinamentoId = novoId

    @property
    def status(self):
        return self.__status
              
    @property
    def duracao(self):
        return self.__duracao
    
    @duracao.setter
    def duracao(self, novaDuracao):
        self.__duracao = novaDuracao

    @property
    def participante(self):
        return self.__participante
    
    @participante.setter
    def participante(self, novoParticipante):
        self.__participante = novoParticipante

        
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def cargo(self):
        return self.__cargo
    
    @cargo.setter
    def cargo(self, novaDescricao):
        self.__cargo = novaDescricao

    @property
    def dataInicio(self):
        return self.__dataInicio
    
    @property
    def dataFim(self):
        return self.__dataFim
    
    @property
    def cargo(self):
        return self.__cargo
    
    def remover_participante(self, funcionario_id):
        """Remove um funcionário do treinamento e do banco de dados."""
        if funcionario_id in self.participantes:
            self.participantes.remove(funcionario_id)
            del self.progresso[funcionario_id]
            with sqlite3.connect(Env.DATABASE_TREINAMENTOS) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM participantes WHERE treinamento_id=? AND funcionario_id=?",
                        (self.treinamentoId, funcionario_id))
            conn.commit()
            conn.close()
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
    


        




    def get_treinamento_by_id(cls, treinamento_id):
        """Recupera um treinamento do banco de dados pelo ID."""
        with sqlite3.connect(Env.DATABASE_TREINAMENTOS) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM treinamentos WHERE id=?", (treinamento_id,))
            row = cursor.fetchone()

        if row:
            return cls(
                titulo=row[1],
                descricao=row[2],
                data_inicio=row[3],
                data_fim=row[4],
                status=row[5]
            )
        else:
            raise ValueError(f"Treinamento com ID {treinamento_id} não encontrado.")
        

