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


def menu(win, text_list, function_list, data_list,name):
    name=tk.Label(win, text=name)
    for i in range(len(text_list)):
        create_button(win,data_list[i][1],data_list[i][0], text=text_list[i], function=function_list[i])