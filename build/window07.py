from tkinter import Tk
from tkinter import PhotoImage
from tkinter import *
from tkfunction import Tk_function

class CadastroT(Tk_function):
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

        self.button_image_1 = PhotoImage(file = Tk_function.assets("button_2.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth = 0,
            highlightthickness = 0,
            command = Tk_function.register_coaching,
            relief="flat"
        )
        self.button_1.place(x = 100.0, y = 158.0, width = 64.0, height = 55.0)

        self.button_image_2 = PhotoImage(file = Tk_function.assets("button_3.png"))
        self.button_2 = Button(
            image = self.button_image_2,
            borderwidth = 0,
            highlightthickness = 0,
            command = Tk_function.register_coaching_back,
            relief = "flat"
        )
        self.button_2.place( x=357.0, y=716.0, width=160.0, height=60.0)

        self.canvas.create_text(
            546.0,
            605.0,
            anchor = "nw",
            text = "Data de Término",
            fill = "#F3F3F3",
            font = ("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_1 = PhotoImage(file=Tk_function.assets("entry6_4.png"))
        self.entry_bg_1 = self.canvas.create_image(617.5, 656.0, image = self.entry_image_1) 
        self.entry_1 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font= ("IBMPlexSansCond Regular", 16 * -1))
        self.entry_1.place(x=548.0, y=636.0, width=139.0, height=38.0)

        self.canvas.create_text(
            196.0,
            322.0,
            anchor="nw",
            text="Descrição",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.canvas.create_text(
            196.0,
            462.0,
            anchor="nw",
            text="Participantes",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_2 = PhotoImage(file=Tk_function.assets("entry6_2.png"))
        self.entry_bg_2 = self.canvas.create_image(440.5, 403.0, image=self.entry_image_2)
        self.entry_2 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=194.0, y=356.0, width=493.0, height=92.0)

        self.entry_image_3 = PhotoImage(file=Tk_function.assets("entry6_2.png"))
        self.entry_bg_3 = self.canvas.create_image(440.5, 542.0, image = self.entry_image_3)
        self.entry_3 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_3.place( x=194.0, y=495.0, width=493.0, height=92.0)

        self.canvas.create_text(
            194.0,
            605.0,
            anchor="nw",
            text="Data de Inicio",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_4 = PhotoImage(file=Tk_function.assets("entry6_4.png"))
        self.entry_bg_4 = self.canvas.create_image(263.5, 655.0, image = self.entry_image_4)
        self.entry_4 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_4.place(x=194.0, y=635.0, width=139.0, height=38.0)

        self.canvas.create_text(
            196.0,
            240.0,
            anchor="nw",
            text="Título",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_5 = PhotoImage(file=Tk_function.assets("entry6_5.png"))
        self.entry_bg_5 = self.canvas.create_image(440.5, 290.0, image=self.entry_image_5)
        self.entry_5 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font= ("IBMPlexSansCond Regular", 16 * -1))
        self.entry_5.place(x=194.0, y=270.0, width=493.0, height=38.0)

        self.canvas.create_text(
            381.0,
            605.0,
            anchor="nw",
            text="Duração (Horas)",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_6 = PhotoImage(file=Tk_function.assets("entry6_6.png"))
        self.entry_bg_6 = self.canvas.create_image( 440.5, 656.0, image = self.entry_image_6)
        self.entry_6 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font= ("IBMPlexSansCond Regular", 16 * -1))
        self.entry_6.place( x=386.0, y=636.0, width=109.0, height=38.0)

        self.canvas.create_text(
            172.0,
            166.0,
            anchor="nw",
            text="Cadastro de Treinamentos",
            fill="#FFFFFF",
            font=("IBMPlexSansCond Regular", 36 * -1)
        )

        self.canvas.create_text(
            753.9,
            801.0,
            anchor="nw",
            text="W.Y.W",
            fill="#FFFFFF",
            font=("Alef Regular", 18 * -1)
        )

        self.image_image_4 = PhotoImage(file=Tk_function.assets("image_4.png"))
        self.image_4 = self.canvas.create_image(744.0, 812.0, image = self.image_image_4)

        self.canvas.create_text(739.0, 804.0, anchor="nw", text="C", fill="#FFFFFF", font=("Alata Regular", 14 * -1))


root = Tk()
app = CadastroT(root)
root.mainloop()