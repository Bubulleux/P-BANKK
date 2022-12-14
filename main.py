import tkinter as tk
import bank_data_handler
import widgets

def test():
    print("bouton cliqué")

window = tk.Tk()
window.title("Ma Banque")
window.geometry("500x300")

#widgets.menu_client(window, (["header 1","header 2"], ["value 1", "value 2"]), (("header 3", "header 4"), ("value 3", "value 4")))
widgets.menu(window, ["Rechercher", "Ajouter", "Supprimer", "Quitter"], [test, test, test, window.destroy], "Un titre")

window.mainloop()
