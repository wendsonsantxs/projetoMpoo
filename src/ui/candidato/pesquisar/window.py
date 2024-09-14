from tkinter import Tk
from tkinter import Canvas
from tkinter import PhotoImage
from tkinter import Button

from ui.window import Window
from ui.window_state import WindowState
from ui.candidato.pesquisar.candidato import CandidatoPesquisar
from ui.candidato.pesquisar.banco_talento import BancoT


class PesquisarWindow(Window):
    def __init__(self, root = Tk):
        super().__init__(root)
        WindowState.set_window(WindowState.ID_CANDIDATO_PESQUISAR, CandidatoPesquisar(root=self.root))
        WindowState.set_window(WindowState.ID_BANCO_TALENTO, BancoT(root=self.root))

    def create(self):
        super().create()
        
        self.canvas = Canvas( self.root, bg = "#FFFFFF", height = self.height, 
                             width = self.width, bd = 0, highlightthickness = 0, relief = "ridge")

        self.canvas.place(x = 0, y = 0)
        self.bg = PhotoImage(file=self.assets("image_1.png"))
        self.image_1 = self.canvas.create_image(412.0, 412.0, image=self.bg)

        self.rectangle = PhotoImage(file=self.assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            407.0, 461.0, image=self.rectangle)

        self.logo = PhotoImage(file=self.assets("image_3.png"))
        self.image_3 = self.canvas.create_image(200.0, 76.0, image=self.logo)

        self.canvas.create_text(
            285.0,
            42.99999999999999,
            anchor="nw",
            text="Sistema De Gerenciamento De\nRecursos Humanos (Hrms)",
            fill="#FFFFFF",
            font=("Itim Regular", 27 * -1)
        )

        self.button_image_1 = PhotoImage(file=self.assets("button_1.png"))

        self.button_1 = Button(
            image = self.button_image_1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.button_P1,
            relief = "flat"
        )
        self.button_1.place(x=500.0, y=370.0, width=172.0, height=60.0)

        self.button_2 = Button(
            image = self.button_image_1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.button_P2,
            relief = "flat"
        )
        self.button_2.place(x=500.0, y=545.0, width=172.0, height=60.0)

        self.canvas.create_text(
            249.0,
            205.0,
            anchor="nw",
            text="Pesquisar",
            fill="#FFFFFF",
            font=("Itim Regular", 33 * -1)
        )

    
        self.canvas.create_text(
            200,
            380,
            anchor="nw",
            text="Pesquisar Candidato",
            fill="#FFFFFF",
            font=("Itim Regular", 30 * -1)
        )

        self.canvas.create_text(
            200.0,
            555.0,
            anchor="nw",
            text="Banco De Talentos",
            fill="#FFFFFF",
            font=("Itim Regular", 30 * -1)
        )

        self.canvas.create_text(
            741.0,
            788.0,
            anchor="nw",
            text="W.Y.W",
            fill="#FFFFFF",
            font=("Alef Regular", 18 * -1)
        )

        self.image_image_4 = PhotoImage(file=self.assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            730.0,
            800.0,
            image=self.image_image_4
        )

        self.canvas.create_text(
            725.0,
            792.0,
            anchor="nw",
            text="C",
            fill="#FFFFFF",
            font=("Alata Regular", 14 * -1)
        )

        self.button_image_2 = PhotoImage(file = self.assets("button_2.png"))
        self.button_3 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_back,
            relief="flat"
        )
        self.button_3.place(x=169.0, y=201.0, width=64.0, height=55.0)


    def button_P1(self):
        self.switch_window(WindowState.get_window(WindowState.ID_CANDIDATO_PESQUISAR))

    def button_P2(self):
        self.switch_window(WindowState.get_window(WindowState.ID_BANCO_TALENTO))

    def button_back(self):
        self.switch_window(WindowState.get_window(WindowState.ID_RELACAO_C))