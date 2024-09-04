import window01, window02, window03, window04, window05, window06, window07, window08, window09, window10, window11, window12, window13, window14

class Janelas:
    def __init__(self):
        self.Tela = window01.Tela
        self.RelacaoF = window02.RelacaoF
        self.RelacaoV = window03.RelacaoV
        self.RelacaoT = window04.RelacaoT
        self.CadastroF = window05.CadastroF
        self.CadastroV = window06.CadastroV
        self.CadastroT = window07.CadastroT
        self.FolhaPagamento = window08.FolhaPagamento
        self.FolhaPonto = window09.FolhaPonto
        self.Avaliacoes = window10.Avaliacoes
        self.VagasA = window11.VagasA
        self.BancoT = window12.BancoT
        self.TreinamentoAt = window13.TreinamentoAt
        self.HistoricoT = window14.HistoricoT

        self.janelas = [self.Tela, self.RelacaoF, self.RelacaoV, self.RelacaoT, self.CadastroF, self.CadastroV, self.CadastroT, self.FolhaPagamento, self.FolhaPonto, self.Avaliacoes, self.VagasA, self.BancoT, self.TreinamentoAt, self.HistoricoT]

        self.current_index = 0
        self.janelas[0].deiconify() # Mostra a primeira janela

    def proxima_janela(self):
        self.janelas[self.current_index].withdraw() # Oculta a janela atual
        self.current_index = (self.current_index + 1) % len(self.janelas)