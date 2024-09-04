from tkinter import *
from pathlib import Path

class Tk_function():

    def assets(path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / "assets"

        return ASSETS_PATH / Path(path) # retorna
    
    def build(path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        BUILD_PATH = OUTPUT_PATH / "build"

        return BUILD_PATH / Path(path)

    def tela_button01(): # Window01
        pass

    def tela_button02():

        pass

    def tela_button03():
        pass

    def relacaoF_back(): # Window02
        pass

    def relacaoF_button01():
        pass

    def relacaoF_button02():
        pass
    
    def relacaoF_button03():
        pass

    def relacaoF_button04():
        pass

    def relacaoV_back(): # Window03
        pass

    def relacaoV_button01():
        pass

    def relacaoV_button02():
        pass

    def relacaoV_button03():
        pass
    
    def relacaoT_back(): # Window04
        pass

    def relacaoT_button01():
        pass

    def relacaoT_button02():
        pass

    def relacaoT_button03():
        pass

    def register_employee(): # Window05
        pass

    def register_employee_back():
        pass

    def register_vacancy(): # Window06
        pass

    def register_vacancy_back():
        pass

    def register_coaching(): # Window07
        pass

    def register_coaching_back():
        pass

    def payroll_back(): # Window08
        pass

    def entry_point_back(): # Window09
        pass

    def reviews_back(): # Window10
        pass

    def active_vacancies_back(): # Window11
        pass

    def talent_banck_back(): # Window12
        pass

    def active_coaching_back(): # Window13
        pass

    def training_history_back(): # Window14
        pass