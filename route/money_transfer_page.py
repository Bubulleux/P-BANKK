import tkinter as tk
from route.page import Page
import route.custom_widget as custom_widget


class MoneyTransferPage(Page):
    def __init__(self, app, account_id_a=None):
        super().__init__(app)
        self.debit_account, self.debit_sold, self.debit_overdraft = self.app.db.get_client_current_accounts_by_id(account_id_a) if account_id_a else (None, None, None)
        self.credit_entry = tk.IntVar()
        self.value_entry = tk.IntVar()

    def transfer(self):
        self.app.db.transfer_money(self.debit_account, self.credit_entry.get(), self.value_entry.get())
        self.app.draw()

    def draw(self, window: tk.Tk):
        tk.Label(window, text=f"Id du compte a débiter: {self.debit_account}").grid(row=0, column=0, columnspan=2)

        tk.Label(window, text="Id du compte a créditer:").grid(row=1, column=0)
        tk.Entry(window, textvariable=self.credit_entry).grid(row=1, column=1)

        tk.Label(window, text="Valeur à tranférer:").grid(row=2, column=0)
        tk.Entry(window, textvariable=self.value_entry).grid(row=2, column=1)

        custom_widget.create_button(window, 3, 0, "Transférer", self.transfer)
        custom_widget.create_button(window, 3, 1, "Retour", lambda: self.app.go_to_current_account_page(self.debit_account))
