from tkinter import Button
from tkinter import Canvas
from tkinter import Entry
from tkinter import PhotoImage
from tkinter import Tk

from ui.window import Window
from ui.window_state import WindowState
from model.funcionario import Funcionario

class CadastroF(Window):
    def __init__(self, root: Tk, width: int = 980, height: int = 825):
        super().__init__(root, width, height)
        self.mensage_get = None

    def create(self):
        super().create()
        self.canvas = Canvas(self.root, bg="#FFFFFF", height=self.height,
                             width=self.width, bd=0, highlightthickness=0, relief="ridge")

        self.canvas.place(x=0, y=0)

        self.bg = PhotoImage(file=self.assets("image4_1.png"))
        self.image_1 = self.canvas.create_image(490.0, 412.0, image=self.bg)

        self.rectangle = PhotoImage(file=self.assets("image4_2.png"))
        self.image_2 = self.canvas.create_image(
            487.0, 460.0, image=self.rectangle)

        self.logo = PhotoImage(file=self.assets("image_3.png"))
        self.image_3 = self.canvas.create_image(195.0, 70.0, image=self.logo)

        self.canvas.create_text(
            280.0,
            35,
            anchor="nw",
            text="Sistema De Gerenciamento De\nRecursos Humanos (Hrms)",
            fill="#FFFFFF",
            font=("Itim Regular", 30 * -1)
        )

        self.button_image_1 = PhotoImage(file=self.assets("button_2.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_back,
            relief="flat"
        )
        self.button_1.place(x=93.0, y=154.0, width=64.0, height=55.0)

        self.button_image_2 = PhotoImage(file=self.assets("button_3_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.register_employee,
            relief="flat"
        )
        self.button_2.place(x=374.0, y=710.0, width=235.0, height=71.0)

        self.canvas.create_text(
            484.0,
            229.0,
            anchor="nw",
            text="CPF",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_1 = PhotoImage(file=self.assets("entry4_2.png"))
        self.entry_bg_1 = self.canvas.create_image(
            581.0, 272.5, image=self.entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=(
            "IBMPlexSansCond Regular", 16 * -1))
        self.entry_1.place(
            x=490.0,
            y=255.0,
            width=182.0,
            height=33.0)

        self.canvas.create_text(
            484.0,
            314.0,
            anchor="nw",
            text="Telefone",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_2 = PhotoImage(file=self.assets("entry4_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            581.0, 358.5,  image=self.entry_image_2)
        self.entry_2 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=(
            "IBMPlexSansCond Regular", 16 * -1))
        self.entry_2.place(x=490.0, y=341.0, width=182.0, height=33.0)

        self.canvas.create_text(
            648.0,
            440.0,
            anchor="nw",
            text="CEP",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_3 = PhotoImage(file=self.assets("entry4_2.png"))
        self.entry_bg_3 = self.canvas.create_image(
            745.0, 484.5, image=self.entry_image_3)
        self.entry_3 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=(
            "IBMPlexSansCond Regular", 16 * -1))
        self.entry_3.place(x=654.0, y=467.0,  width=182.0, height=33.0)

        self.canvas.create_text(
            106.0,
            532.0,
            anchor="nw",
            text="Bairro",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_4 = PhotoImage(file=self.assets("entry4_3.png"))
        self.entry_bg_4 = self.canvas.create_image(
            213.0, 576.5, image=self.entry_image_4)
        self.entry_4 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=(
            "IBMPlexSansCond Regular", 16 * -1))
        self.entry_4.place(x=110.0, y=559.0, width=206.0, height=33.0)

        self.canvas.create_text(
            106.0,
            623.0,
            anchor="nw",
            text="Cargo",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.canvas.create_text(
            762.0,
            623.0,
            anchor="nw",
            text="Contratação",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_5 = PhotoImage(
            file=self.assets("entry4_3.png"))  # cargo
        self.entry_bg_5 = self.canvas.create_image(
            213.0, 667.5, image=self.entry_image_5)
        self.entry_5 = Entry(bd=0, bg="#FFFFFF", fg="#000716",  font=(
            "IBMPlexSansCond Regular", 16 * -1), highlightthickness=0)
        self.entry_5.place(x=110.0, y=650.0, width=206.0, height=33.0)

        self.canvas.create_text(
            361.0,
            623.0,
            anchor="nw",
            text="Departamento",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_6 = PhotoImage(
            file=self.assets("entry4_3.png"))  # departamento
        self.entry_bg_6 = self.canvas.create_image(
            464.0,  667.5, image=self.entry_image_6)
        self.entry_6 = Entry(bd=0,  bg="#FFFFFF", fg="#000716", highlightthickness=0, font=(
            "IBMPlexSansCond Regular", 16 * -1))
        self.entry_6.place(x=361.0, y=650.0, width=206.0, height=33.0)

        self.canvas.create_text(
            609.0,
            623.0,
            anchor="nw",
            text="Salário",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_7 = PhotoImage(file=self.assets("entry4_5.png"))
        self.entry_bg_7 = self.canvas.create_image(
            671.0, 667.5, image=self.entry_image_7)
        self.entry_7 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=(
            "IBMPlexSansCond Regular", 16 * -1))  # salario
        self.entry_7.place(x=614.0, y=650.0, width=114.0, height=33.0)

        self.entry_image_8 = PhotoImage(file=self.assets("entry4_4.png"))
        self.entry_bg_8 = self.canvas.create_image(
            819.0, 667.5, image=self.entry_image_8)  # contratação
        self.entry_8 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=(
            "IBMPlexSansCond Regular", 16 * -1))
        self.entry_8.place(x=766.0, y=650.0, width=106.0, height=33.0)

        self.canvas.create_text(
            361.0,
            532.0,
            anchor="nw",
            text="Cidade",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_9 = PhotoImage(file=self.assets("entry4_6.png"))
        self.entry_bg_9 = self.canvas.create_image(
            472.0, 576.5, image=self.entry_image_9)
        self.entry_9 = Entry(bd=0, bg="#FFFFFF",  fg="#000716", highlightthickness=0, font=(
            "IBMPlexSansCond Regular", 16 * -1))
        self.entry_9.place(x=369.0, y=559.0, width=206.0, height=33.0)

        self.canvas.create_text(
            486.0,
            441.0,
            anchor="nw",
            text="Número",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_10 = PhotoImage(file=self.assets("entry4_7.png"))
        self.entry_bg_10 = self.canvas.create_image(
            539.5, 485.5, image=self.entry_image_10)
        self.entry_10 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=(
            "IBMPlexSansCond Regular", 16 * -1))
        self.entry_10.place(x=490.0, y=468.0, width=99.0, height=33.0)

        self.canvas.create_text(
            718.0,
            230.0,
            anchor="nw",
            text="Data de Nascimento",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_11 = PhotoImage(file=self.assets("entry4_8.png"))
        self.entry_bg_11 = self.canvas.create_image(
            797.5, 272.5, image=self.entry_image_11)
        self.entry_11 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=(
            "IBMPlexSansCond Regular", 16 * -1))
        self.entry_11.place(x=724.0, y=255.0, width=147.0, height=33.0)

        self.canvas.create_text(
            104.0,
            229.0,
            anchor="nw",
            text="Nome",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_12 = PhotoImage(file=self.assets("entry4_1.png"))
        self.entry_bg_12 = self.canvas.create_image(
            279.0, 272.5, image=self.entry_image_12)
        self.entry_12 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=(
            "IBMPlexSansCond Regular", 16 * -1))
        self.entry_12.place(x=111.0, y=255.0, width=336.0, height=33.0)

        self.canvas.create_text(
            105.0,
            316.0,
            anchor="nw",
            text="E-mail",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_13 = PhotoImage(file=self.assets("entry4_1.png"))
        self.entry_bg_13 = self.canvas.create_image(
            278.0, 358.5, image=self.entry_image_13)
        self.entry_13 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=(
            "IBMPlexSansCond Regular", 16 * -1))
        self.entry_13.place(x=110.0, y=341.0, width=336.0, height=33.0)

        self.canvas.create_text(
            103.0,
            441.0,
            anchor="nw",
            text="Endereço",
            fill="#F3F3F3",
            font=("IBMPlexSansCond Regular", 16 * -1)
        )

        self.entry_image_14 = PhotoImage(file=self.assets("entry4_1.png"))
        self.entry_bg_14 = self.canvas.create_image(
            278.0,  484.5, image=self.entry_image_14)
        self.entry_14 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=(
            "IBMPlexSansCond Regular", 16 * -1))
        self.entry_14.place(x=110.0, y=467.0, width=336.0, height=33.0)

        self.canvas.create_rectangle(
            102.0,
            418.0609715450555,
            452.9946177005768,
            421.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_rectangle(
            539.0,
            418.12191243935376,
            878.9947868585587,
            421.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_text(
            899.0,
            795.0,
            anchor="nw",
            text="W.Y.W",
            fill="#FFFFFF",
            font=("Alef Regular", 18 * -1)
        )

        self.image_image_3 = PhotoImage(file=self.assets("image_4.png"))
        self.image_3 = self.canvas.create_image(
            889.0,
            806.0,
            image=self.image_image_3
        )

        self.canvas.create_text(
            884.0,
            798.0,
            anchor="nw",
            text="C",
            fill="#FFFFFF",
            font=("Alata Regular", 14 * -1)
        )

        self.canvas.create_text(
            168.0,
            160.0,
            anchor="nw",
            text="Cadastro Funcionário",
            fill="#FFFFFF",
            font=("IBMPlexSansCond Regular", 36 * -1)
        )

    def button_back(self):
        self.switch_window(WindowState.get_window(WindowState.ID_RELACAO_F))

    def register_employee(self):
        
        if self.entry_12.get() and self.entry_13.get() and self.entry_1.get() and self.entry_2.get() and self.entry_14.get() and self.entry_10.get() and self.entry_4.get() and self.entry_9.get() and self.entry_3.get() and self.entry_5.get() and self.entry_6.get() and self.entry_7.get() and self.entry_8.get() and self.entry_11.get():

            nome = self.entry_12.get() 
            email = self.entry_13.get()
            cpf = self.entry_1.get()
            telefone = self.entry_2.get()
            endereco = self.entry_14.get()
            numero = self.entry_10.get()
            bairro = self.entry_4.get()
            cidade = self.entry_9.get()
            cep = self.entry_3.get()
            cargo = self.entry_5.get()
            departamento = self.entry_6.get()
            salario = self.entry_7.get()
            contratacao = self.entry_8.get()
            data_nascimento = self.entry_11.get()

            try:
                funcionario = Funcionario(nome, email, cpf, telefone, endereco, numero, bairro, 
                                            cidade, cep, cargo, departamento, salario, contratacao, data_nascimento)
                funcionario.adicionar_funcionario()

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
                    600.0, 
                    174.0,  
                    anchor="nw", 
                    text="* Cadastro realizado com sucesso", 
                    fill="#008c00",
                    font=("Itim Regular", 18 * -1)
                    )
        else:
            if not self.mensage_get:
                self.mensage_get = self.canvas.create_text(
                        600.0, 
                        176.0,  
                        anchor="nw", 
                        text="Preencha todos os campos (*)", 
                        fill="#FF0000",
                        font=("Itim regular", 18 * -1)
                        )