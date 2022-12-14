import tkinter as tk
from route.page import Page
import route.custom_widget as custom_widget


class MainMenu(Page):
    def __init__(self, app):
        super().__init__(app)

    def draw(self, window: tk.Tk):
        name = tk.Label(window, text="Titre")
        name.grid(row=0, column=0)
        custom_widget.create_button(window, 1, 0, "Rechercher", self.app.go_to_search_client)
        custom_widget.create_button(window, 2, 0, "Test", lambda : self.app.go_to_client_page(1))
        custom_widget.create_button(window, 3, 0, "Quiter", self.app.destroy)

