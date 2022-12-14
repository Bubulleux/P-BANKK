import tkinter as tk


def create_button(win, row, col, text, function):
    button = tk.Button(win, text=text, command=function)
    button.grid(row=row, column=col)


def create_table(parent, row, col, headers, rows):
    table = tk.Frame(parent)
    for i, header in enumerate(headers):
        label = tk.Label(table, text=header)
        label.grid(row=0, column=i, padx=1, pady=1)
    for j, row in enumerate(rows):
        for i, value in enumerate(row):
            label = tk.Label(table, text=value)
            label.grid(row=j + 1, column=i, padx=1, pady=1)
    table.grid(row=row, column=col)


def destroy_widgets(parent):
    for child in parent.winfo_children():
        child.destroy()
