from ui.window import Window


class WindowState:
    ID_MAIN = '1' # Main Window

    ID_RELACAO_F = '2' # Relacao de Funcionarios
    ID_RELACAO_V = '3' # Relacao de Vagas
    ID_RELACAO_T = '4' # Relacao de Treinamentos

    ID_CADASTRO_F = '5' # Cadastro de Funcionarios
    ID_REMOCAO_F = '6' # Remoção de Funcionarios
    ID_PESQUISA_F = '7' # Relação de Pesquisa
    ID_FUNCIONARIO_PESQUISAR = '8' # Pesquisar Funcionarios
    ID_BANCO_F = '9' # Banco de Funcionarios
    ID_FOLHA_PAGAMENTO = '10' # Folha de Pagamento
    ID_FOLHA_PONTO = '11' # Folha de Ponto

    ID_CADASTRO_T = '12' # Cadastro de Treinamentos
    ID_PESQUISAR_T = '13' # Relação para Pesquisar Treinamentos
    ID_REMOVER_T = '14' # Remover Treinamentos
    ID_PESQUISAR_TREINAMENTO = '15' # Pesquisar Treinamentos
    ID_TREINAMENTO_ATIVO = '16' # Treinamentos Ativos
    ID_TREINAMENTO_HISTORICO = '17' # Historico de Treinamento

    ID_CADASTRO_V = '18' # Cadastro de Vagas
    ID_REMOVER_V = '19' # Remover Vagas
    ID_PESQUISAR_V = '20' # Relação para Pesquisar Vagas
    ID_VAGA_PESQUISAR = '21' # Pesquisar Vaga
    ID_VAGA_ATIVA = '22' # Vagas Ativas
    ID_BANCO_V = '23' # Banco de Vagas
    
    ID_RELACAO_C = '24' # Relacao de Candidatos
    ID_CADASTRO_C = '25' # Cadastro de Candidatos
    ID_BANCO_TALENTO = '26' # Banco de Talentos
    

    state: dict[str, Window] = {}

    @staticmethod
    def set_window(window_id: str, target_window: Window):
        window = WindowState.state.get(window_id)
        if window == None:
            WindowState.state.update({window_id: target_window})

    @staticmethod
    def get_window(window_id: str) -> Window | None:
        return WindowState.state.get(window_id)
