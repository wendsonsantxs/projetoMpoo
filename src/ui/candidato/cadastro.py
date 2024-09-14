from tkinter import Tk
from tkinter import Canvas
from tkinter import PhotoImage
from tkinter import Button
from tkinter import Entry

from ui.window import Window
from ui.window_state import WindowState

class CadastroCandidato(Window):
    def __init__(self, root = Tk):
        super().__init__(root)

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

        

        self.button_image_1 = PhotoImage(file=self.assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(x=105.0,  y=158.0, width=64.0, height=55.0)
        
        self.button_image_2 = PhotoImage(file=self.assets("button_2.png"))
        self.button_2 = Button(
            image = self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place( x=357.0, y=716.0, width=160.0, height=60.0)
        self.canvas.create_text(
            402.0,
            323.0,
            anchor="nw",
            text="Vaga",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )
        
        self.entry_image_1 = PhotoImage(file=self.assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
          550.0,
          373.0,
          image= self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(x=397.0, y=353.0, width=306.0, height=38.0)
        
        self.canvas.create_text(
            520.0,
            240.0,
            anchor="nw",
            text="CPF",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )
        
        self.canvas.create_text(
            130.0,
            326.0,
            anchor="nw",
            text="Telefone",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )
        
        self.canvas.create_text(
            130.0,
            426.0,
            anchor="nw",
            text="Qualidades",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )
        
        self.entry_image_2 = PhotoImage( file=self.assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            611.0,
            286.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(x=510.0, y=266.0, width=202.0, height=38.0)
        
        self.entry_image_3 = PhotoImage(file=self.assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            229.0,
            373.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=128.0,
            y=353.0,
            width=202.0,
            height=38.0
        )
        
        self.entry_image_4 = PhotoImage(file=self.assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
          420.0,
          508.0,
          image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4.place(x=128.0, y=461.0, width=584.0, height=92.0)
        
        self.entry_image_5 = PhotoImage(file=self.assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(420.0, 654.0, image = self.entry_image_5)
        self.entry_5 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_5.place(x=128.0, y=611.0, width=584.0, height=84.0)

        self.canvas.create_text(
            130.0,
            578.0,
            anchor="nw",
            text="Observações",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )
        
        self.canvas.create_text(
            130.0,
            240.0,
            anchor="nw",
            text="Nome",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )
        
        self.entry_image_6 = PhotoImage(file=self.assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(302.0, 286.0, image=self.entry_image_6)
        self.entry_6 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_6.place(x=128.0, y=266.0, width=348.0, height=38.0)
        
        self.canvas.create_text(
            169.0,
            166.0,
            anchor="nw",
            text="Cadastro de Candidatos",
            fill="#FFFFFF",
            font=("IBMPlexSansCond Regular", 36 * -1)
        )
        
        self.image_image_3 = PhotoImage(file=self.assets("image_3.png"))
        self.image_3 = self.canvas.create_image(287.0, 65.0, image=self.image_image_3)
        
        self.canvas.create_text(
            367.0,
            34.0,
            anchor="nw",
            text="Sistema De Gerenciamento De \nRecursos Humanos (Hrms)",
            fill="#FFFFFF",
            font=("Itim Regular", 22 * -1)
        )
        
        self.canvas.create_text(
            753.0,
            799.0,
            anchor="nw",
            text="W.Y.W",
            fill="#FFFFFF",
            font=("Alef Regular", 18 * -1)
        )
        
        self.image_image_4 = PhotoImage(file=self.assets("image_4.png"))
        self.image_4 = self.canvas.create_image(744.0, 812.0, image=self.image_image_4)
        
        self.canvas.create_text(
            739.0,
            806.0,
            anchor="nw",
            text="C",
            fill="#FFFFFF",
            font=("Alata Regular", 14 * -1)
        )