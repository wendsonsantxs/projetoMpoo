
from tkinter import *
from tkfunction import *

class Tela(Tk_function):
    def __init__(self, root):
        self.root = root
        self.logotipo = PhotoImage(file = Tk_function.assets("logo.png"))
        self.root.call('wm', 'iconphoto', root._w, self.logotipo)
        self.root.title('App HRMS')
        self.root.geometry("825x825")
        root.resizable(False, False)
        
        self.canvas = Canvas( root, bg = "#FFFFFF", height = 825, width = 825, bd = 0, highlightthickness = 0, relief = "ridge")

        self.canvas.place(x = 0, y = 0)

        self.bg = PhotoImage(file = Tk_function.assets("image_1.png"))
        self.image_1 = self.canvas.create_image(412.0, 412.0, image=self.bg)

        self.rectangle = PhotoImage(file = Tk_function.assets("image_2.png"))
        self.image_2 = self.canvas.create_image(407.0, 461.0, image=self.rectangle)

        self.logo = PhotoImage(file = Tk_function.assets("image_3.png"))
        self.image_3 = self.canvas.create_image(195.0, 76.0, image=self.logo)
        #

        self.canvas.create_text(
            271.0, 40,
            anchor="nw",
            text="Sistema De Gerenciamento De\nRecursos Humanos(HRMS)",
            fill="#FFFFFF",
            font=("Itim", 30 * -1)
        )

        self.button_image_1 = PhotoImage(file = Tk_function.assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command = Tk_function.tela_button01,
            relief="flat"
        )
        self.button_1.place(x=500.0, y=289.0, width=170.0, height=60.0)

        self.button_image_2 = PhotoImage(file = Tk_function.assets("button_1.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=Tk_function.tela_button02,
            relief="flat"
        )
        self.button_2.place(
            x=500.0,
            y=445.0,
            width=170.0,
            height=60.0
        )

        self.button_image_3 = PhotoImage(file = Tk_function.assets("button_1.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth = 0,
            highlightthickness = 1,
            command = Tk_function.tela_button03,
            relief = "flat"
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

        self.image_image_4 = PhotoImage(file = Tk_function.assets("image_4.png"))
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
        

root = Tk()
app = Tela(root)
root.mainloop()