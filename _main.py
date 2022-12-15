import tkinter
import route
import bank_data_handler
import init_db


class App:
    def __init__(self, db):
        self.window = tkinter.Tk()
        self.window.title("Ma Banque")
        # self.window.geometry("600x300")
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

    def go_to_current_account_page(self, account_id):
        self.page = route.CurrentAccountPage(self, account_id)
        self.draw()

    def go_to_money_transfer_page(self, account_id):
        self.page = route.MoneyTransferPage(self, account_id)
        self.draw()

    def go_to_email_page(self):
        self.page = route.EmailPage(self)
        self.draw()

    def go_to_transfer_page(self):
        self.page = route.MoneyTransferPage(self)
        self.draw()

    def go_to_all_saving_account(self):
        self.page = route.SavingAccountPage(self)
        self.draw()

    def reset_data_base(self):
        init_db.init()

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
