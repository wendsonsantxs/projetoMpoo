from tkinter import Tk
from tkinter import Button
from tkinter import Canvas
from tkinter import PhotoImage

from ui.window import Window
from ui.window_state import WindowState

from ui.candidato.cadastro import CadastroCandidato
from ui.candidato.remover import RemoverC
from ui.candidato.pesquisar.window import PesquisarWindow

class CandidatoWindow(Window):
    def __init__(self, root = Tk):
        super().__init__(root)
        WindowState.set_window(WindowState.ID_CADASTRO_C, CadastroCandidato(root=self.root))
        WindowState.set_window(WindowState.ID_REMOVER_C, RemoverC(root=self.root))
        WindowState.set_window(WindowState.ID_PESQUISAR_C, PesquisarWindow(root=self.root))

    def create(self):
        super().create()
        
        self.canvas = Canvas(self.root, bg = "#FFFFFF", height = self.height, width = self.width,
                             bd = 0, highlightthickness = 0, relief = "ridge")

        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(file=self.assets("image_1.png"))
        self.image_1 = self.canvas.create_image(412.0, 412.0, image= self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.assets("image_2.png"))
        self.image_2 = self.canvas.create_image(424.0, 476.0, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=self.assets("image_3.png"))
        self.image_3 = self.canvas.create_image(222.0, 92.0, image=self.image_image_3)

        self.canvas.create_text(
            299.0,
            57.0,
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
            command= self.button1,
            relief="flat"
        )
        self.button_1.place(x=494.0, y=307.0, width=172.0, height=60.0)

        self.button_image_2 = PhotoImage(file=self.assets("button_1.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command= self.button2,
            relief="flat"
        )
        self.button_2.place(x=494.0, y=464.0, width=172.0, height=60.0)

        self.button_image_3 = PhotoImage(file=self.assets("button_1.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command= self.button3,
            relief="flat"
        )
        self.button_3.place(x=494.0, y=618.0, width=172.0, height=60.0)

        self.canvas.create_text(
            184.0,
            311.0,
            anchor="nw",
            text="Cadastrar Candidato",
            fill="#FFFFFF",
            font=("Itim Regular", 30 * -1)
        )

        self.canvas.create_text(
            190.0,
            472.0,
            anchor="nw",
            text="Remover Candidato",
            fill="#FFFFFF",
            font=("Itim Regular", 30 * -1)
        )

        self.canvas.create_text(
            190.0,
            629.0,
            anchor="nw",
            text="Pesquisar Candidato",
            fill="#FFFFFF",
            font=("Itim Regular", 30 * -1)
        )

        self.canvas.create_text(
            742.0,
            787.0,
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
            724.0,
            791.0,
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
            command= self.button_back,
            relief="flat"
        )
        self.button_4.place(x=169.0, y=201.0, width=64.0, height=55.0)

    def button1(self):
        self.switch_window(swap_to=WindowState.get_window(WindowState.ID_CADASTRO_C))
    
    def button2(self):
        self.switch_window(swap_to=WindowState.get_window(WindowState.ID_REMOVER_C))

    def button3(self):
        self.switch_window(swap_to=WindowState.get_window(WindowState.ID_PESQUISAR_C))

    def button_back(self):
        self.switch_window(swap_to=WindowState.get_window(WindowState.ID_RELACAO_V))