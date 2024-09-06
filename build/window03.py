from tkinter import Tk
from pathlib import Path
from tkinter import *


class RelacaoV():
    def __init__(self):
        self.root = Tk()
        self.logotipo = PhotoImage(file = self.assets("logo.png"))
        self.root.call('wm', 'iconphoto', self.root._w, self.logotipo)
        self.root.title('App HRMS')
        self.root.geometry("825x825")
        self.root.resizable(False, False)
        
        self.canvas = Canvas( self.root, bg = "#FFFFFF", height = 825, width = 825, bd = 0, highlightthickness = 0, relief = "ridge")

        self.canvas.place(x = 0, y = 0)

        self.bg = PhotoImage(file = self.assets("image_1.png"))
        self.image_1 = self.canvas.create_image(412.0, 412.0, image=self.bg)

        self.rectangle = PhotoImage(file = self.assets("image_2.png"))
        self.image_2 = self.canvas.create_image(407.0, 461.0, image=self.rectangle)

        self.logo = PhotoImage(file = self.assets("image_3.png"))
        self.image_3 = self.canvas.create_image(195.0, 76.0, image=self.logo)

        self.canvas.create_text(
            284.0,
            46,
            anchor="nw",
            text="Sistema De Gerenciamento De\nRecursos Humanos (Hrms)",
            fill="#FFFFFF",
            font=("Itim Regular", 30 * -1)
        )

        self.button_image_1 = PhotoImage(file = self.assets("button_1.png"))
        self.button_1 = Button(
            image = self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command = self.relacaoV_button01,
            relief="flat"
        )
        self.button_1.place(x=494.0, y=307.0, width=172.0, height=60.0)

        self.button_image_2 = PhotoImage(file = self.assets("button_1.png"))
        self.button_2 = Button(
            image= self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command = self.relacaoV_button02,
            relief="flat"
        )
        self.button_2.place(x=494.0, y=464.0, width=172.0, height=60.0)

        self.button_image_3 = PhotoImage(file = self.assets("button_1.png"))
        self.button_3 = Button(
            image= self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command = self.relacaoV_button03,
            relief="flat"
        )
        self.button_3.place( x=494.0, y=618.0, width=172.0,height=60.0)

        self.canvas.create_text(
            217.0,
            311.0,
            anchor="nw",
            text="Cadastrar Vagas",
            fill="#FFFFFF",
            font=("Itim Regular", 30 * -1)
        )

        self.canvas.create_text(
            234.0,
            474.0,
            anchor="nw",
            text="Vagas Ativas",
            fill="#FFFFFF",
            font=("Itim Regular", 30 * -1)
        )

        self.canvas.create_text(
            201.0,
            629.0,
            anchor="nw",
            text="Banco De Talentos",
            fill="#FFFFFF",
            font=("Itim Regular", 30 * -1)
        )

        self.canvas.create_text(
            742.0,
            789.0,
            anchor="nw",
            text="W.Y.W",
            fill="#FFFFFF",
            font=("Alef Regular", 18 * -1)
        )

        self.image_image_4 = PhotoImage(file = self.assets("image_4.png"))
        self.image_4 = self.canvas.create_image(730.0, 800.0, image = self.image_image_4)

        self.canvas.create_text(
            725.0,
            792.0,
            anchor="nw",
            text="C",
            fill="#FFFFFF",
            font=("Alata Regular", 14 * -1)
        )

        self.button_image_4 = PhotoImage(file = self.assets("button_2.png"))
        self.button_4 = Button(
            image = self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command = self.button_back,
            relief="flat"
        )
        self.button_4.place(x=169.0, y=201.0, width=64.0, height=55.0)

        self.root.mainloop()

    def relacaoV_button01(self):
        pass

    def relacaoV_button02(self):
        pass

    def relacaoV_button03(self):

        pass

    def button_back(self):
        pass

    def assets(self, filename):
        return Path(__file__).parent / "assets" / filename
    

if __name__ == '__main__':
    RelacaoV()