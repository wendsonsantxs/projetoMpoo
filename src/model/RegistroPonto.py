from utils.util import Util
from utils.env import Env
from datetime import datetime

import sqlite3

class RegistroPonto:
    def __init__(self):
        self.pontoId = Util.gerador_id(6, 839)
        self.__funcionarioId = None
        self.__data= None
        self.__horaEntrada= None
        self.__saidaDescanso = None
        self.__retornoDescanso = None
        self.__horaSaida= None
        self.__horasTrabalhadas= self.calcular_horas_trabalhadas()
 
    def get_dados(self, funcionarioId, data, horaEntrada, horaSaida, saidaDescanso, retornoDescanso):
        self.funcionarioId = funcionarioId
        self.data = data
        self.horaEntrada = horaEntrada
        self.horaSaida = horaSaida
        self.saidaDescanso = saidaDescanso
        self.retornoDescanso = retornoDescanso

        
    @property
    def funcionarioId(self):
        return self.__funcionarioId
    
    @funcionarioId.setter
    def funcionarioId(self, novoId):
        verify = Util.verify_existence(Env.DATABASE_FUNCIONARIO, 'funcionario', 'funcionarioId', novoId)
        if verify:
            raise ValueError('Funcionário não existe')
        else:
            self.__funcionarioId = novoId

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, novaData):
        self.__data = Util.verify_data(novaData)
    
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

    @property
    def saidaDescanso(self):
        return self.__saidaDescanso
    
    @saidaDescanso.setter
    def saidaDescanso(self, novaHora):
        self.__saidaDescanso = novaHora

    @property
    def retornoDescanso(self):
        return self.__retornoDescanso
    
    @retornoDescanso.setter
    def retornoDescanso(self, novaHora):
        self.__retornoDescanso = novaHora

    def registrar_entrada(self):
        self.entrada = datetime.now()

    def registrar_saida(self):
        self.saida = datetime.now()

    def calcular_horas_trabalhadas(self):
        if self.entrada or self.saidaDescanso:
            horas_entrada = (self.saidaDescanso - self.entrada)
        if self.retornoDescanso or self.saida:
            horas_saida = (self.saida - self.retornoDescanso)
            
        #horas_saida = (self.saida - self.entrada).total_seconds() / 3600

    def inserir(self):
        
        conn = sqlite3.connect(Env.DATABASE_PONTO)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Folha_Ponto (
                Ponto-id INTEGER PRIMARY KEY AUTOINCREMENT,
                Funcionario-id INTEGER NOT NULL,
                Data iNTEGER NOT NULL,
                hora_entrada iNTEGER NOT NULL,
                Saida_descanso iNTEGER NOT NULL,
                Retorno_descanso iNTEGER NOT NULL,
                Hora_saida iNTEGER NOT NULL,
                Horas_trabalhadas iNTEGER NOT NULL
            )
        """)
       
        try:
            cursor.execute('''
                INSERT INTO Folha_Ponto (Ponto-id, Funcionario-id, Data, Hora_entrada, Saida_descanso, Retorno_descanso, Hora_saida, Horas_trabalhadas)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (self.pontoId, self.__funcionarioId, self.__data,  self.__horaEntrada, self.__saidaDescanso, self.__retornoDescanso, self.__horaSaida, self.__horasTrabalhadas))
            conn.commit()
            conn.close()
            print("Ponto Registrado com sucesso!")

        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")