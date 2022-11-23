import sqlite3


class BankDBHandler:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.c = self.connection.cursor()

    def get_client(self, name):
        pass

    def get_client_by_id(self, id):
        pass

    def get_client_banks_current_accounts(self, client_id):
        pass

    def set_accounts_overdraft(self, new_value):
        pass

    def transfer_money(self, output_account, input_account, transfer_value):
        pass

    def client_saving_account(self, client_id):
        pass

    def get_all_current_account(self):
        pass

    def get_all_saving_account(self):
        pass

    def update_all_saving_account(self):
        pass

    def delete_client(self, client_id):
        pass

    def delete_current_account(self, account_id):
        pass

    def delete_saving_account(self, account_id):
        pass



