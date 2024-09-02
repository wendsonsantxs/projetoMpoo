from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / 'assets'


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("980x825")
window.configure(bg = "#FFFFFF")
image = PhotoImage(file=relative_to_assets("logo.png")) 
window.call('wm', 'iconphoto', window._w, image)
window.title('App HRMS')


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 825,
    width = 980,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image4_1.png"))
image_1 = canvas.create_image(
    490.0,
    412.0,
    image=image_image_1
)

image_image_2 = PhotoImage(file=relative_to_assets("image4_2.png"))
image_2 = canvas.create_image(
    487.0,
    460.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=93.0,
    y=154.0,
    width=64.0,
    height=55.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_3_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=390.0,
    y=710.0,
    width=235.0,
    height=71.0
)

canvas.create_text(
    484.0,
    229.0,
    anchor="nw",
    text="CPF",
    fill="#F3F3F3",
    font=("IBMPlexSansCond Regular", 16 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry4_2.png"))
entry_bg_1 = canvas.create_image(
    581.0,
    272.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=490.0,
    y=255.0,
    width=182.0,
    height=33.0
)

canvas.create_text(
    484.0,
    314.0,
    anchor="nw",
    text="Telefone",
    fill="#F3F3F3",
    font=("IBMPlexSansCond Regular", 16 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry4_2.png"))
entry_bg_2 = canvas.create_image(
    581.0,
    358.5,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=490.0,
    y=341.0,
    width=182.0,
    height=33.0
)

canvas.create_text(
    648.0,
    440.0,
    anchor="nw",
    text="CEP",
    fill="#F3F3F3",
    font=("IBMPlexSansCond Regular", 16 * -1)
)

entry_image_3 = PhotoImage(file=relative_to_assets("entry4_2.png"))
entry_bg_3 = canvas.create_image(
    745.0,
    484.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=654.0,
    y=467.0,
    width=182.0,
    height=33.0
)

canvas.create_text(
    106.0,
    532.0,
    anchor="nw",
    text="Bairro",
    fill="#F3F3F3",
    font=("IBMPlexSansCond Regular", 16 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry4_3.png"))
entry_bg_4 = canvas.create_image(
    213.0,
    576.5,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=110.0,
    y=559.0,
    width=206.0,
    height=33.0
)

canvas.create_text(
    106.0,
    623.0,
    anchor="nw",
    text="Cargo",
    fill="#F3F3F3",
    font=("IBMPlexSansCond Regular", 16 * -1)
)

canvas.create_text(
    762.0,
    623.0,
    anchor="nw",
    text="Contratação",
    fill="#F3F3F3",
    font=("IBMPlexSansCond Regular", 16 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry4_3.png"))
entry_bg_5 = canvas.create_image(
    213.0,
    667.5,
    image=entry_image_5
)
entry_5 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=110.0,
    y=650.0,
    width=206.0,
    height=33.0
)

canvas.create_text(
    361.0,
    623.0,
    anchor="nw",
    text="Departamento",
    fill="#F3F3F3",
    font=("IBMPlexSansCond Regular", 16 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry4_3.png"))
entry_bg_6 = canvas.create_image(
    464.0,
    667.5,
    image=entry_image_6
)
entry_6 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=361.0,
    y=650.0,
    width=206.0,
    height=33.0
)

canvas.create_text(
    609.0,
    623.0,
    anchor="nw",
    text="Salário",
    fill="#F3F3F3",
    font=("IBMPlexSansCond Regular", 16 * -1)
)

entry_image_7 = PhotoImage(file=relative_to_assets("entry4_5.png"))
entry_bg_7 = canvas.create_image(
    671.0,
    667.5,
    image=entry_image_7
)
entry_7 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=614.0,
    y=650.0,
    width=114.0,
    height=33.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry4_4.png"))
entry_bg_8 = canvas.create_image(
    819.0,
    667.5,
    image=entry_image_8
)
entry_8 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=766.0,
    y=650.0,
    width=106.0,
    height=33.0
)

canvas.create_text(
    361.0,
    532.0,
    anchor="nw",
    text="Cidade",
    fill="#F3F3F3",
    font=("IBMPlexSansCond Regular", 16 * -1)
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry4_6.png"))
entry_bg_9 = canvas.create_image(
    472.0,
    576.5,
    image=entry_image_9
)
entry_9 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=369.0,
    y=559.0,
    width=206.0,
    height=33.0
)

canvas.create_text(
    486.0,
    441.0,
    anchor="nw",
    text="Número",
    fill="#F3F3F3",
    font=("IBMPlexSansCond Regular", 16 * -1)
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry4_7.png"))
entry_bg_10 = canvas.create_image(
    539.5,
    485.5,
    image=entry_image_10
)
entry_10 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=490.0,
    y=468.0,
    width=99.0,
    height=33.0
)

canvas.create_text(
    718.0,
    230.0,
    anchor="nw",
    text="Data de Nascimento",
    fill="#F3F3F3",
    font=("IBMPlexSansCond Regular", 16 * -1)
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry4_8.png"))
entry_bg_11 = canvas.create_image(
    797.5,
    272.5,
    image=entry_image_11
)
entry_11 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_11.place(
    x=724.0,
    y=255.0,
    width=147.0,
    height=33.0
)

canvas.create_text(
    104.0,
    229.0,
    anchor="nw",
    text="Nome",
    fill="#F3F3F3",
    font=("IBMPlexSansCond Regular", 16 * -1)
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry4_1.png"))
entry_bg_12 = canvas.create_image(
    279.0,
    272.5,
    image=entry_image_12
)
entry_12 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_12.place(
    x=111.0,
    y=255.0,
    width=336.0,
    height=33.0
)

canvas.create_text(
    105.0,
    316.0,
    anchor="nw",
    text="E-mail",
    fill="#F3F3F3",
    font=("IBMPlexSansCond Regular", 16 * -1)
)

entry_image_13 = PhotoImage(
    file=relative_to_assets("entry4_1.png"))
entry_bg_13 = canvas.create_image(
    278.0,
    358.5,
    image=entry_image_13
)
entry_13 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_13.place(
    x=110.0,
    y=341.0,
    width=336.0,
    height=33.0
)

canvas.create_text(
    103.0,
    441.0,
    anchor="nw",
    text="Endereço",
    fill="#F3F3F3",
    font=("IBMPlexSansCond Regular", 16 * -1)
)

entry_image_14 = PhotoImage(
    file=relative_to_assets("entry4_1.png"))
entry_bg_14 = canvas.create_image(
    278.0,
    484.5,
    image=entry_image_14
)
entry_14 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_14.place(
    x=110.0,
    y=467.0,
    width=336.0,
    height=33.0
)

canvas.create_rectangle(
    102.0,
    418.0609715450555,
    452.9946177005768,
    421.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    539.0,
    418.12191243935376,
    878.9947868585587,
    421.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    898.0,
    793.0,
    anchor="nw",
    text="W.Y.W",
    fill="#FFFFFF",
    font=("Alef Regular", 18 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_3 = canvas.create_image(
    889.0,
    806.0,
    image=image_image_3
)

canvas.create_text(
    883.0,
    798.0,
    anchor="nw",
    text="C",
    fill="#FFFFFF",
    font=("Alata Regular", 14 * -1)
)

canvas.create_text(
    168.0,
    160.0,
    anchor="nw",
    text="Cadastro Funcionário",
    fill="#FFFFFF",
    font=("IBMPlexSansCond Regular", 36 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_4 = canvas.create_image(
    364.0,
    62.00000000000001,
    image=image_image_4
)

canvas.create_text(
    442.0,
    34.00000000000001,
    anchor="nw",
    text="Sistema De Gerenciamento De \nRecursos Humanos (Hrms)",
    fill="#FFFFFF",
    font=("Itim Regular", 22 * -1)
)
window.resizable(False, False)
window.mainloop()
