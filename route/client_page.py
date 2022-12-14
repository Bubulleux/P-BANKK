import tkinter as tk
from route.page import Page
import route.custom_widget as custom_widget


class ClientPage(Page):
    def __init__(self, app, client_id):
        super().__init__(app)
        self.client_id = client_id
        self.client_name = None
        self.client_email = None
        self.client_current_account = None
        self.client_saving_account = None
        self.get_data()

    def get_data(self):
        self.client_name, self.client_email = self.app.db.get_client_by_id(self.client_id)
        self.client_current_account = self.app.db.get_client_current_accounts(self.client_id)
        self.client_saving_account = self.app.db.get_client_saving_accounts(self.client_id)

    def draw(self, window: tk.Tk):
        custom_widget.create_button(window, 0, 0, "Menu", self.app.go_to_main_menu)

        tk.Label(window, text=f"Nom du client: {self.client_name}").grid(row=1, column=0)
        tk.Label(window, text=f"Email du client: {self.client_email}").grid(row=2, column=0)

        tk.Label(window, text=f"Compte courrant:").grid(row=3, column=0)
        tk.Label(window, text=f"Compte épargne:").grid(row=3, column=1)

        tableau_courant = tk.Frame(window, background="black")
        tableau_epargne = tk.Frame(window, background="black")

        headers = [
            tk.Label(tableau_courant, text="solde"),
            tk.Label(tableau_courant, text="overdraft"),
            tk.Label(tableau_courant)
        ]
        for i, header in enumerate(headers):
            header.grid(row=0, column=i, padx=1, pady=1, sticky=tk.NSEW)
        for i, (key, value) in enumerate(self.client_current_account.items()):
            labels = [
                tk.Label(tableau_courant, text=value[0]),
                tk.Label(tableau_courant, text=value[1]),
                tk.Button(tableau_courant, text="Supprimer", command=lambda: self.delete_current_account(key))
            ]
            for j, label in enumerate(labels):
                label.grid(row=i + 1, column=j, padx=1, pady=1, sticky=tk.NSEW)

        headers = [
            tk.Label(tableau_epargne, text="id du compte"),
            tk.Label(tableau_epargne, text="solde"),
            tk.Label(tableau_epargne, text="overdraft")
        ]
        for i, header in enumerate(headers):
            header.grid(row=0, column=i, padx=1, pady=1, sticky=tk.NSEW)
        for i, (key, value) in enumerate(self.client_saving_account.items()):
            labels = [
                tk.Label(tableau_epargne, text=value[0]),
                tk.Label(tableau_epargne, text=value[1]),
                tk.Button(tableau_epargne, text="Supprimer", command=lambda: self.delete_saving_account(key)),
            ]
            for j, label in enumerate(labels):
                label.grid(row=i + 1, column=j, padx=1, pady=1, sticky=tk.NSEW)

        tableau_courant.grid(row=4, column=0, pady=2)
        tableau_epargne.grid(row=4, column=1, pady=2)

    def delete_current_account(self, account_id):
        self.app.db.delete_current_account(account_id)
        self.get_data()
        self.app.draw()

    def delete_saving_account(self, account_id):
        self.app.db.delete_saving_account(account_id)
        self.get_data()
        self.app.draw()
