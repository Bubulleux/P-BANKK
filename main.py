import tkinter as tk
import bank_data_handler
import widgets


window = tk.Tk()
window.title("Ma Banque")
window.geometry("500x100")

widgets.menu_client(window, [{"yo":0, "test":1,"patate":2}], [])

window.mainloop()
