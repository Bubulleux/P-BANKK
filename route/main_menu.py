import tkinter as tk
from route.page import Page
import route.custom_widget as custom_widget


class MainMenu(Page):
    def __init__(self, app):
        super().__init__(app)

    def draw(self, window: tk.Tk):
        name = tk.Label(window, text="Menu principal")
        name.grid(row=0, column=0)
        custom_widget.create_button(window, 1, 0, "Rechercher", self.app.go_to_search_client)
        custom_widget.create_button(window, 2, 0, "Recher un client avec un id", lambda: self.app.go_to_client_page(1))
        custom_widget.create_button(window, 3, 0, "Obtenir les Emails des clients à découvert", lambda: self.app.go_to_email_page())
        custom_widget.create_button(window, 4, 0, "Transférer de l'argent", lambda: self.app.go_to_transfer_page())
        custom_widget.create_button(window, 5, 0, "Compte épargne", lambda: self.app.go_to_all_saving_account())
        custom_widget.create_button(window, 6, 0, "Ré initialiser la base de donner", lambda: self.app.reset_data_base())
        custom_widget.create_button(window, 7, 0, "Quiter", self.app.destroy)
