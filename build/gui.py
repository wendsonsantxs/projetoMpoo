from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, Scrollbar, INSERT, END, VERTICAL, HORIZONTAL, RIGHT, Y, X, LEFT, BOTH


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" 


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
image = PhotoImage(file=relative_to_assets("logo.png")) 
window.call('wm', 'iconphoto', window._w, image)
window.title('App HRMS')
window.geometry("825x825")
#window.configure(bg = "#FFFFFF")


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
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    412.0,
    412.0,
    image=image_image_1
)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    407.0,
    461.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    195.0,
    76.0,
    image=image_image_3
)

canvas.create_text(
    271.0,
    40,
    anchor="nw",
    text="Sistema De Gerenciamento De\nRecursos Humanos(HRMS)",
    fill="#FFFFFF",
    font=("Itim", 30 * -1)
)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=500.0,
    y=289.0,
    width=170.0,
    height=60.0
)

button_image_2 = PhotoImage(file=relative_to_assets("button_1.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=500.0,
    y=445.0,
    width=170.0,
    height=60.0
)

button_image_3 = PhotoImage(file=relative_to_assets("button_1.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth = 0,
    highlightthickness = 1,
    command = lambda: print("button_3 clicked"),
    relief = "flat"
)
button_3.place(
    x=500.0,
    y=585.0,
    width=172.0,
    height=60.0
)

canvas.create_text(
    146.0,
    300.0,
    anchor="nw",
    text="Relação De Funcionários",
    fill="#FFFFFF",
    font=("Itim Regular", 30 * -1)
)

canvas.create_text(
    195.0,
    460.0,
    anchor="nw",
    text="Relações De Vagas",
    fill="#FFFFFF",
    font=("Itim Regular", 30 * -1)
)

canvas.create_text(
    225.0,
    599.0,
    anchor="nw",
    text="Treinamentos",
    fill="#FFFFFF",
    font=("Itim Regular", 30 * -1)
)

canvas.create_text(
    720.0,
    782.0,
    anchor="nw",
    text="W.Y.W",
    fill="#FFFFFF",
    font=("Alef Regular", 18 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    709.0,
    795.0,
    image=image_image_4
)

canvas.create_text(
    703.0,
    787.0,
    anchor="nw",
    text="C",
    fill="#FFFFFF",
    font=("Alata Regular", 14 * -1)
)
window.resizable(False, False)
window.mainloop()
