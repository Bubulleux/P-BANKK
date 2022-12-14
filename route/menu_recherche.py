import tkinter as tk
from route.page import Page
import route.custom_widget as custom_widget


class MenuRecherche(Page):
    def __init__(self, app):
        super().__init__(app)
        self.search_text = tk.StringVar()
        self.comptes_courants = []
        self.comptes_epargnes = []

    def search(self):
        return self.search_text

    def draw(self, window: tk.Tk):
        barre = tk.Entry(window, width=50, textvariable=self.search_text)
        barre.grid(row=0, column=0)
        custom_widget.create_button(window, 0, 1, "Rechercher", self.search)

        custom_widget.create_table(window, 1, 0, self.comptes_courants[0], self.comptes_courants[1:])
        custom_widget.create_table(window, 2, 0, self.comptes_epargnes[0], self.comptes_epargnes[1:])
