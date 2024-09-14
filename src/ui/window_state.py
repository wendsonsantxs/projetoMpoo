from ui.window import Window


class WindowState:
    ID_MAIN = '1'
    ID_RELACAO_F = '2'
    ID_RELACAO_V = '3'
    ID_RELACAO_T = '4'
    ID_CADASTRO_F = '5'
    ID_AVALIACAO = '6'
    ID_FOLHA_PAGAMENTO = '7'
    ID_FOLHA_PONTO = '8'
    ID_CADASTRO_T = '9'
    ID_TREINAMENTO_ATIVO = '10'
    ID_TREINAMENTO_HISTORICO = '11'
    ID_CADASTRO_V = '12'
    ID_BANCO_TALENTO = '13'
    ID_VAGA_ATIVA = '14'

    state: dict[str, Window] = {}

    @staticmethod
    def set_window(window_id: str, target_window: Window):
        window = WindowState.state.get(window_id)
        if window == None:
            WindowState.state.update({window_id: target_window})

    @staticmethod
    def get_window(window_id: str) -> Window | None:
        return WindowState.state.get(window_id)
