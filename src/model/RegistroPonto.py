from utils.util import Util
from utils.env import Env
from datetime import datetime

import sqlite3

class RegistroPonto:
    def __init__(self, funcionarioId, data, horaEntrada, horaSaida, horasTrabalhadas):
        self.pontoId= Util.gerador_id(6, 839)
        self.__funcionarioId= funcionarioId
        self.__data= data
        self.__horaEntrada= horaEntrada
        self.__horaSaida= horaSaida
        self.__horasTrabalhadas= horasTrabalhadas
 

    def registrar_entrada(self):
        self.entrada = datetime.now()

    def registrar_saida(self):
        self.saida = datetime.now()

    def calcular_horas_trabalhadas(self):
        if self.entrada and self.saida:
            self.horasTrabalhadas = (self.saida - self.entrada).total_seconds() / 3600

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


    def inserir(self):
        
        conn = sqlite3.connect(Env.DATABASE_PONTO)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS treinamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                funcionario TEXT NOT NULL,
                data TEXT NOT NULL,
                hora_entrada TEXT NOT NULL,
                hora_saida TEXT NOT NULL,
                horas_diaria TEXT NOT NULL
            )
        """)
       
        try:
            cursor.execute('''
                INSERT INTO treinamentos (id, funcionario, data, hora_entrada, hora_saida, horas_diaria)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (self.pontoId, self.__funcionarioId, self.__data, self.__horaEntrada, self.__horaSaida, self.__horasTrabalhadas))
            conn.commit()
            print("Ponto Registrado com sucesso!")

        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")