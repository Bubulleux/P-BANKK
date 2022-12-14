import tkinter as tk
from route.page import Page
import route.custom_widget as custom_widget


class ClientPage(Page):
    def __init__(self, app, client_id=None):
        super().__init__(app)
        self.id_entry = tk.IntVar()

        if client_id is not None:
            self.id_entry.set(client_id)

        self.client_id = client_id
        self.client_name = None
        self.client_email = None
        self.client_current_account = None
        self.client_saving_account = None
        self.get_data()

    def get_data(self):
        try:
            self.client_id = self.id_entry.get()
            self.client_name, self.client_email = self.app.db.get_client_by_id(self.client_id)
            self.client_current_account = self.app.db.get_client_current_accounts(self.client_id)
            self.client_saving_account = self.app.db.get_client_saving_accounts(self.client_id)
        except Exception as e:
            self.client_id = None

    def update_data(self):
        self.get_data()
        self.app.draw()

    def draw(self, window: tk.Tk):
        tk.Label(window, text="Id du client").grid(row=0, column=0)
        tk.Entry(window, width=20, textvariable=self.id_entry).grid(row=0, column=1)
        custom_widget.create_button(window, 0, 2, "Rechercher", self.update_data)
        custom_widget.create_button(window, 0, 3, "Menu", self.app.go_to_main_menu)

        if self.client_id is None:
            tk.Label(window, text="Aucun client trouvé").grid(row=1, column=0)
            return

        tk.Label(window, text=f"Nom du client: {self.client_name}").grid(row=1, column=0)
        tk.Label(window, text=f"Email du client: {self.client_email}").grid(row=2, column=0)

        tk.Label(window, text=f"Comptes courrant:").grid(row=3, column=0)
        tk.Label(window, text=f"Comptes épargne:").grid(row=3, column=2)

        tableau_courant = tk.Frame(window, background="black")
        tableau_epargne = tk.Frame(window, background="black")

        headers = [
            tk.Label(tableau_courant, text="id du compte"),
            tk.Label(tableau_courant, text="solde"),
            tk.Label(tableau_courant, text="découvert"),
            tk.Label(tableau_courant),
            tk.Label(tableau_courant)
        ]
        for i, header in enumerate(headers):
            if header.cget("text") == "":
                header.grid(row=0, column=i, sticky=tk.NSEW)
            else:
                header.grid(row=0, column=i, padx=1, pady=1, sticky=tk.NSEW)
        for i, (key, value) in enumerate(self.client_current_account.items()):
            labels = [
                tk.Label(tableau_courant, text=value[0]),
                tk.Label(tableau_courant, text=value[1]),
                tk.Label(tableau_courant, text=value[2]),
                tk.Button(tableau_courant, text="Voire le compte", command=lambda k=key: self.app.go_to_current_account_page(k)),
                tk.Button(tableau_courant, text="Supprimer", command=lambda k=key: self.delete_current_account(k))
            ]
            for j, label in enumerate(labels):
                label.grid(row=i + 1, column=j, padx=1, pady=1, sticky=tk.NSEW)

        headers = [
            tk.Label(tableau_epargne, text="id du compte"),
            tk.Label(tableau_epargne, text="solde"),
            tk.Label(tableau_epargne, text="pourcentage"),
            tk.Label(tableau_epargne)
        ]
        for i, header in enumerate(headers):
            if header.cget("text") == "":
                header.grid(row=0, column=i, sticky=tk.NSEW)
            else:
                header.grid(row=0, column=i, padx=1, pady=1, sticky=tk.NSEW)
        for i, (key, value) in enumerate(self.client_saving_account.items()):
            labels = [
                tk.Label(tableau_epargne, text=value[0]),
                tk.Label(tableau_epargne, text=value[1]),
                tk.Label(tableau_epargne, text=value[2]),
                tk.Button(tableau_epargne, text="Supprimer", command=lambda k=key: self.delete_saving_account(k))
            ]
            for j, label in enumerate(labels):
                label.grid(row=i + 1, column=j, padx=1, pady=1, sticky=tk.NSEW)

        tableau_courant.grid(row=4, column=0, pady=2)
        tableau_epargne.grid(row=4, column=2, pady=2)

    def delete_current_account(self, account_id):
        self.app.db.delete_current_account(account_id)
        self.get_data()
        self.app.draw()

    def delete_saving_account(self, account_id):
        self.app.db.delete_saving_account(account_id)
        self.get_data()
        self.app.draw()
