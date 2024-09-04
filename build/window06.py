from tkinter import Tk
from tkinter.ttk import *
from tkinter import *
from tkfunction import Tk_function

class CadastroV(Tk_function):
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

        self.rectangle = PhotoImage(file = Tk_function.assets("image2_2.png"))
        self.image_2 = self.canvas.create_image(410.0, 461.0, image=self.rectangle)

        self.logo = PhotoImage(file = Tk_function.assets("image_3.png"))
        self.image_3 = self.canvas.create_image(195.0, 66.0, image=self.logo)

        self.canvas.create_text(
            271.0, 36,
            anchor = "nw",
            text = "Sistema De Gerenciamento De\nRecursos Humanos(HRMS)",
            fill = "#FFFFFF",
            font = ("Itim", 30 * -1)
        )

        self.button_image_1 = PhotoImage(file=Tk_function.assets("button_2.png"))
        self.button_1 = Button(
            image = self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command = Tk_function.register_vacancy_back,
            relief="flat"
        )
        self.button_1.place(x=107.0, y=155.0, width=64.0, height=55.0)

        self.button_image_2 = PhotoImage(file=Tk_function.assets("button_3.png"))
        self.button_2 = Button(
            image = self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command = Tk_function.register_vacancy,
            relief="flat"
        )
        self.button_2.place( x=333.0, y=704.0, width=161.0, height=60.0)

        self.canvas.create_text(
            189.0,
            332.0,
            anchor="nw",
            text="Requisitos",  
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_1 = PhotoImage(file=Tk_function.assets("entry5_1.png"))
        self.entry_bg_1 = self.canvas.create_image(    408.5, 398.0, image = self.entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=194.0, y=362.0, width=429.0, height=70.0)

        self.canvas.create_text(
            189.0,
            458.0,
            anchor="nw",
            text="Descrição",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_2 = PhotoImage(file = Tk_function.assets("entry5_6.png"))
        self.entry_bg_2 = self.canvas.create_image(408.5, 535.0, image = self.entry_image_2)
        self.entry_2 = Entry(bd = 0, bg = "#FFFFFF", fg = "#000716", highlightthickness = 0)
        self.entry_2.place(x=194.0, y=488.0, width=429.0, height=92.0)

        self.canvas.create_text(
            189.0,
            599.0,
            anchor="nw",
            text="Data de Publicação",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_3 = PhotoImage(file=Tk_function.assets("entry5_3.png"))
        self.entry_bg_3 = self.canvas.create_image(297.0, 655.0, image = self.entry_image_3)
        self.entry_3 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font= ("IBMPlexSansCond Regular", 16 * -1))
        self.entry_3.place(x=194.0, y=635.0, width=206.0, height=38.0)

        self.canvas.create_text(
            196.0,
            240.0,
            anchor="nw",
            text="Título",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_4 = PhotoImage(file=Tk_function.assets("entry5_4.png"))
        self.entry_bg_4 = self.canvas.create_image(408.5, 290.0, image = self.entry_image_4)
        self.entry_4 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_4.place(x=194.0, y=270.0, width=429.0, height=38.0)

        self.canvas.create_text(
            444.0,
            599.0,
            anchor="nw",
            text="Duração até a seleção",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_5 = PhotoImage(file=Tk_function.assets("entry5_2.png"))
        self.entry_bg_5 = self.canvas.create_image(537.5, 655.0, image = self.entry_image_5)
        self.entry_5 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_5.place(x=452.0, y=635.0, width=171.0, height=38.0)

        self.canvas.create_text(
            185.0,
            167.0,
            anchor="nw",
            text="Cadastro de Vagas",
            fill="#FFFFFF",
            font=("IBMPlexSansCond Regular", 36 * -1)
        )

        self.canvas.create_text(
            752.0,
            797.0,
            anchor="nw",
            text="W.Y.W",
            fill="#FFFFFF",
            font=("Alef Regular", 18 * -1)
        )

        self.image_image_4 = PhotoImage(file = Tk_function.assets("image_4.png"))
        self.image_4 = self.canvas.create_image( 742.0, 808.0, image = self.image_image_4)

        self.canvas.create_text(
            737.0,
            800.0,
            anchor="nw",
            text="C",
            fill="#FFFFFF",
            font=("Alata Regular", 14 * -1)
        )

root = Tk()
app = CadastroV(root)
root.mainloop()