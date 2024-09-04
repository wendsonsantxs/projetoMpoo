from tkinter import Tk
from tkinter import PhotoImage
from tkinter import *
from tkfunction import Tk_function

class RelacaoT(Tk_function):
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

        self.canvas.create_text(
            286.0,
            40,
            anchor="nw",
            text="Sistema De Gerenciamento De\nRecursos Humanos (Hrms)",
            fill="#FFFFFF",
            font=("Itim Regular", 30 * -1)
        )

        self.button_image_1 = PhotoImage(file = Tk_function.assets("button_1.png"))
        self.button_1 = Button(
            image = self.button_image_1,
            borderwidth = 0,
            highlightthickness = 0,
            command = Tk_function.relacaoT_button01,
            relief = "flat"
        )
        self.button_1.place(x=510.0, y=307.0, width=172.0, height=60.0)

        self.button_image_2 = PhotoImage(file = Tk_function.assets("button_1.png"))
        self.button_2 = Button(
            image= self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command = Tk_function.relacaoT_button02,
            relief="flat"
        )
        self.button_2.place(x=510.0, y=464.0, width=172.0, height=60.0)

        self.button_image_3 = PhotoImage(file = Tk_function.assets("button_1.png"))
        self.button_3 = Button(
            image= self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command = Tk_function.relacaoT_button03,
            relief="flat"
        )
        self.button_3.place( x=510.0, y=618.0, width=172.0,height=60.0)

        self.canvas.create_text(
            182.0,
            317.0,
            anchor="nw",
            text="Cadastrar Treinamento",
            fill="#FFFFFF",
            font=("Itim Regular", 30 * -1)
        )

        self.canvas.create_text(
            200.0,
            474.0,
            anchor="nw",
            text="Treinamentos Ativos",
            fill="#FFFFFF",
            font=("Itim Regular", 30 * -1)
        )

        self.canvas.create_text(
            165.0,
            629.0,
            anchor="nw",
            text="Histórico de Treinamento",
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

        self.image_image_4 = PhotoImage(file = Tk_function.assets("image_4.png"))
        self.image_4 = self.canvas.create_image(730.0, 800.0, image = self.image_image_4)

        self.canvas.create_text(
            725.0,
            792.0,
            anchor="nw",
            text="C",
            fill="#FFFFFF",
            font=("Alata Regular", 14 * -1)
        )

        self.button_image_4 = PhotoImage(file = Tk_function.assets("button_2.png"))
        self.button_4 = Button(
            image = self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command = Tk_function.relacaoT_back,
            relief="flat"
        )
        self.button_4.place(x=169.0, y=201.0, width=64.0, height=55.0)

root = Tk()
app = RelacaoT(root)
root.mainloop()