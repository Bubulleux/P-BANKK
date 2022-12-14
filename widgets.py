import tkinter as tk


def create_button(win, row, col, text, function):
    button = tk.Button(win, text=text, command=function)
    button.grid(row=row, column=col)

def destroy_widgets(parent):
    for child in parent.winfo_children():
        child.destroy()

def menu(win, text_list, function_list,name):
    name=tk.Label(win,text=name)
    name.grid(row=0, column=0)
    for i in range(len(text_list)):
        create_button(win,i + 1,0, text_list[i], function_list[i])

def menu_client(win, comptes_courant, comptes_epargne):
    tableau_courant = tk.Frame(win, background="black")
    tableau_epargne = tk.Frame(win, background="black")

    headers = [tk.Label(tableau_courant, text=key) for key in comptes_courant[0]]
    for i, header in enumerate(headers):
        header.grid(row=0, column=i, padx=1, pady=1, sticky=tk.NSEW)
    for i, compte in enumerate(comptes_courant[1:]):
        labels = [tk.Label(tableau_courant, text=value) for value in compte]
        for j, label in enumerate(labels):
            label.grid(row=i + 1, column=j, padx=1, pady=1, sticky=tk.NSEW)

    headers = [tk.Label(tableau_epargne, text=key) for key in comptes_epargne[0]]
    for i, header in enumerate(headers):
        header.grid(row=0, column=i, padx=1, pady=1, sticky=tk.NSEW)
    for i, compte in enumerate(comptes_epargne[1:]):
        labels = [tk.Label(tableau_epargne, text=value) for value in compte]
        for j, label in enumerate(labels):
            label.grid(row=i + 1, column=j, padx=1, pady=1, sticky=tk.NSEW)
    
    tableau_courant.grid(row=0, column=0)
    tableau_epargne.grid(row=0, column=1)

def menu_recherche(win, db, text, fonction):
    search = tk.StringVar()
    bar = tk.Entry(win, width=30, textvariable=search)
    bar.insert(0, text)

    send = tk.Button(win, text="Rechercher", command=lambda : fonction(search.get(), db))

    bar.grid(row=0, column=0)
    send.grid(row=0, column=1)
