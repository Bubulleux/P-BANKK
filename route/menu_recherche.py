import tkinter as tk
from route.page import Page
import route.custom_widget as custom_widget


class MenuRecherche(Page):
    def __init__(self, app):
        super().__init__(app)
        self.search_text = tk.StringVar()
        self.comptes_courants = []
        self.comptes_epargnes = []
        self.search_client = {}
        self.search()

    def search(self):
        self.search_client = self.app.db.get_clients(self.search_text.get())
        self.app.draw()

    def draw(self, window: tk.Tk):
        barre = tk.Entry(window, width=50, textvariable=self.search_text)
        barre.grid(row=0, column=0)
        custom_widget.create_button(window, 0, 1, "Rechercher", self.search)
        custom_widget.create_button(window, 0, 2, "Menu", self.app.go_to_main_menu)

        if len(self.search_client) == 0:
            tk.Label(window, text="Aucun client trouver").grid(row=1, column=0)
            return

        tableau_result = tk.Frame(window, background="black")
        headers = [
            tk.Label(tableau_result, text="Nom du client"),
            tk.Label(tableau_result, text="Email du client"),
            tk.Label(tableau_result)
        ]
        for i, header in enumerate(headers):
            header.grid(row=0, column=i, padx=1, pady=1, sticky=tk.NSEW)
        for i, (key, value) in enumerate(self.search_client.items()):
            labels = [
                tk.Label(tableau_result, text=value[0]),
                tk.Label(tableau_result, text=value[1]),
                tk.Button(tableau_result, text="Info", command=lambda k=key: self.app.go_to_client_page(k))
            ]
            for j, label in enumerate(labels):
                label.grid(row=i + 1, column=j, padx=1, pady=1, sticky=tk.NSEW)
        tableau_result.grid(row=4, column=0, pady=2)
