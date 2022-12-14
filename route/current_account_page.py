import tkinter as tk
from route.page import Page
import route.custom_widget as custom_widget


class CurrentAccountPage(Page):
    def __init__(self, app, account_id):
        super().__init__(app)
        self.account_id = account_id
        self.overdraft_entry = tk.IntVar()
        self.client_id, self.account_sold, self.overdraft = (None, None, None)
        self.get_data()

    def get_data(self):
        self.client_id, self.account_sold, self.overdraft = self.app.db.get_client_current_accounts_by_id(self.account_id)
        self.overdraft_entry.set(self.overdraft)

    def set_overdraft(self):
        self.app.db.set_accounts_overdraft(self.account_id, self.overdraft_entry.get())
        self.get_data()
        self.app.draw()

    def draw(self, window: tk.Tk):
        custom_widget.create_button(window, 0, 0, "Retour", lambda: self.app.go_to_client_page(self.client_id))
        custom_widget.create_button(window, 0, 1, "Transférer de l'argent", lambda: self.app.go_to_money_transfer_page(self.account_id))
        custom_widget.create_button(window, 0, 2, "Menu", self.app.go_to_main_menu)

        tk.Label(window, text=f"Id du compte: {self.account_id}").grid(row=1, column=0)
        tk.Label(window, text=f"Id du client: {self.client_id}").grid(row=1, column=1)
        tk.Label(window, text=f"Sold du compte: {self.account_sold}$").grid(row=2, column=0)

        tk.Label(window, text="Découvers du compte:").grid(row=3, column=0)
        tk.Entry(window, textvariable=self.overdraft_entry).grid(row=3, column=1)
        tk.Button(window, text="Valider", command=self.set_overdraft).grid(row=3, column=2)
