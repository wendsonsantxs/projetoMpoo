from datetime import datetime
import re
import uuid
import sqlite3

class Util:
    @staticmethod
    def gerador_id(x, y):
        while True:
            id_gerado = uuid.uuid4()
            str_id = str(id_gerado).replace('-', '')
            numero_id = re.sub(r'\D', '', str_id)
            troca_id = numero_id[:x]

            if len(troca_id) >= x:
                id = str(y) + str(troca_id)
            return id

    @staticmethod
    def status(x, y):

        date_str = datetime.now().strftime("%d/%m")
        date_obj = datetime.strptime(date_str, "%d/%m")
        date_x = datetime.strptime(x, "%d/%m")
        date_y = datetime.strptime(y, "%d/%m")

        if date_x > date_obj:
            return 'Não começado'
        elif date_x == date_obj or date_obj <= date_y:
            return 'Em andamento'
        else:
            return 'Encerrado'

    @staticmethod   
    def verify_cpf(cpf):
        if not re.match(r'^\d{3}\.\d{3}\d{3}\-\{2}$', cpf):
            temp_cpf = re.sub(r'\D', '', cpf)
            try:

                if len(temp_cpf) != 11: # Verifica se o CPF tem 11 dígitos
                    raise ValueError('CPF deve ter 11 dígitos')
                
                if temp_cpf == temp_cpf[0] * 11: # Verifica se os dígitos são iguais
                    raise ValueError('CPF inválido')
                
                soma = sum(int(temp_cpf[i]) * (10 - i) for i in range(9))
                primeiro_digito = (soma * 10 % 11) % 10
            
                soma = sum(int(temp_cpf[i]) * (11 - i) for i in range(10))
                segundo_digito = (soma * 10 % 11) % 10

                if not temp_cpf[-2:] == f"{primeiro_digito}{segundo_digito}":
                    raise ValueError('CPF inválido')
                else:
                    return cpf
            except ValueError as e:
                print(e)
                return None
        else:
            raise ValueError('CPF inválido, 000.000.000-00')
    
    @staticmethod
    def verify_telefone(telefone):
        temp = re.sub(r'\D', '', telefone)

        if len(temp) == 11:
            if temp == temp[0]* 11:
                raise ValueError('O número de telefone não pode ser de um número só')
            else:
                return telefone
        else:
            raise ValueError('O número de telefone deve conter 11 dígitos')
    
    @staticmethod
    def verify_data(data):
        try:
            datetime.strptime(data, '%d/%m/%Y')
            return data
        except ValueError:
            raise ValueError('Data inválida')
        
    @staticmethod
    def verify_existence(database, databaseName, column, value):

        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        cursor.execute("SELECT 1 FROM "+databaseName+" WHERE "+column+" = ?", (value,))
        resultado = cursor.fetchone()

        conn.close()

        return resultado is not None