import tkinter as tk
from route.page import Page
import route.custom_widget as custom_widget


class MainMenu(Page):
    def __init__(self, app, name, button):
        super().__init__(app)
        self.name = name
        self.button = button

    def draw(self, window: tk.Tk):
        name = tk.Label(window, text=self.name)
        name.grid(row=0, column=0)
        for i, (button_name, button_function) in enumerate(self.button):
            custom_widget.create_button(window, i + 1, 0, button_name, button_function)

