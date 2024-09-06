from tkinter import Tk
from tkinter import PhotoImage
from tkinter import *
from pathlib import Path

class Avaliacoes():
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
            text="Avaliações",
            fill="#FFFFFF",
            font=("IBMPlexSansCond Regular", 36 * -1))

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
        self.root.mainloop()

    def assets(self, filename):
        return Path(__file__).parent / "assets" / filename
    
    def button_back(self):
        pass

if __name__ == "__main__":
    Avaliacoes()