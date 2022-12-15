import tkinter as tk
from route.page import Page
import route.custom_widget as custom_widget


class MoneyTransferPage(Page):
    def __init__(self, app, account_id_a=None):
        super().__init__(app)
        self.account_a_entry = tk.IntVar()
        self.account_b_entry = tk.IntVar()

        if account_id_a is not None:
            self.account_a_entry.set(account_id_a)

        self.value_entry = tk.IntVar()
        self.sold_account_a, self.overdraft_account_a = None, None
        self.sold_account_b, self.overdraft_account_b = None, None
        self.get_data()

    def get_data(self):
        try:
            _, self.sold_account_a, self.overdraft_account_a = self.app.db.get_client_current_accounts_by_id(self.account_a_entry.get())
        except Exception as e:
            self.sold_account_a, self.overdraft_account_a = (None, None)

        try:
            _, self.sold_account_b, self.overdraft_account_b = self.app.db.get_client_current_accounts_by_id(self.account_b_entry.get())
        except Exception as e:
            self.sold_account_b, self.overdraft_account_b = (None, None)

    def show_data(self):
        self.get_data()
        self.app.draw()

    def transfer(self):
        try:
            self.app.db.transfer_money(self.account_a_entry.get(), self.account_b_entry.get(), self.value_entry.get())
            self.get_data()
            self.app.draw()
        except Exception as E:
            pass

    def draw(self, window: tk.Tk):
        tk.Label(window, text="Compte de débiter").grid(row=0, column=0)
        tk.Entry(window, textvariable=self.account_a_entry).grid(row=0, column=1)
        if self.sold_account_a is None:
            tk.Label(window, text="Aucun Compte n'a été trouver").grid(row=0, column=2)
        else:
            tk.Label(window, text=f"Sold du compte {self.sold_account_a}$, Déouvers autoriser: {self.overdraft_account_a}$").grid(row=0, column=2)


        tk.Label(window, text="Compte de créditer").grid(row=1, column=0)
        tk.Entry(window, textvariable=self.account_b_entry).grid(row=1, column=1)
        if self.sold_account_b is None:
            tk.Label(window, text="Aucun Compte n'a été trouver").grid(row=1, column=2)
        else:
            tk.Label(window, text=f"Sold du compte {self.sold_account_b}$, Déouvers autoriser:  {self.overdraft_account_b}$").grid(row=1, column=2)

        tk.Button(window, text="Actulaliser", command=self.show_data).grid(row=2, column=0)

        tk.Label(window, text="Valeur à tranférer:").grid(row=3, column=0)
        tk.Entry(window, textvariable=self.value_entry).grid(row=3, column=1)

        custom_widget.create_button(window, 4, 0, "Transférer", self.transfer)
        custom_widget.create_button(window, 4, 1, "Menu", lambda: self.app.go_to_main_menu())
