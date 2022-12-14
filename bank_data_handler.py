import sqlite3


class BankDBHandler:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.c = self.connection.cursor()

    def close(self):
        self.connection.close()

    def get_clients(self, name):
        data = self.c.execute("SELECT id_client, name, email FROM clients WHERE name LIKE ?", (f"%{name}%",)).fetchall()
        return {client_id: (name, email) for client_id, name, email in data}

    def get_client_by_id(self, client_id):
        data = self.c.execute("SELECT name, email FROM clients WHERE id_client = ?", (client_id,)).fetchone()
        return data

    def get_client_current_accounts(self, client_id):
        data = self.c.execute("SELECT id_account, client_id, sold, overdraft "
                              "FROM currents_accounts WHERE client_id = ?", (client_id,)).fetchall()
        return {account_id: (account_id, sold, overdraft) for account_id, _, sold, overdraft in data}

    def get_client_saving_accounts(self, client_id):
        data = self.c.execute("SELECT id_account, client_id, sold, rate "
                              "FROM savings_accounts WHERE client_id = ?", (client_id,)).fetchall()
        return {account_id: (account_id, sold, rate) for account_id, _, sold, rate in data}

    def get_all_current_account(self):
        data = self.c.execute("SELECT id_account, client_id, sold, overdraft FROM currents_accounts").fetchall()
        return {account_id: (client_id, sold, overdraft) for account_id, client_id, sold, overdraft in data}

    def get_all_saving_account(self):
        data = self.c.execute("SELECT id_account, client_id, sold, rate FROM savings_accounts").fetchall()
        return {account_id: (client_id, sold, rate) for account_id, client_id, sold, rate in data}

    def get_client_current_accounts_by_id(self, account_id):
        data = self.c.execute("SELECT client_id, sold, overdraft FROM currents_accounts WHERE id_account = ?",
                              (account_id,)).fetchone()
        return data

    def get_client_saving_accounts_by_id(self, account_id):
        data = self.c.execute("SELECT client_id, sold, rate FROM savings_accounts WHERE id_account = ?",
                              (account_id,)).fetchone()
        return data

    def update_all_saving_account(self):
        saving_accounts = self.get_all_saving_account()
        parameters = [(value[1] * (1 + value[2]), key) for key, value in saving_accounts.items()]
        self.c.executemany("UPDATE savings_accounts SET sold = ? WHERE id_account = ?", parameters)
        self.connection.commit()

    def set_accounts_overdraft(self, account_id, new_value):
        if new_value > 0 or self.get_client_current_accounts_by_id(account_id) is None:
            return False
        self.c.execute("UPDATE currents_accounts SET overdraft = ? WHERE id_account = ?", (new_value, account_id))
        self.connection.commit()
        return True

    def transfer_money(self, output_account, input_account, transfer_value):
        output_sold = self.get_client_current_accounts_by_id(output_account)[1]
        input_sold = self.get_client_current_accounts_by_id(input_account)[1]
        self.c.execute("UPDATE currents_accounts SET sold = ? WHERE id_account = ?",
                       (output_sold - transfer_value, output_account))
        self.c.execute("UPDATE currents_accounts SET sold = ? WHERE id_account = ?",
                       (input_sold + transfer_value, input_account))
        self.connection.commit()

    def delete_current_account(self, account_id):
        if self.get_client_current_accounts_by_id(account_id) is None:
            return False
        self.c.execute("DELETE FROM currents_accounts WHERE id_account = ?", (account_id,))
        self.connection.commit()
        return True

    def delete_saving_account(self, account_id):
        if self.get_client_saving_accounts_by_id(account_id) is None:
            return False
        self.c.execute("DELETE FROM savings_accounts WHERE id_account = ?", (account_id,))
        self.connection.commit()
        return True

    def delete_client(self, client_id, forced=False):
        if not forced and (self.get_client_current_accounts(client_id) != {} or
                           self.get_client_saving_accounts(client_id) != {}):
            return False

        for account_id in self.get_client_current_accounts(client_id):
            self.delete_current_account(account_id)
        for account_id in self.get_client_saving_accounts(client_id):
            self.delete_saving_account(account_id)

        self.c.execute("DELETE FROM clients WHERE id_client = ?", (client_id,))
        self.connection.commit()
        return True
