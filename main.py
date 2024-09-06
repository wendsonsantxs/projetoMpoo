from avaliacoes import *
from candidatos import *
from folhas_ponto import *
from funcionarios import *
from pagamentos import *
from treinamentos import *
from vagas import *
import build.window01, build.window02, build.window03, build.window04, build.window05, build.window06, build.window07, build.window08, build.window09, build.window10, build.window11, build.window12, build.window13, build.window14


class Janelas:
    def __init__(self):
        self.Tela = build.window01.Tela()
        self.RelacaoF = build.window02.RelacaoF()
        self.RelacaoV = build.window03.RelacaoV()
        self.RelacaoT = build.window04.RelacaoT()
        self.CadastroF = build.window05.CadastroF()
        self.CadastroV = build.window06.CadastroV()
        self.CadastroT = build.window07.CadastroT()
        self.FolhaPagamento = build.window08.FolhaPagamento()
        self.FolhaPonto = build.window09.FolhaPonto()
        self.Avaliacoes = build.window10.Avaliacoes()
        self.VagasA = build.window11.VagasA()
        self.BancoT = build.window12.BancoT()
        self.TreinamentoAt = build.window13.TreinamentoAt()
        self.HistoricoT = build.window14.HistoricoT()

        self.janelas = [self.Tela, self.RelacaoF, self.RelacaoV, self.RelacaoT, self.CadastroF, self.CadastroV, self.CadastroT, self.FolhaPagamento, self.FolhaPonto, self.Avaliacoes, self.VagasA, self.BancoT, self.TreinamentoAt, self.HistoricoT]

        self.current_index = 0
        self.janelas[0].deiconify() #Mostra a primeira janela

    def proxima_janela(self, x):
        self.janelas[self.current_index].withdraw() #Oculta a janela atual
        self.current_index = (self.current_index + x) % len(self.janelas) #Calcula o índice da próxima janela
        self.janelas[self.current_index].deiconify() #Mostra a próxima janela


if __name__ == "__main__":
    janelas = Janelas()
    janelas.Tela.mainloop()