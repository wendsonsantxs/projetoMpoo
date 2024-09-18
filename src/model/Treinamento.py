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
        self.__status = None

    def get_dados(self, titulo, descricao, dataInicio, dataFim, duracao, participantes):
        self.titulo = titulo
        self.descricao = descricao
        self.dataInicio = dataInicio
        self.dataFim = dataFim
        self.duracao = duracao
        status = Util.status(self.dataInicio, self.dataFim)
        self.status = status
        self.participantes = participantes

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
        for i in participantes:
            
            conn = sqlite3.connect(Env.DATABASE_FUNCIONARIO)
            cursor = conn.cursor()

            cursor.execute("SELECT 1 FROM funcionarios WHERE funcionarioId = ?", i) #verificar se o funcionario existe
            resultado = cursor.fetchone()

            if resultado:
                cursor.execute("SELECT * FROM funcionarios LIMIT 1 OFFSET 1")
                nome = cursor.fetchone()
                self.__participantes[i] = nome
            else:
                print("Funcionário não encontrado")

            

    def inserir_treinamento(self):
       
        conn = sqlite3.connect(Env.DATABASE_TREINAMENTO)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Treinamentos (
                Treinamento_id INTEGER PRIMARY KEY AUTOINCREMENT,
                Titulo TEXT NOT NULL,
                Descrição TEXT NOT NULL,
                Data_inicio TEXT NOT NULL,
                Data_inicio TEXT NOT NULL,
                DuraçãoTEXT NOT NULL,
                Data_fim TEXT NOT NULL,
                Status TEXT NOT NULL
            )
        ''')
       
        try:
            cursor.execute('''
                INSERT INTO Treinamentos (Treinamento_id, Titulo, Descrição, Data_inicio, Duração, Data_fim, Status)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (self.treinamentoId, self.__titulotitulo, self.__descricao, self.__dataInicio, self.__duracao, self.__dataFim, self.__status))
            conn.commit()
            conn.close()

            print("Treinamento adicionado com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")

    def remover_participante(self, funcionario_id):
        
        if funcionario_id in self.participantes:
            self.participantes.remove(funcionario_id)
            with sqlite3.connect(Env.DATABASE_TREINAMENTOS) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM participantes WHERE treinamento_id=? AND funcionario_id=?",
                        (self.treinamentoId, funcionario_id))
            conn.commit()
            conn.close()
        else:
            raise ValueError('Funcionário não encontrado no treinamento.')

    def inserir_participantes(self, funcionario_id):
        """Adiciona um funcionário ao treinamento."""
        if funcionario_id not in self.participantes:
            self.participantes.append(funcionario_id)
            with sqlite3.connect(Env.DATABASE_TREINAMENTOS) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO participantes (treinamento_id, funcionario_id) VALUES (?, ?)",
                        (self.treinamentoId, funcionario_id))
            conn.commit()
            conn.close()
        else:
            raise ValueError('Funcionário já está no treinamento.')