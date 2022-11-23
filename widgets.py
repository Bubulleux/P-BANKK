import tkinter as tk


def create_button(win, row, col, text, function):
    button = tk.Button(win, text = text, command = function)
    button.grid(row = row, column = col)

def menu_client(win, comptes_courant, comptes_epargne):
    tableau_courant = tk.Frame(win)
    headers = [tk.Label(tableau_courant, text = key, highlightthickness = 2) for key in comptes_courant[0].keys()]
    for i in range(len(headers)):
        headers[i].config(highlightbackground = "red", highlightcolor= "red")
        headers[i].grid(row = 0, column = i)
    tableau_courant.pack()
