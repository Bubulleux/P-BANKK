import tkinter as tk
from route.page import Page
import route.custom_widget as custom_widget


class MenuRecherche(Page):
    def __init__(self, app):
        super().__init__(app)
        self.boutons = [(0, 1,  "Rechercher", lambda: 0)]

    def draw(self, window: tk.Tk):
        pass
