import os
from pathlib import Path
from tkinter import Tk


class Window:
    ASSETS_FOLDER = Path(__file__).parent

    def __init__(self, root: Tk, width: int = 825, height: int = 825):
        self.root = root
        self.width = width
        self.height = height

    def assets(self, filename: str) -> str:
        return os.path.join(self.ASSETS_FOLDER, 'assets', filename)

    def create(self) -> None:
        self.root.geometry(newGeometry=f'{self.width}x{self.height}')
        pass

    def run(self) -> None:
        self.root.mainloop()

    def show(self) -> None:
        self.root.deiconify()

    def hide(self) -> None:
        self.root.withdraw()

    def quit(self) -> None:
        self.root.quit()

    def destroy(self) -> None:
        self.root.destroy()

    def switch_window(self, swap_to: 'Window | None') -> None:
        if swap_to == None:
            return
        self.hide()
        swap_to.show()
        swap_to.create()
