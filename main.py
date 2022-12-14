import tkinter as tk
import bank_data_handler
import widgets

def test():
    print("bouton cliqué")

window = tk.Tk()
window.title("Ma Banque")
window.geometry("500x100")

widgets.menu(window, ["rechercher par nom et prénom","rechercher par numéro de client"],[test,test],[(10,1),(1,2)],"main menu")

window.mainloop()
