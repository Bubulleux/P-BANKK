import tkinter as tk
from route.page import Page
import route.custom_widget as custom_widget


class MenuRecherche(Page):
    def __init__(self, app, account_a=None, account_b=None):
        super().__init__(app)
        self.entry_account_a = tk.IntVar()
        self.entry_account_b = tk.IntVar()
        self.


    def get_data(self):
        self.app.draw()

    def draw(self, window: tk.Tk):
        tk.Label(window, text="Coumpte a débiter:").grid(row=0, column=0)
        tk.Label(window, text="Coumpte a créditer:").grid(row=0, column=1)
