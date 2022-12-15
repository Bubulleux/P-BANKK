import tkinter as tk
from route.page import Page
import route.custom_widget as custom_widget


class EmailPage(Page):
    def __init__(self, app):
        super().__init__(app)
        self.emails = []
        self.get_email = {}
        self.email()

    def email(self):
        self.get_email = self.app.db.get_email_when_decouvert()
        self.app.draw()

    def draw(self, window: tk.Tk):
        custom_widget.create_button(window, 0, 2, "Menu", self.app.go_to_main_menu)

        if len(self.get_email) == 0:
            tk.Label(window, text="Aucun client à découvert").grid(row=1, column=0)
            return

        tableau_result = tk.Frame(window, background="black")
        
        for i, (email) in enumerate(self.get_email):
            labels = [
                tk.Label(tableau_result, text=email),
            ]
            for j, label in enumerate(labels):
                label.grid(row=i + 1, column=j, padx=1, pady=1, sticky=tk.NSEW)
        tableau_result.grid(row=4, column=0, pady=2)
