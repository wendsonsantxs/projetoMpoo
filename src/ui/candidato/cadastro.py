from tkinter import Tk
from tkinter import Canvas
from tkinter import PhotoImage
from tkinter import Button
from tkinter import Entry
from tkinter import Text
from tkinter import Scrollbar

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

        self.image_image_2 = PhotoImage(file=self.assets("image2_2.png"))
        self.image_2 = self.canvas.create_image(424.0, 476.0, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=self.assets("image_3.png"))
        self.image_3 = self.canvas.create_image(220.0, 92.0, image=self.image_image_3)

        

        self.button_image_1 = PhotoImage(file=self.assets("button_2.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command = self.button_back,
            relief="flat"
        )
        self.button_1.place(x=105.0,  y=158.0, width=64.0, height=55.0)
        
        self.button_image_2 = PhotoImage(file=self.assets("button_3_2.png"))
        self.button_2 = Button(
            image = self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command = self.register_candidate,
            relief="flat"
        )
        self.button_2.place( x=333.0, y=720.0, width=240.0, height=71.0)
        self.canvas.create_text(
            398.0,
            324.0,
            anchor="nw",
            text="Vaga",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )
        
        self.entry_image_1 = PhotoImage(file=self.assets("entry_7_4.png"))
        self.entry_bg_1 = self.canvas.create_image(
          553.0,
          373.0,
          image= self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("IBMPlexSansCond Regular", 16 * -1)
        )
        self.entry_1.place(x=397.0, y=353.0, width=306.0, height=38.0)

        self.entry_placeholder_1 = "Digite o ID da Vaga"
        self.entry_1.insert(0, self.entry_placeholder_1)
        self.entry_1.bind("<FocusIn>", lambda event: self.clear_placeholder(event, self.entry_1, self.entry_placeholder_1))
        self.entry_1.bind("<FocusOut>", lambda event: self.add_placeholder(event, self.entry_1, self.entry_placeholder_1))
        
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
            427.0,
            anchor="nw",
            text="Qualidades",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 17 * -1)
        )
        
        self.entry_image_2 = PhotoImage( file=self.assets("entry_7_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            611.0,
            286.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("IBMPlexSansCond Regular", 16 * -1)
        )
        self.entry_2.place(x=510.0, y=266.0, width=202.0, height=38.0)

        self.entry_placeholder_2 = "Ex: 123.456.789-00"
        self.entry_2.insert(0, self.entry_placeholder_2)
        self.entry_2.bind("<FocusIn>", lambda event: self.clear_placeholder(event, self.entry_2, self.entry_placeholder_2))
        self.entry_2.bind("<FocusOut>", lambda event: self.add_placeholder(event, self.entry_2, self.entry_placeholder_2))
        
        self.entry_image_3 = PhotoImage(file=self.assets("entry_7_2.png"))
        self.entry_bg_3 = self.canvas.create_image(
            229.0,
            373.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=( "IBMPlexSansCond Regular", 16 * -1)
        )
        self.entry_3.place(
            x=128.0,
            y=353.0,
            width=202.0,
            height=38.0
        )
        
        self.entry_placeholder_3 = "Ex: (00) 12345-6789"
        self.entry_3.insert(0, self.entry_placeholder_3)
        self.entry_3.bind("<FocusIn>", lambda event: self.clear_placeholder(event, self.entry_3, self.entry_placeholder_3))
        self.entry_3.bind("<FocusOut>", lambda event: self.add_placeholder(event, self.entry_3, self.entry_placeholder_3))

        self.entry_image_4 = PhotoImage(file=self.assets("entry_7.png"))
        self.entry_bg_4 = self.canvas.create_image(
          420.0,
          508.0,
          image=self.entry_image_4
        )
        self.entry_4 = Text(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("IBMPlexSansCond Regular", 16 * -1)
        )
        self.entry_4.place(x=128.0, y=461.0, width=584.0, height=92.0)

        self.scrollbar_2 = Scrollbar(self.root, orient = "vertical", command=self.entry_4.yview)
        self.entry_4.configure(yscrollcommand=self.scrollbar_2.set)
        self.scrollbar_2.place_forget()

        self.entry_4.bind("<KeyRelease>", self.check_scrollbar_2)
        self.entry_4.bind("<Configure>", self.check_scrollbar_2)
        
        self.entry_image_5 = PhotoImage(file=self.assets("entry_7.png"))
        self.entry_bg_5 = self.canvas.create_image(420.0, 654.0, image = self.entry_image_5)
        self.entry_5 = Text(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("IBMPlexSansCond Regular", 16 * -1)
        )
        self.entry_5.place(x=128.0, y=611.0, width=584.0, height=84.0)

        self.scrollbar = Scrollbar(self.root, orient = "vertical", command=self.entry_5.yview)
        self.entry_5.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place_forget()

        self.entry_5.bind("<KeyRelease>", self.check_scrollbar)
        self.entry_5.bind("<Configure>", self.check_scrollbar)

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
        
        self.entry_image_6 = PhotoImage(file=self.assets("entry_7_1.png"))
        self.entry_bg_6 = self.canvas.create_image(302.0, 286.0, image=self.entry_image_6)
        self.entry_6 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=("IBMPlexSansCond Regular", 16 * -1))
        self.entry_6.place(x=128.0, y=266.0, width=348.0, height=38.0)
        
        self.canvas.create_text(171.0, 166.0, anchor="nw", text="Cadastro de Candidatos", fill="#FFFFFF", font=("IBMPlexSansCond Regular", 36 * -1) )
        
        self.image_image_3 = PhotoImage(file=self.assets("image_3.png"))
        self.image_3 = self.canvas.create_image(287.0, 65.0, image=self.image_image_3)
        
        self.canvas.create_text( 367.0, 34.0, anchor = "nw", text = "Sistema De Gerenciamento De \nRecursos Humanos (Hrms)", fill="#FFFFFF", font=("Itim Regular", 26 * -1))
        
        self.canvas.create_text( 753.0, 799.0, anchor="nw", text="W.Y.W",  fill="#FFFFFF", font=("Alef Regular", 18 * -1))
        
        self.image_image_4 = PhotoImage(file=self.assets("image_4.png"))
        self.image_4 = self.canvas.create_image(744.0, 812.0, image=self.image_image_4)
        
        self.canvas.create_text(739.0, 806.0, anchor="nw", text="C", fill="#FFFFFF", font=("Alata Regular", 14 * -1))

    
    def button_back(self):
        self.switch_window(swap_to=WindowState.get_window(WindowState.ID_RELACAO_C))

    def check_scrollbar(self, event=None):
        
        if self.entry_5.yview()[1] < 1.0:
            self.scrollbar.place(x=702.0, y=611.0, height=84.0)
        else:
            self.scrollbar.place_forget()

    def check_scrollbar_2(self, event=None):
        
        if self.entry_4.yview()[1] < 1.0:
            self.scrollbar_2.place(x=702.0, y=611.0, height=84.0)
        else:
            self.scrollbar_2.place_forget()

    def clear_placeholder(self, event, entry, placeholder):
        
            if entry.get() == placeholder:
                entry.delete(0, "end")
                entry.config(fg="#f2f4f7")

    def add_placeholder(self, event, entry, placeholder):
        
            if not entry.get():
                entry.insert(0, placeholder)
                entry.config(fg="#FFFFFF")


    def register_candidate(self):
        if self.entry_1.get() and self.entry_2.get() and self.entry_3.get() and self.entry_4.get() and self.entry_5.get():
            nome = self.entry_6.get()
            cpf = self.entry_2.get()
            telefone = self.entry_3.get()
            qualidades = self.entry_4.get("1.0", "end-1c")
            observacoes = self.entry_5.get("1.0", "end-1c")
            vaga = self.entry_1.get()