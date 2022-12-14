import tkinter as tk


def create_button(win, row, col, text, function):
    button = tk.Button(win, text=text, command=function)
    button.grid(row=row, column=col)

def menu_client(win, comptes_courant, comptes_epargne):
    tableau_courant = tk.Frame(win)
    tableau_epargne = tk.Frame(win)

    headers = [tk.Label(tableau_courant, text=key, border="black") for key in comptes_courant[0]]
    for i, header in enumerate(headers):
        header.grid(row=0, column=i)
    for i, compte in enumerate(comptes_courant[1:]):
        labels = [tk.Label(tableau_courant, text=value, border="black") for value in compte]
        for j, label in enumerate(labels):
            label.grid(row=i + 1, column=j)
    tableau_courant.grid(row=0, column=0)

    headers = [tk.Label(tableau_epargne, text=key, border="black") for key in comptes_epargne[0]]
    for i, header in enumerate(headers):
        header.grid(row=0, column=i)
    for i, compte in enumerate(comptes_epargne[1:]):
        labels = [tk.Label(tableau_epargne, text=value, border="black") for value in compte]
        for j, label in enumerate(labels):
            label.grid(row=i + 1, column=j)
    tableau_epargne.grid(row=1, column=0)
