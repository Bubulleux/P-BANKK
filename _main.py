import tkinter
import route
import bank_data_handler
import init_db


class App:
    def __init__(self, db):
        self.window = tkinter.Tk()
        self.window.title("Ma Banque")
        self.window.geometry("500x300")
        self.db: bank_data_handler.BankDBHandler = db
        self.page: route.Page = route.MainMenu(self)

    def main_loop(self):
        self.go_to_main_menu()
        self.window.mainloop()

    def go_to_search_client(self):
        self.page = route.MenuRecherche(self)
        self.draw()

    def go_to_main_menu(self):
        self.page = route.MainMenu(self)
        self.draw()

    def go_to_client_page(self, client_id):
        self.page = route.ClientPage(self, client_id)
        self.draw()

    def draw(self):
        route.custom_widget.destroy_widgets(self.window)
        self.page.draw(self.window)

    def destroy(self):
        self.window.destroy()


def main():
    init_db.init()
    db = bank_data_handler.BankDBHandler("data_base.db")
    app = App(db)
    app.main_loop()
    db.close()


if __name__ == "__main__":
    main()
