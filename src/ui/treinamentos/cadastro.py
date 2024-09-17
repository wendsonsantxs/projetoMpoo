from tkinter import Button
from tkinter import Canvas
from tkinter import PhotoImage
from tkinter import Tk
from tkinter import Entry
from tkinter import Text
from tkinter import Scrollbar

from ui.window import Window
from ui.window_state import WindowState

class CadastroT(Window):
    def __init__(self, root = Tk):
        super().__init__(root)

    def create(self):
        super().create() 
        self.canvas = Canvas( self.root, bg = "#FFFFFF", height = self.height, width = self.width, 
                             bd = 0, highlightthickness = 0, relief = "ridge")

        self.canvas.place(x = 0, y = 0)

        self.bg = PhotoImage(file = self.assets("image_1.png"))
        self.image_1 = self.canvas.create_image(412.0, 412.0, image=self.bg)

        self.rectangle = PhotoImage(file = self.assets("image2_2.png"))
        self.image_2 = self.canvas.create_image(410.0, 461.0, image=self.rectangle)

        self.logo = PhotoImage(file = self.assets("image_3.png"))
        self.image_3 = self.canvas.create_image(195.0, 66.0, image=self.logo)

        self.canvas.create_text(
            271.0, 36,
            anchor = "nw",
            text = "Sistema De Gerenciamento De\nRecursos Humanos(HRMS)",
            fill = "#FFFFFF",
            font = ("Itim", 30 * -1)
        )

        self.button_image_1 = PhotoImage(file = self.assets("button_2.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.button_back,
            relief="flat"
        )
        self.button_1.place(x = 100.0, y = 158.0, width = 64.0, height = 55.0)

        self.button_image_2 = PhotoImage(file = self.assets("button_3.png"))
        self.button_2 = Button(
            image = self.button_image_2,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.register_coaching,
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

        self.entry_image_1 = PhotoImage(file=self.assets("entry6_4.png"))
        self.entry_bg_1 = self.canvas.create_image(617.5, 656.0, image = self.entry_image_1) 
        self.entry_1 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font= ("IBMPlexSansCond Regular", 16 * -1))
        self.entry_1.place(x=548.0, y=636.0, width=139.0, height=38.0)

        self.entry_placeholder_1 = "DD/MM/AAAA"
        self.entry_1.insert(0, self.entry_placeholder_1)
        self.entry_1.bind("<FocusIn>", lambda event: self.clear_placeholder(event, self.entry_1, self.entry_placeholder_1))
        self.entry_1.bind("<FocusOut>", lambda event: self.add_placeholder(event, self.entry_1, self.entry_placeholder_1))

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

        self.entry_image_2 = PhotoImage(file=self.assets("entry6_2.png"))
        self.entry_bg_2 = self.canvas.create_image(440.5, 403.0, image=self.entry_image_2)
        self.entry_2 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font= ("IBMPlexSansCond Regular", 16 * -1))
        self.entry_2.place(x=194.0, y=356.0, width=493.0, height=92.0)

        self.scrollbar_2 = Scrollbar(self.root, orient = "vertical", command=self.entry_2.yview)
        self.entry_2.configure(yscrollcommand=self.scrollbar_2.set)
        self.scrollbar_2.place_forget()

        self.entry_2.bind("<KeyRelease>", self.check_scrollbar_2)
        self.entry_2.bind("<Configure>", self.check_scrollbar_2)

        self.entry_image_3 = PhotoImage(file=self.assets("entry6_2.png"))
        self.entry_bg_3 = self.canvas.create_image(440.5, 542.0, image = self.entry_image_3)
        self.entry_3 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font= ("IBMPlexSansCond Regular", 16 * -1))
        self.entry_3.place( x=194.0, y=495.0, width=493.0, height=92.0)

        self.scrollbar_3 = Scrollbar(self.root, orient = "vertical", command=self.entry_3.yview)
        self.entry_3.configure(yscrollcommand=self.scrollbar_3.set)
        self.scrollbar_3.place_forget()

        self.entry_3.bind("<KeyRelease>", self.check_scrollbar_3)
        self.entry_3.bind("<Configure>", self.check_scrollbar_3)

        self.canvas.create_text(
            194.0,
            605.0,
            anchor="nw",
            text="Data de Inicio",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_4 = PhotoImage(file=self.assets("entry6_4.png"))
        self.entry_bg_4 = self.canvas.create_image(263.5, 655.0, image = self.entry_image_4)
        self.entry_4 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font= ("IBMPlexSansCond Regular", 16 * -1))
        self.entry_4.place(x=194.0, y=635.0, width=139.0, height=38.0)

        self.entry_placeholder_4 = "DD/MM/AAAA"
        self.entry_4.insert(0, self.entry_placeholder_4)
        self.entry_4.bind("<FocusIn>", lambda event: self.clear_placeholder(event, self.entry_4, self.entry_placeholder_4))
        self.entry_4.bind("<FocusOut>", lambda event: self.add_placeholder(event, self.entry_4, self.entry_placeholder_4))

        self.canvas.create_text(
            196.0,
            240.0,
            anchor="nw",
            text="Título",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_5 = PhotoImage(file=self.assets("entry6_5.png"))
        self.entry_bg_5 = self.canvas.create_image(440.5, 290.0, image=self.entry_image_5)
        self.entry_5 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font= ("IBMPlexSansCond Regular", 16 * -1))
        self.entry_5.place(x=194.0, y=270.0, width=493.0, height=38.0)

        self.canvas.create_text(
            381.0,
            605.0,
            anchor="nw",
            text="Duração",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_6 = PhotoImage(file=self.assets("entry6_6.png"))
        self.entry_bg_6 = self.canvas.create_image( 440.5, 656.0, image = self.entry_image_6)
        self.entry_6 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font= ("IBMPlexSansCond Regular", 16 * -1))
        self.entry_6.place( x=386.0, y=636.0, width=109.0, height=38.0)

        self.entry_placeholder_6 = "(Horas)"
        self.entry_6.insert(0, self.entry_placeholder_6)
        self.entry_6.bind("<FocusIn>", lambda event: self.clear_placeholder(event, self.entry_6, self.entry_placeholder_6))
        self.entry_6.bind("<FocusOut>", lambda event: self.add_placeholder(event, self.entry_6, self.entry_placeholder_6))

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

        self.image_image_4 = PhotoImage(file=self.assets("image_4.png"))
        self.image_4 = self.canvas.create_image(744.0, 812.0, image = self.image_image_4)

        self.canvas.create_text(739.0, 804.0, anchor="nw", text="C", fill="#FFFFFF", font=("Alata Regular", 14 * -1))

    def button_back(self):
        self.switch_window(WindowState.get_window(WindowState.ID_RELACAO_T))

    

    def check_scrollbar_2(self, event=None):
        
        if self.entry_2.yview()[1] < 1.0:
            self.scrollbar_2.place(x=677.0, y=356.0, height=92.0)
        else:
            self.scrollbar_2.place_forget()

    def check_scrollbar_3(self, event=None):
        
        if self.entry_3.yview()[1] < 1.0:
            self.scrollbar_3.place(x=677.0, y=493.0, height=84.0)
        else:
            self.scrollbar_3.place_forget()

    def clear_placeholder(self, event):
        if self.entry.get() == self.entry_placeholder:
            self.entry.delete(0, "end")
            self.entry.config(fg="#000000")

    def add_placeholder(self, event):
        if not self.entry.get():
            self.entry.insert(0, self.entry_placeholder)
            self.entry.config(fg="#000716")


    def register_coaching(self):
        nome = self.entry_5.get()
        descricao = self.entry_2.get("1.0", "end-1c")
        participantes = self.entry_3.get("1.0", "end-1c")
        data_inicio = self.entry_4.get()
        data_fim = self.entry_1.get()
        duracao = self.entry_6.get()
        
