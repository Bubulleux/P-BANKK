import tkinter
import route
import bank_data_handler


class App:
    def __init__(self, db):
        self.window = tkinter.Tk()
        self.db = db
        self.page: route.Page = route.MainMenu(self, "Un titre", [
            ("Recherche", self.go_to_search_client),
            ("Quitter", self.destroy),
        ])

    def main_loop(self):
        self.draw()
        self.window.mainloop()

    def go_to_search_client(self):
        self.page = route.MenuRecherche(self)
        self.draw()

    def draw(self):
        route.custom_widget.destroy_widgets(self.window)
        self.page.draw(self.window)

    def destroy(self):
        self.window.destroy()


def main():
    db = bank_data_handler.BankDBHandler("data_base.db")
    app = App(db)
    app.main_loop()
    db.close()


if __name__ == "__main__":
    main()
