
from pathlib import Path
from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / 'assets'


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("825x825")
window.configure(bg = "#FFFFFF")
image = PhotoImage(file=relative_to_assets("logo.png")) 
window.call('wm', 'iconphoto', window._w, image)
window.title('App HRMS')


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 825,
    width = 825,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    412.0,
    412.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image2_2.png"))
image_2 = canvas.create_image(
    415.0,
    461.0,
    image=image_image_2
)

button_image_1 = PhotoImage(file = relative_to_assets("button_2.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=100.0,
    y=158.0,
    width=64.0,
    height=55.0
)

button_image_2 = PhotoImage(file=relative_to_assets("button_3.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=357.0,
    y=716.0,
    width=160.0,
    height=60.0
)

canvas.create_text(
    546.0,
    605.0,
    anchor="nw",
    text="Data de Término",
    fill="#F3F3F3",
    font=("IBMPlexSansCond Regular", 16 * -1)
)

entry_image_1 = PhotoImage(file=relative_to_assets("entry6_4.png"))
entry_bg_1 = canvas.create_image(
    617.5,
    656.0,
    image=entry_image_1
)
entry_1 = Label(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=548.0,
    y=636.0,
    width=139.0,
    height=38.0
)

canvas.create_text(
    196.0,
    322.0,
    anchor="nw",
    text="Descrição",
    fill="#F3F3F3",
    font=("IBMPlexSansCond Regular", 16 * -1)
)

canvas.create_text(
    196.0,
    462.0,
    anchor="nw",
    text="Participantes",
    fill="#F3F3F3",
    font=("IBMPlexSansCond Regular", 16 * -1)
)

entry_image_2 = PhotoImage(file=relative_to_assets("entry6_2.png"))
entry_bg_2 = canvas.create_image(
    440.5,
    403.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=194.0,
    y=356.0,
    width=493.0,
    height=92.0
)

entry_image_3 = PhotoImage(file=relative_to_assets("entry6_2.png"))
entry_bg_3 = canvas.create_image(
    440.5,
    542.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=194.0,
    y=495.0,
    width=493.0,
    height=92.0
)

canvas.create_text(
    194.0,
    605.0,
    anchor="nw",
    text="Data de Inicio",
    fill="#F3F3F3",
    font=("IBMPlexSansCond Regular", 16 * -1)
)

entry_image_4 = PhotoImage(file=relative_to_assets("entry6_4.png"))
entry_bg_4 = canvas.create_image(
    263.5,
    655.0,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=194.0,
    y=635.0,
    width=139.0,
    height=38.0
)

canvas.create_text(
    196.0,
    240.0,
    anchor="nw",
    text="Título",
    fill="#F3F3F3",
    font=("IBMPlexSansCond Regular", 16 * -1)
)

entry_image_5 = PhotoImage(file=relative_to_assets("entry6_5.png"))
entry_bg_5 = canvas.create_image(
    440.5,
    290.0,
    image=entry_image_5
)
entry_5 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=194.0,
    y=270.0,
    width=493.0,
    height=38.0
)

canvas.create_text(
    381.0,
    605.0,
    anchor="nw",
    text="Duração (Horas)",
    fill="#F3F3F3",
    font=("IBMPlexSansCond Regular", 16 * -1)
)

entry_image_6 = PhotoImage(file=relative_to_assets("entry6_6.png"))
entry_bg_6 = canvas.create_image(
    440.5,
    656.0,
    image=entry_image_6
)
entry_6 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=386.0,
    y=636.0,
    width=109.0,
    height=38.0
)

canvas.create_text(
    169.0,
    166.0,
    anchor="nw",
    text="Cadastro de Treinamentos",
    fill="#FFFFFF",
    font=("IBMPlexSansCond Regular", 36 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    287.0,
    65.0,
    image=image_image_3
)

canvas.create_text(
    367.0,
    33.99999999999999,
    anchor="nw",
    text="Sistema De Gerenciamento De \nRecursos Humanos (Hrms)",
    fill="#FFFFFF",
    font=("Itim Regular", 22 * -1)
)

canvas.create_text(
    753.0,
    799.0,
    anchor="nw",
    text="W.Y.W",
    fill="#FFFFFF",
    font=("Alef Regular", 18 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    744.0,
    812.0,
    image=image_image_4
)

canvas.create_text(
    739.0,
    804.0,
    anchor="nw",
    text="C",
    fill="#FFFFFF",
    font=("Alata Regular", 14 * -1)
)
window.resizable(False, False)
window.mainloop()
