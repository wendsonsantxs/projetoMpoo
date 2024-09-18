from tkinter import Button
from tkinter import Canvas
from tkinter import PhotoImage
from tkinter import Tk

from ui.window import Window
from ui.window_state import WindowState
from ui.funcionarios.cadastro import CadastroF
from ui.funcionarios.remover import Remocao
from ui.funcionarios.pesquisar.window import PesquisarF

class FuncionariosWindow(Window):
    def __init__(self, root: Tk):
        super().__init__(root=root)
        WindowState.set_window(WindowState.ID_CADASTRO_F, CadastroF(root=self.root))
        WindowState.set_window(WindowState.ID_REMOCAO_F, Remocao(root=self.root))
        WindowState.set_window(WindowState.ID_PESQUISA_F, PesquisarF(root=self.root))
 
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
        self.image_3 = self.canvas.create_image(200.0, 76.0, image=self.logo)

        self.canvas.create_text(
            285.0,
            42.99999999999999,
            anchor="nw",
            text="Sistema De Gerenciamento De\nRecursos Humanos (Hrms)",
            fill="#FFFFFF",
            font=("Itim Regular", 30 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=self.assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.relacaoF_button01,
            relief="flat"
        )
        self.button_1.place(x=502.0, y=325.0, width=172.0, height=60.0)

        self.button_image_2 = PhotoImage(
            file=self.assets("button_1.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.relacaoF_button02,
            relief="flat"
        )
        self.button_2.place(x=502.0,  y=455.0, width=172.0, height=60.0)

        self.button_image_3 = PhotoImage(
            file=self.assets("button_1.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.relacaoF_button03,
            relief="flat"
        )
        self.button_3.place(x=502.0, y=577.0, width=172.0, height=60.0)

        self.canvas.create_text(
            164.0,
            336.0,
            anchor="nw",
            text="Cadastro De Funcionário",
            fill="#FFFFFF",
            font=("Itim Regular", 29 * -1)
        )

        self.canvas.create_text(
            192.0,
            466.0,
            anchor="nw",
            text="Remover Funcionário",
            fill="#FFFFFF",
            font=("Itim Regular", 30 * -1)
        )

        self.canvas.create_text(
            258.0,
            590.0,
            anchor="nw",
            text="Pesquisar",
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

        self.image_image_4 = PhotoImage(
            file=self.assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            730.0, 798.0, image=self.image_image_4)

        self.canvas.create_text(
            725.0,
            790.0,
            anchor="nw",
            text="C",
            fill="#FFFFFF",
            font=("Alata Regular", 14 * -1)
        )

        self.button_image_5 = PhotoImage(
            file=self.assets("button_2.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_back,
            relief="flat"
        )
        self.button_5.place(x=159.0, y=193.0, width=64.0, height=55.0)

    def relacaoF_button01(self):
        self.switch_window(swap_to=WindowState.get_window(WindowState.ID_CADASTRO_F))

    def relacaoF_button02(self):
        self.switch_window(swap_to=WindowState.get_window(WindowState.ID_REMOCAO_F))

    def relacaoF_button03(self):
        self.switch_window(swap_to=WindowState.get_window(WindowState.ID_PESQUISA_F))

    def button_back(self):
        self.switch_window(swap_to=WindowState.get_window(WindowState.ID_MAIN))
