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
window.geometry("500x100")

widgets.menu(window, ["Recherche","Observer un compte","Modifier des informations d'un compte"],[lambda : search(window,db),test,test],"main menu")
window.mainloop()
