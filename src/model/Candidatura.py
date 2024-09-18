from utils.util import Util
from utils.env import Env

import sqlite3

class Candidatura:
    def __init__(self):
        self._candidatoId = Util.gerador_id(6, 24)
        self.__vagaId = None
        self.__nome = None
        self.__cpf = None
        self.__telefone = None
        self.__qualidades = None
        self.__observacoes = None

    def get_dados(self, nome, cpf, telefone, vaga, qualidades, observacoes):
        self.nome = nome
        self.vagaId = vaga
        self.cpf = cpf
        self.telefone = telefone
        self.qualidades = qualidades
        self.observacoes = observacoes
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = Util.verify_cpf(cpf)

    @property
    def vagaId(self):
        return self.__vagaId
    
    @vagaId.setter
    def vagaId(self, vagaId):
        verify = Util.verify_existence(Env.DATABASE_VAGAS, 'Vagas', 'Vaga_id', vagaId)
        if verify == False:
            raise ValueError('Vaga não existe')
        else:
            self.__vagaId = vagaId

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = Util.verify_telefone(telefone)

    @property
    def qualidades(self):
        return self.__qualidades
    
    @qualidades.setter
    def qualidades(self, qualidades):
        self.__qualidades = qualidades

    @property
    def observacoes(self):
        return self.__observacoes
    
    @observacoes.setter
    def observacoes(self, observacoes):
        self.__observacoes = observacoes


    def adicionar_candidato(self):
        conn = sqlite3.connect(Env.DATABASE_TALENTOS)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Candidatos( 
                Candidato_Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Nome TEXT NOT NULL,
                CPF TEXT NOT NULL,
                Telefone TEXT NOT NULL,
                Qualidades TEXT NOT NULL,
                Observações TEXT NOT NULL,
                Vaga_id TEXT NOT NULL
            )
        ''')

        try:
            cursor.execute('''
                INSERT INTO Candidatos (Candidato_Id, Nome, CPF, Telefone, Qualidades, Observações, Vaga_id)
                VALUES (?,?,?,?,?,?,?)
            ''',(self._candidatoId, self.__nome, self.__cpf, self.__telefone, self.__qualidades, self.__observacoes, self.__vagaId))
            
            conn.commit()
            conn.close()

            print("Candidato adicionado com sucesso!")

        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")
        

    def remover_candidato(self):
        pass

    # def get_entrevistas_agendadas(self):
    #     """Recupera entrevistas agendadas do banco de dados e atualiza a lista local."""
    #     conn = sqlite3.connect('funcionarios.db')
    #     cursor = conn.cursor()

    #     cursor.execute("SELECT * FROM entrevistas WHERE candidatura_id=?", (self.id,))
    #     rows = cursor.fetchall()

    #     conn.close()

    #     entrevistas = []
    #     for row in rows:
    #         entrevista = {
    #             'data': row[2],  # Supondo que a coluna 2 seja a data
    #             'horario': row[3],  # Supondo que a coluna 3 seja o horário
    #             'entrevistador': row[4]  # Supondo que a coluna 4 seja o entrevistador
    #         }
    #         entrevistas.append(entrevista)

    #     self.entrevistas = entrevistas  # Atualiza a lista local de entrevistas
    #     return entrevistas
