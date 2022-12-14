import tkinter as tk
import bank_data_handler as dh
import widgets

def test():
    print("bouton cliqué")
    
def main_menu(window,db):
    widgets.destroy_widgets(window)
    widgets.menu(window, ["Rechercher", "Ajouter", "Modifier", "Quitter"], [lambda: search(window,db),lambda: look_at(window,db),lambda: update(window,db), window.destroy], "Un titre")

def rechercher(text,db):
    # Bla bla bla tu recherches dans la database et tu l'affiches en appelant d'autres fonctions de wigets
    print(text)

def input_menu(win,text,db):
    widgets.destroy_widgets(win)
    (widgets.menu_recherche(win,db,text,rechercher))
    
def client_menu(win,dat):
    widgets.menu_client()

def search(win,db):
    widgets.destroy_widgets(win)
    widgets.menu(win,["rechercher par nom et prénom","recherche par numéro de client","revenir"],[lambda : db.get_clients(input_menu(win,"nom prénom de la personne que vous cherchez")),lambda : db.get_client_by_id(input_menu(win,"id du client que vous cherchez")),lambda:main_menu(win,db)],"Recherche")

def look_at(win, db):
    pass

def update(win,db):
    pass

db=dh.BankDBHandler("data_base.db")
window = tk.Tk()
window.title("Ma Banque")
window.geometry("500x300")

#widgets.menu_client(window, (["header 1","header 2"], ["value 1", "value 2"]), (("header 3", "header 4"), ("value 3", "value 4")))
main_menu(window,db)

window.mainloop()
