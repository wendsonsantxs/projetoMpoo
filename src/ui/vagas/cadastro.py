from tkinter import Button
from tkinter import Canvas
from tkinter import PhotoImage
from tkinter import Entry
from tkinter import Tk
from tkinter import Text
from tkinter import Scrollbar

from ui.window import Window
from ui.window_state import WindowState
from model.Vaga import Vaga

class CadastroV(Window):
    def __init__(self, root = Tk):
        super().__init__(root)
        self.mensage_get = None
    
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

        self.button_image_1 = PhotoImage(file=self.assets("button_2.png"))
        self.button_1 = Button(
            image = self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command = self.button_back,
            relief="flat"
        )
        self.button_1.place(x=107.0, y=155.0, width=64.0, height=55.0)

        self.button_image_2 = PhotoImage(file=self.assets("button_3.png"))
        self.button_2 = Button(
            image = self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command = self.register_vacancy,
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

        self.entry_image_1 = PhotoImage(file=self.assets("entry5_1.png"))
        self.entry_bg_1 = self.canvas.create_image(    408.5, 398.0, image = self.entry_image_1)
        self.entry_1 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font= ("IBMPlexSansCond Regular", 17 * -1))
        self.entry_1.place(x=194.0, y=361.9, width=429.0, height=68.3)

        self.scrollbar_1 = Scrollbar(self.root, orient = "vertical", command=self.entry_1.yview)
        self.entry_1.configure(yscrollcommand=self.scrollbar_1.set)
        self.scrollbar_1.place_forget()

        self.entry_1.bind("<KeyRelease>", self.check_scrollbar_1)
        self.entry_1.bind("<Configure>", self.check_scrollbar_1)

        self.canvas.create_text(
            189.0,
            458.0,
            anchor="nw",
            text="Descrição",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_2 = PhotoImage(file = self.assets("entry5_6.png"))
        self.entry_bg_2 = self.canvas.create_image(408.5, 535.0, image = self.entry_image_2)
        self.entry_2 = Text(bd = 0, bg = "#FFFFFF", fg = "#000716", highlightthickness = 0, font= ("IBMPlexSansCond Regular", 17 * -1))
        self.entry_2.place(x=194.0, y=488.5, width=429.0, height=90.5)

        self.scrollbar_2 = Scrollbar(self.root, orient = "vertical", command=self.entry_2.yview)
        self.entry_2.configure(yscrollcommand=self.scrollbar_2.set)
        self.scrollbar_2.place_forget()

        self.entry_2.bind("<KeyRelease>", self.check_scrollbar_2)
        self.entry_2.bind("<Configure>", self.check_scrollbar_2)

        self.canvas.create_text(
            189.0,
            599.0,
            anchor="nw",
            text="Data de Publicação",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_3 = PhotoImage(file=self.assets("entry5_3.png"))
        self.entry_bg_3 = self.canvas.create_image(297.0, 655.0, image = self.entry_image_3)
        self.entry_3 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font= ("IBMPlexSansCond Regular", 16 * -1))
        self.entry_3.place(x=194.0, y=635.0, width=206.0, height=38.0)

        self.entry_placeholder_3 = "DD/MM/AAAA"
        self.entry_3.insert(0, self.entry_placeholder_3)
        self.entry_3.bind("<FocusIn>", lambda event: self.clear_placeholder(event, self.entry_3, self.entry_placeholder_3))
        self.entry_3.bind("<FocusOut>", lambda event: self.add_placeholder(event, self.entry_3, self.entry_placeholder_3))

        self.canvas.create_text(
            196.0,
            240.0,
            anchor="nw",
            text="Título",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_4 = PhotoImage(file=self.assets("entry5_4.png"))
        self.entry_bg_4 = self.canvas.create_image(408.5, 290.0, image = self.entry_image_4)
        self.entry_4 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font= ("IBMPlexSansCond Regular", 16 * -1))
        self.entry_4.place(x=194.0, y=270.0, width=429.0, height=38.0)

        self.canvas.create_text(
            444.0,
            599.0,
            anchor="nw",
            text="Data da seleção",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_5 = PhotoImage(file=self.assets("entry5_2.png"))
        self.entry_bg_5 = self.canvas.create_image(537.5, 655.0, image = self.entry_image_5)
        self.entry_5 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font= ("IBMPlexSansCond Regular", 16 * -1))
        self.entry_5.place(x=452.0, y=635.0, width=171.0, height=38.0)

        self.entry_placeholder_5 = "DD/MM/AAAA"
        self.entry_5.insert(0, self.entry_placeholder_5)
        self.entry_5.bind("<FocusIn>", lambda event: self.clear_placeholder(event, self.entry_5, self.entry_placeholder_5))
        self.entry_5.bind("<FocusOut>", lambda event: self.add_placeholder(event, self.entry_5, self.entry_placeholder_5))

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

        self.image_image_4 = PhotoImage(file = self.assets("image_4.png"))
        self.image_4 = self.canvas.create_image( 742.0, 808.0, image = self.image_image_4)

        self.canvas.create_text(
            737.0,
            800.0,
            anchor="nw",
            text="C",
            fill="#FFFFFF",
            font=("Alata Regular", 14 * -1)
        )
    
    def button_back(self):
        self.switch_window(swap_to=WindowState.get_window(WindowState.ID_RELACAO_V))

    def check_scrollbar_1(self, event=None):
        
        if self.entry_1.yview()[1] < 1.0:
            self.scrollbar_1.place(x=613.0, y=362.0, height=70.0)
        else:
            self.scrollbar_1.place_forget()

    def check_scrollbar_2(self, event=None):
        
        if self.entry_2.yview()[1] < 1.0:
            self.scrollbar_2.place(x=613.0, y=488.0, height=92.0)
        else:
            self.scrollbar_2.place_forget()

    def clear_placeholder(self, event, entry, placeholder):
        
            if entry.get() == placeholder:
                entry.delete(0, "end")
                entry.config(fg="#000000")

    def add_placeholder(self, event, entry, placeholder):
        
            if not entry.get():
                entry.insert(0, placeholder)
                entry.config(fg="#f2f4f7")

    def register_vacancy(self):

        if self.entry_1.get('1.0', 'end-1c') and self.entry_2.get('1.0', 'end-1c') and self.entry_3.get() and self.entry_4.get() and self.entry_5.get():

            titulo = self.entry_4.get()
            requisitos = self.entry_1.get('1.0', 'end-1c')
            descricao = self.entry_2.get('1.0', 'end-1c')
            data_publicacao = self.entry_3.get()
            data_selecao = self.entry_5.get()

            try:
                vaga = Vaga()
                vaga.get_dados(titulo, descricao, requisitos, data_publicacao, data_selecao)
                vaga.adicionar_vaga()

            except ValueError as e:
                if self.mensage_get:
                    self.canvas.delete(self.mensage_get)
                self.mensage_get = self.canvas.create_text(
                    600.0, 
                    174.0,  
                    anchor="nw", 
                    text=f"* {e}", 
                    fill="#FF0000",
                    font=("Itim Regular", 18 * -1)
                    )
                return

            if self.mensage_get:
                self.canvas.delete(self.mensage_get)
            self.mensage_get = self.canvas.create_text(
                    560.0, 
                    174.0,  
                    anchor="nw", 
                    text="*Sucesso ao cadastrar", 
                    fill="#008c00",
                    font=("Itim Regular", 16 * -1)
                    )

        else:
            if not self.mensage_get:
                self.mensage_get = self.canvas.create_text(
                        560.0, 
                        176.0,  
                        anchor="nw", 
                        text="Preencha todos os campos (*)", 
                        fill="#FF0000",
                        font=("Itim regular", 16 * -1)
                        )