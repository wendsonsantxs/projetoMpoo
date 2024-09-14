from datetime import datetime
import re
import uuid

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