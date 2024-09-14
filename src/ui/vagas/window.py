from tkinter import Button
from tkinter import Canvas
from tkinter import PhotoImage
from tkinter import Tk

from ui.window import Window
from ui.window_state import WindowState
from ui.vagas.remover import RemoverV
from ui.vagas.cadastro import CadastroV
from ui.vagas.pesquisar.window import PesquisarWindow
from ui.candidato.Window import CandidatoWindow

class VagasWindow(Window):
    def __init__(self, root: Tk):
        super().__init__(root)
        WindowState.set_window(WindowState.ID_REMOVER_V, RemoverV(root=self.root))
        WindowState.set_window(WindowState.ID_CADASTRO_V, CadastroV(root=self.root))
        WindowState.set_window(WindowState.ID_RELACAO_C, CandidatoWindow(root=self.root))
        WindowState.set_window(WindowState.ID_PESQUISAR_V, PesquisarWindow(root=self.root))

    def create(self):
        super().create()
        self.canvas = Canvas(self.root, bg="#FFFFFF", height=self.height,
                             width=self.width, bd=0, highlightthickness=0, relief="ridge")

        self.canvas.place(x=0, y=0)

        self.bg = PhotoImage(file=self.assets("image_1.png"))
        self.image_1 = self.canvas.create_image(412.0, 412.0, image=self.bg)

        self.rectangle = PhotoImage(file=self.assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            407.0, 461.0, image=self.rectangle)

        self.logo = PhotoImage(file=self.assets("image_3.png"))
        self.image_3 = self.canvas.create_image(195.0, 76.0, image=self.logo)

        self.canvas.create_text(
            284.0,
            46,
            anchor="nw",
            text="Sistema De Gerenciamento De\nRecursos Humanos (Hrms)",
            fill="#FFFFFF",
            font=("Itim Regular", 30 * -1)
        )

        self.button_image_1 = PhotoImage(file=self.assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.relacaoV_button01,
            relief="flat"
        )
        self.button_1.place(x=494.0, y=295.0, width=172.0, height=60.0)

        self.button_image_2 = PhotoImage(file=self.assets("button_1.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.relacaoV_button02,
            relief="flat"
        )
        self.button_2.place(x=494.0, y=413.0, width=172.0, height=60.0)

        self.button_image_3 = PhotoImage(file=self.assets("button_1.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.relacaoV_button03,
            relief="flat"
        )
        self.button_3.place(x=494.0, y=531.0, width=172.0, height=60.0)

        self.button_image_4 = PhotoImage(file=self.assets("button_1.png"))
        self.button_4 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.relacaoV_button04,
            relief="flat"
        )
        self.button_4.place(x=494.0, y=649.0, width=172.0, height=60.0)

        self.canvas.create_text(
            217.0,
            311.0,
            anchor="nw",
            text="Cadastrar Vagas",
            fill="#FFFFFF",
            font=("Itim Regular", 30 * -1)
        )

        self.canvas.create_text(
            220.0,
            427.0,
            anchor="nw",
            text="Remover Vagas",
            fill="#FFFFFF",
            font=("Itim Regular", 30 * -1)
        )

        self.canvas.create_text(
            238.0,
            546.0,
            anchor="nw",
            text="Pesquisar",
            fill="#FFFFFF",
            font=("Itim Regular", 30 * -1)
        )

        self.canvas.create_text(
            175.0,
            662.0,
            anchor="nw",
            text="Relação de Candidatos",
            fill="#FFFFFF",
            font=("Itim Regular", 29 * -1)
        )

        self.canvas.create_text(
            742.0,
            789.0,
            anchor="nw",
            text="W.Y.W",
            fill="#FFFFFF",
            font=("Alef Regular", 18 * -1)
        )

        self.image_image_5 = PhotoImage(file=self.assets("image_4.png"))
        self.image_5 = self.canvas.create_image(
            730.0, 800.0, image=self.image_image_5)

        self.canvas.create_text(
            725.0,
            792.0,
            anchor="nw",
            text="C",
            fill="#FFFFFF",
            font=("Alata Regular", 14 * -1)
        )

        self.button_image_4 = PhotoImage(file=self.assets("button_2.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_back,
            relief="flat"
        )
        self.button_4.place(x=169.0, y=201.0, width=64.0, height=55.0)

    def relacaoV_button01(self):
        self.switch_window(swap_to=WindowState.get_window(WindowState.ID_CADASTRO_V))

    def relacaoV_button02(self):
        self.switch_window(swap_to=WindowState.get_window(WindowState.ID_REMOVER_V))

    def relacaoV_button03(self):
        self.switch_window(swap_to=WindowState.get_window(WindowState.ID_PESQUISAR_V))

    def relacaoV_button04(self):
        self.switch_window(swap_to=WindowState.get_window(WindowState.ID_RELACAO_C))

    def button_back(self):
        self.switch_window(swap_to=WindowState.get_window(WindowState.ID_MAIN))
