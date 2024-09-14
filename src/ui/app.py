import os

from tkinter import Tk
from tkinter import Button
from tkinter import Canvas
from tkinter import PhotoImage

from ui.funcionarios.window import FuncionariosWindow
from ui.vagas.window import VagasWindow
from ui.treinamentos.window import TreinamentosWindow
from ui.window import Window
from ui.window_state import WindowState


class MainWindow(Window):
    def __init__(self, title: str = 'App HRMS', width: int = 825 , height: int = 825):
        self.root = Tk()
        self.root.title(string=title)
        self.root.geometry(newGeometry=f'{width}x{height}')
        self.root.resizable(width=False, height=False)
        self.load_icon()

        # TODO: set this state on main
        WindowState.set_window(window_id=WindowState.ID_MAIN, target_window=self)
        WindowState.set_window(window_id=WindowState.ID_RELACAO_F, target_window=FuncionariosWindow(root=self.root))
        WindowState.set_window(window_id=WindowState.ID_RELACAO_V, target_window=VagasWindow(root=self.root))
        WindowState.set_window(window_id=WindowState.ID_RELACAO_T, target_window=TreinamentosWindow(root=self.root))
        

    def load_icon(self):
        try:
            icon_path = self.assets(filename='logo.png')
            self.icon = PhotoImage(file=icon_path) 
            self.root.iconphoto(True, self.icon)
        except Exception as e:
            print(f"Error setting icon: {e}")
            os._exit(1)

    def create(self):
        self.canvas = Canvas(self.root, bg="#FFFFFF", height=825,
                             width=825, bd=0, highlightthickness=0, relief="ridge")

        self.canvas.place(x=0, y=0)

        self.bg = PhotoImage(file=self.assets("image_1.png"))
        self.image_1 = self.canvas.create_image(412.0, 412.0, image=self.bg)

        self.rectangle = PhotoImage(file=self.assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            407.0, 461.0, image=self.rectangle)

        self.logo = PhotoImage(file=self.assets("image_3.png"))
        self.image_3 = self.canvas.create_image(195.0, 76.0, image=self.logo)

        self.canvas.create_text(
            271.0, 40,
            anchor="nw",
            text="Sistema De Gerenciamento De\nRecursos Humanos(HRMS)",
            fill="#FFFFFF",
            font=("Itim", 30 * -1)
        )

        self.button_image_1 = PhotoImage(file=self.assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.tela_button01,
            relief="flat"
        )
        self.button_1.place(x=500.0, y=289.0, width=170.0, height=60.0)

        self.button_image_2 = PhotoImage(file=self.assets("button_1.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.tela_button02,
            relief="flat"
        )
        self.button_2.place(
            x=500.0,
            y=445.0,
            width=170.0,
            height=60.0
        )

        self.button_image_3 = PhotoImage(file=self.assets("button_1.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=1,
            command=self.tela_button03,
            relief="flat"
        )
        self.button_3.place(x=500.0, y=585.0, width=172.0, height=60.0)

        self.canvas.create_text(
            146.0,
            300.0,
            anchor="nw",
            text="Relação De Funcionários",
            fill="#FFFFFF",
            font=("Itim Regular", 30 * -1)
        )

        self.canvas.create_text(
            195.0,
            460.0,
            anchor="nw",
            text="Relações De Vagas",
            fill="#FFFFFF",
            font=("Itim Regular", 30 * -1)
        )

        self.canvas.create_text(
            225.0,
            599.0,
            anchor="nw",
            text="Treinamentos",
            fill="#FFFFFF",
            font=("Itim Regular", 30 * -1)
        )

        self.canvas.create_text(
            720.0,
            784.0,
            anchor="nw",
            text="W.Y.W",
            fill="#FFFFFF",
            font=("Alef Regular", 18 * -1)
        )

        self.image_image_4 = PhotoImage(file=self.assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            709.0,
            795.0,
            image=self.image_image_4
        )

        self.canvas.create_text(
            704.0,
            787.0,
            anchor="nw",
            text="C",
            fill="#FFFFFF",
            font=("Alata Regular", 14 * -1)
        )

  
    def tela_button01(self):
        self.switch_window(swap_to=WindowState.get_window(WindowState.ID_RELACAO_F))

    def tela_button02(self):
        self.switch_window(swap_to=WindowState.get_window(WindowState.ID_RELACAO_V))

    def tela_button03(self):
        self.switch_window(swap_to=WindowState.get_window(WindowState.ID_RELACAO_T))
