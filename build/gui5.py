from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


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

image_image_2 = PhotoImage(file=relative_to_assets("image2_2.png"))
image_2 = canvas.create_image(
    415.0,
    461.0,
    image=image_image_2
)

button_image_1 = PhotoImage(file=relative_to_assets("button_2.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=107.0,
    y=155.0,
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
    x=333.0,
    y=704.0,
    width=161.0,
    height=60.0
)

canvas.create_text(
    189.0,
    332.0,
    anchor="nw",
    text="Requisitos",
    fill="#F3F3F3",
    font=("IBMPlexSansCond Regular", 16 * -1)
)

entry_image_1 = PhotoImage(file=relative_to_assets("entry5_1.png"))
entry_bg_1 = canvas.create_image(
    408.5,
    398.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=194.0,
    y=362.0,
    width=429.0,
    height=70.0
)

canvas.create_text(
    189.0,
    458.0,
    anchor="nw",
    text="Descrição",
    fill="#F3F3F3",
    font=("IBMPlexSansCond Regular", 16 * -1)
)

entry_image_2 = PhotoImage(file=relative_to_assets("entry5_6.png"))
entry_bg_2 = canvas.create_image(
    408.5,
    535.0,
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
    y=488.0,
    width=429.0,
    height=92.0
)

canvas.create_text(
    189.0,
    599.0,
    anchor="nw",
    text="Data de Publicação",
    fill="#F3F3F3",
    font=("IBMPlexSansCond Regular", 16 * -1)
)

entry_image_3 = PhotoImage(file=relative_to_assets("entry5_3.png"))
entry_bg_3 = canvas.create_image(
    297.0,
    655.0,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=194.0,
    y=635.0,
    width=206.0,
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

entry_image_4 = PhotoImage(file=relative_to_assets("entry5_4.png"))
entry_bg_4 = canvas.create_image(
    408.5,
    290.0,
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
    y=270.0,
    width=429.0,
    height=38.0
)

canvas.create_text(
    444.0,
    599.0,
    anchor="nw",
    text="Duração até a seleção",
    fill="#F3F3F3",
    font=("IBMPlexSansCond Regular", 16 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry5_2.png"))
entry_bg_5 = canvas.create_image(
    537.5,
    655.0,
    image=entry_image_5
)
entry_5 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=452.0,
    y=635.0,
    width=171.0,
    height=38.0
)

canvas.create_text(
    185.0,
    167.0,
    anchor="nw",
    text="Cadastro de Vagas",
    fill="#FFFFFF",
    font=("IBMPlexSansCond Regular", 36 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    282.0,
    65.0,
    image=image_image_3
)

canvas.create_text(
    362.0,
    32.99999999999999,
    anchor="nw",
    text="Sistema De Gerenciamento De \nRecursos Humanos (Hrms)",
    fill="#FFFFFF",
    font=("Itim Regular", 22 * -1)
)

canvas.create_text(
    751.0,
    795.0,
    anchor="nw",
    text="W.Y.W",
    fill="#FFFFFF",
    font=("Alef Regular", 18 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    742.0,
    808.0,
    image=image_image_4
)

canvas.create_text(
    737.0,
    800.0,
    anchor="nw",
    text="C",
    fill="#FFFFFF",
    font=("Alata Regular", 14 * -1)
)
window.resizable(False, False)
window.mainloop()
