import tkinter as tk

def create_button(win, row, col, text, function):
    button = tk.Button(win, text=text, command=function)
    button.grid(row=row, column=col)


def destroy_widgets(parent):
    for child in parent.winfo_children():
        child.destroy()