import os
from pathlib import Path

class Env:
    ROOT = Path(__file__).parent.parent.parent
    DATABASE_FUNCIONARIO = os.path.join(ROOT, 'database', 'funcionarios.db') 
    DATABASE_TALENTOS = os.path.join(ROOT, 'database', 'banco_de_talentos.db')
    DATABASE_AVALIACOES = os.path.join(ROOT, 'database', 'avaliacoes_funcionario.db')
    DATABASE_VAGAS = os.path.join(ROOT, 'database', 'vagas.db')
    DATABASE_PAGAMENTO = os.path.join(ROOT, 'database', 'pagamento.db')
    DATABASE_TREINAMENTOS = os.path.join(ROOT, 'database', 'treinamentos.db')
    DATABASE_PONTO = os.path.join(ROOT, 'database', 'registro_ponto.db')