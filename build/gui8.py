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
    417.0,
    457.0,
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
    x=116.0,
    y=139.0,
    width=64.0,
    height=55.0
)

canvas.create_text(
    189.0,
    147.0,
    anchor="nw",
    text="Folha de Pontos",
    fill="#FFFFFF",
    font=("IBMPlexSansCond Regular", 36 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    284.0,
    61.99999999999999,
    image=image_image_3
)

canvas.create_text(
    362.0,
    38.99999999999999,
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
    738.0,
    805.0,
    anchor="nw",
    text="C",
    fill="#FFFFFF",
    font=("Alata Regular", 14 * -1)
)
window.resizable(False, False)
window.mainloop()
