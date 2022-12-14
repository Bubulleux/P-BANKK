import tkinter as tk
from _main import App

class Page:
    def __init__(self, app):
        self.app: App = app

    def draw(self, window: tk.Tk):
        pass