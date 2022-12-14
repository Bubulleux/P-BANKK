import tkinter as tk
import bank_data_handler as dh
import widgets

def test():
    print("bouton cliqué")
    
def search(win,db):
    widgets.menu(win,["rechercher par nom et prénom","recherche par numéro de client"],[lambda : db.get_clients(input("nom prénom de la personne que vous cherchez")),lambda : db.get_client_by_id(input("id du client que vous cherchez"))],"Recherche")

def look_at(win, db):
    pass

def update(win,db):
    pass

db=dh.BankDBHandler("data_base.db")
window = tk.Tk()
window.title("Ma Banque")
window.geometry("500x300")

#widgets.menu_client(window, (["header 1","header 2"], ["value 1", "value 2"]), (("header 3", "header 4"), ("value 3", "value 4")))
widgets.menu(window, ["Rechercher", "Ajouter", "Supprimer", "Quitter"], [test, test, test, window.destroy], "Un titre")

window.mainloop()
