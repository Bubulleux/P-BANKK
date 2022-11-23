import sqlite3


class BankDBHandler:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.c = self.connection.cursor()

    def get_clients(self, name):
        data = self.c.execute("SELECT id_client, name, email FROM clients WHERE name LIKE ?", (f"%{name}%",)).fetchall()
        return {client_id: (name, email) for client_id, name, email in data}

    def get_client_by_id(self, client_id):
        data = self.c.execute("SELECT name, email FROM clients WHERE id_client = ?", (client_id,)).fetchone()
        return data

    def get_client_banks_current_accounts(self, client_id):
        data = self.c.execute("SELECT id_account, client_id, sold, overdraft "
                              "FROM currents_accounts WHERE client_id = ?", (client_id,)).fetchall()
        return {account_id: (sold, overdraft) for account_id, _, sold, overdraft in data}

    def get_client_saving_account(self, client_id):
        data = self.c.execute("SELECT id_account, client_id, sold, rate "
                              "FROM savings_accounts WHERE client_id = ?", (client_id,)).fetchall()
        return {account_id: (sold, rate) for account_id, _, sold, rate in data}

    def get_all_current_account(self):
        data = self.c.execute("SELECT id_account, client_id, sold, overdraft FROM currents_accounts").fetchall()
        return {account_id: (client_id, sold, overdraft) for account_id, client_id, sold, overdraft in data}

    def get_all_saving_account(self):
        data = self.c.execute("SELECT id_account, client_id, sold, rate FROM savings_accounts").fetchall()
        return {account_id: (client_id, sold, rate) for account_id, client_id, sold, rate in data}

    def get_current_accounts_by_id(self, account_id):
        data = self.c.execute("SELECT client_id, sold, overdraft FROM currents_accounts WHERE id_account = ?",
                              (account_id,)).fetchone()
        return data

    def get_saving_accounts_by_id(self, account_id):
        data = self.c.execute("SELECT client_id, sold, rate FROM savings_accounts WHERE id_account = ?",
                              (account_id,)).fetchone()
        return data

    def update_all_saving_account(self):
        pass

    def set_accounts_overdraft(self, account_id, new_value):
        if new_value > 0:
            return False
        try:
            self.c.execute("UPDATE currents_accounts SET overdraft = ? WHERE id_clients = ?", (new_value, account_id))
        except Exception as e:
            return False
        return True

    def transfer_money(self, output_account, input_account, transfer_value):
        pass

    def delete_client(self, client_id):
        pass

    def delete_current_account(self, account_id):
        pass

    def delete_saving_account(self, account_id):
        pass




