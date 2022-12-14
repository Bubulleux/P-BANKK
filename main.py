import tkinter as tk
import bank_data_handler as dh
import widgets

def test():
    print("bouton cliqué")
    
#def main_menu(window,db):
 #   widgets.destroy_widgets(window)
  #  widgets.menu(window, ["Rechercher", "Ajouter", "Modifier", "Quitter"], [lambda: search(window,db),lambda: look_at(window,db),lambda: update(window,db), window.destroy], "Un titre")

def rechercher_clients(text,db):
    widgets.destroy_widgets(window)
    widgets.menu_client(window, db.get_client_current_accounts(text),db.get_client_saving_accounts(text))
    cascade_menu(window)
def rechercher_clients_par_id(text,db):
    widgets.destroy_widgets(window)
    widgets.menu_client(window,  db.get_client_current_accounts_by_id(text),db.get_client_saving_accounts_by_id(text))
    cascade_menu(window)
#def input_menu(win,db,text,fnct):
 #   widgets.destroy_widgets(win)
  #  widgets.menu_recherche(win,db,text,fnct)
    
#def client_menu(win,dat):
 #   widgets.menu_client()

#def search(win,db):
 #   widgets.destroy_widgets(win)
  #  widgets.menu(win,["","recherche par numéro de client","revenir"],[lambda : input_menu(win,db,"nom prénom de la personne que vous cherchez",rechercher_clients),lambda : input_menu(win,db,"id du client que vous cherchez",rechercher_clients_par_id),lambda:main_menu(win,db)],"Recherche")

#def look_at(win, db):
 #   pass

#def update(win,db):
 #   pass

db=dh.BankDBHandler("data_base.db")
window = tk.Tk()
window.title("Ma Banque")
window.geometry("500x300")
def cascade_menu(window):
    menubar = tk.Menu(window)
    window.config(menu=menubar)
    search_menu=tk.Menu(menubar)
    look_menu=tk.Menu(menubar)
    update_menu=tk.Menu(menubar)
    client_menu=tk.Menu(update_menu)
    general_menu=tk.Menu(update_menu)

    search_menu.add_command(
        label='rechercher par nom et prénom',
        command=lambda: widgets.menu_recherche(window,db,"entrez nom prénom", rechercher_clients)
    )
    search_menu.add_command(
        label='recherche par numéro de client',
        command=lambda: widgets.menu_recherche(window,db,"entrez l'ID client", rechercher_clients_par_id)
    )

    look_menu.add_command(
    label="consulter les comptes courants d'un client",
    command=window.destroy
)
    look_menu.add_command(
    label="consulter les comptes épargnes d'un client",
    command=window.destroy
)

    client_menu.add_command(
    label="modifier l'autorisation de découvert d'un compte",
    command=window.destroy
)
    client_menu.add_command(
    label="réaliser un virement entre 2 comptes",
    command=window.destroy
)
    client_menu.add_command(
    label="supprimer le compte",
    command=window.destroy
)

    general_menu.add_command(
    label="actualiser tous les soldes des comptes épargnes en fnct de leurs taux",
    command=window.destroy
)
    general_menu.add_command(
    label="récupérer la liste des mails des personnes à découvert",
    command=window.destroy
)


    update_menu.add_cascade(
    label='menu client',
    menu=client_menu
)
    update_menu.add_cascade(
    label='menu client',
    menu=general_menu
)

    menubar.add_cascade(
    label="Recherche",
    menu=search_menu
)
    menubar.add_cascade(
    label="Observation",
    menu=look_menu
)
    menubar.add_cascade(
    label="Modification",
    menu=update_menu
)

#widgets.menu_client(window, (["header 1","header 2"], ["value 1", "value 2"]), (("header 3", "header 4"), ("value 3", "value 4")))
cascade_menu(window)
window.mainloop()
