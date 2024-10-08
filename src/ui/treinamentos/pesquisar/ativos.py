from tkinter import Button
from tkinter import Canvas
from tkinter import PhotoImage
from tkinter import Tk
from tkinter import Entry

from ui.window import Window
from ui.window_state import WindowState

class TreinamentoAt(Window):
    def __init__(self, root = Tk):
        super().__init__(root)

    def create(self):
        super().create()
        self.canvas = Canvas( self.root, bg = "#FFFFFF", height = self.height, width = self.width, 
                             bd = 0, highlightthickness = 0, relief = "ridge")

        self.canvas.place(x = 0, y = 0)
        self.bg = PhotoImage(file = self.assets("image_1.png"))
        self.image_1 = self.canvas.create_image(412.0, 412.0, image=self.bg)

        self.rectangle = PhotoImage(file = self.assets("image2_2.png")) #rectangle
        self. image_2 = self.canvas.create_image(417.0, 457.0, image = self.rectangle)

        self.button_image_1 = PhotoImage(file = self.assets("button_2.png"))
        self.button_1 = Button(
            image = self.button_image_1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.button_back,
            relief = "flat"
        )
        self.button_1.place( x=110.0, y=140.0,  width=64.0, height=55.0)

        self.canvas.create_text(
            189.0,
            147.0,
            anchor="nw",
            text="Treinamentos Ativos",
            fill="#FFFFFF",
            font=("IBMPlexSansCond Regular", 32 * -1))

        self.image_image_3 = PhotoImage(file = self.assets("image_3.png"))
        self.image_3 = self.canvas.create_image(284.0,  62.0,  image=self.image_image_3)

        self. canvas.create_text(
            362.0,
            39.0,
            anchor="nw",
            text="Sistema De Gerenciamento De \nRecursos Humanos (Hrms)",
            fill="#FFFFFF",
            font=("Itim Regular", 22 * -1)
        )

        self. canvas.create_text(
            757.0,
            800.0,
            anchor="nw",
            text="W.Y.W",
            fill="#FFFFFF",
            font=("Alef Regular", 18 * -1)
        )

        self. image_image_4 = PhotoImage(file = self.assets("image_4.png"))
        self. image_4 = self.canvas.create_image(744.0,  812.0, image=self.image_image_4)

        self. canvas.create_text(
            739.0,
            804.0,
            anchor="nw",
            text="C",
            fill="#FFFFFF",
            font=("Alata Regular", 14 * -1)
            )
            
        # self.entry_image_1 = PhotoImage(file=self.assets("entry4_2.png"))
        # self.entry_bg_1 = self.canvas.create_image(
        #     605.0, 168.0, image=self.entry_image_1)
        # self.entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=(
        #     "IBMPlexSansCond Regular", 16 * -1))
        # self.entry_1.place(
        #     x=520.0,
        #     y=152.0,
        #     width=182.0,
        #     height=33.0)
        
        # self.button_image_2 = PhotoImage(file = self.assets("button_4.png"))
        # self.button_2 = Button(
        #     image = self.button_image_2,
        #     borderwidth = 0,
        #     highlightthickness = 0,
        #     command = self.button_back,
        #     relief = "flat"
        # )
        # self.button_2.place( x=706.0, y=149.3,  width=34.0, height=37.0)
        
    def button_back(self):
        self.switch_window(WindowState.get_window(WindowState.ID_PESQUISAR_T))

    def button_search(self):
        pass