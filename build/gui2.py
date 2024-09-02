from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets"
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
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    424.0,
    476.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    222.0,
    92.0,
    image=image_image_3
)

canvas.create_text(
    299.0,
    56.99999999999999,
    anchor="nw",
    text="Sistema De Gerenciamento De\nRecursos Humanos (Hrms)",
    fill="#FFFFFF",
    font=("Itim Regular", 30 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=494.0,
    y=307.0,
    width=172.0,
    height=60.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=494.0,
    y=464.0,
    width=172.0,
    height=60.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=494.0,
    y=618.0,
    width=172.0,
    height=60.0
)

canvas.create_text(
    217.0,
    311.0,
    anchor="nw",
    text="Cadastrar Vagas",
    fill="#FFFFFF",
    font=("Itim Regular", 30 * -1)
)

canvas.create_text(
    234.0,
    474.0,
    anchor="nw",
    text="Vagas Ativas",
    fill="#FFFFFF",
    font=("Itim Regular", 30 * -1)
)

canvas.create_text(
    201.0,
    629.0,
    anchor="nw",
    text="Banco De Talentos",
    fill="#FFFFFF",
    font=("Itim Regular", 30 * -1)
)

canvas.create_text(
    742.0,
    787.0,
    anchor="nw",
    text="W.Y.W",
    fill="#FFFFFF",
    font=("Alef Regular", 18 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    730.0,
    800.0,
    image=image_image_4
)

canvas.create_text(
    724.0,
    791.0,
    anchor="nw",
    text="C",
    fill="#FFFFFF",
    font=("Alata Regular", 14 * -1)
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=169.0,
    y=201.0,
    width=64.0,
    height=55.0
)
window.resizable(False, False)
window.mainloop()
