import sqlite3
from utils.env import Env
from utils.util import Util
from datetime import datetime 

class RegistroPonto:
    def __init__(self, funcionarioId, data):
        self.__pontoId= Util.gerador_id(6, 839)
        self.__funcionarioId= self.verificar_funcionario(funcionarioId)
        self.data= data
        self.__horaEntrada= self.hora_entrada()
        self.__horaSaida= self.hora_saida()
        self.__horasTrabalhadas= self.calcular_horas_trabalhadas()
 

    def registrar_entrada(self):
        return datetime.now()

    def registrar_saida(self):
        return datetime.now()

    def calcular_horas_trabalhadas(self):
        if self.entrada and self.saida:
            self.horasTrabalhadas = (self.saida - self.entrada).total_seconds() / 3600

    def verificar_funcionario(self):
        if self.funcionarioId > 0:
            return True
        else:
            return False
    
    def adicionarPontoBd(self):
        conn= sqlite3.connect(Env.DATABASE_PONTO)
        cursor= conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pontos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ponto_id TEXT NOT NULL,
                funcionario_id TEXT NOT NULL,
                data TEXT NOT NULL,
                hora_entrada TEXT NOT NULL,
                hora_saida TEXT NOT NULL,
                horas_trabalhadas TEXT NOT NULL
            )
        """)
        try:
            cursor.execute('''
                INSERT INTO pontos (ponto_id, funcionario_id, data, hora_entrada, hora_saida, horas_trabalhadas)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (self.pontoId, self.funcionarioId, self.data, self.horaEntrada, self.horaSaida, self.horasTrabalhadas))
            conn.commit()
            conn.close()
            print("Ponto adicionado com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")

    def verificarHoraEntrada(self):
        if self.horaEntrada:
            return True
        else:
            return False
        
    def verificarHoraSaida(self):
        if self.horaSaida:
            return True
        else:
            return False
        
    @property
    def pontoId(self):
        return self.__pontoId
    
    @pontoId.setter
    def pontoId(self, novoId):
        self.__pontoId = novoId

    @property
    def horasTrabalhadas(self):
        return self.__horasTrabalhadas
    
    @horasTrabalhadas.setter
    def horasTrabalhadas(self, novaHora):
        self.__horasTrabalhadas = novaHora
    @property
    def funcionarioId(self):
        return self.__funcionarioId
    
    @funcionarioId.setter
    def funcionarioId(self, novoId):
        self.__funcionarioId = novoId

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, novaData):
        self.__data = novaData
    
    @property
    def horaEntrada(self):
        return self.__horaEntrada
    @horaEntrada.setter
    def horaEntrada(self, novaHora):
        self.__horaEntrada = novaHora
    
    @property
    def horaSaida(self):
        return self.__horaSaida
    @horaSaida.setter
    def horaSaida(self, novaHora):
        self.__horaSaida = novaHora
        