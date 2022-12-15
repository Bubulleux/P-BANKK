import tkinter as tk
from route.page import Page
import route.custom_widget as custom_widget


class SavingAccountPage(Page):
    def __init__(self, app):
        super().__init__(app)
        self.saving_account = {}
        self.get_data()

    def get_data(self):
        self.saving_account = self.app.db.get_all_saving_account()

    def update_sold(self):
        self.app.db.update_all_saving_account()
        self.get_data()
        self.app.draw()

    def draw(self, window: tk.Tk):
        custom_widget.create_button(window, 0, 0, "Rafraichire les Sold", self.update_sold)
        custom_widget.create_button(window, 0, 1, "Menu", self.app.go_to_main_menu)
        print(self.saving_account)


        tableau_saving = tk.Frame(window, background="black")
        headers = [
            tk.Label(tableau_saving, text="id du compte"),
            tk.Label(tableau_saving, text="solde"),
            tk.Label(tableau_saving, text="pourcentage"),
        ]
        for i, header in enumerate(headers):
            if header.cget("text") == "":
                header.grid(row=0, column=i, sticky=tk.NSEW)
            else:
                header.grid(row=0, column=i, padx=1, pady=1, sticky=tk.NSEW)
        for i, (key, value )in enumerate(self.saving_account.items()):
            labels = [
                tk.Label(tableau_saving, text=value[0]),
                tk.Label(tableau_saving, text=value[1]),
                tk.Label(tableau_saving, text=value[2]),
            ]
            for j, label in enumerate(labels):
                label.grid(row=i + 1, column=j, padx=1, pady=1, sticky=tk.NSEW)

        tableau_saving.grid(row=2, column=0, columnspan=2
                            )
