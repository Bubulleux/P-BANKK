import bank_data_handler
import init_db


def init():
    init_db.init()
    return bank_data_handler.BankDBHandler("data_base.db")


def test_get_client():
    db = init()
    assert db.get_clients("Bo") == {1: ("Boby", "boby@gmail.com")}
    assert len(db.get_clients("")) == 5
    assert db.get_clients("azerty") == {}
    db.close()


def test_get_client_by_id():
    db = init()
    assert db.get_client_by_id(1) == ("Boby", "boby@gmail.com")
    assert db.get_client_by_id(-1) is None
    db.close()


def test_get_client_banks_current_accounts():
    db = init()
    assert db.get_client_current_accounts(1) == {1: (501.01, -2)}
    assert db.get_client_current_accounts(2) == {2: (1763987.0, -2000000.0), 3: (508539.0, -100000.0)}
    assert db.get_client_current_accounts(-1) == {}
    db.close()


def test_get_client_saving_account():
    db = init()
    assert db.get_client_saving_account(2) == {2: (8299, 1.9), 3: (88923, 5)}
    assert db.get_client_saving_account(-1) == {}
    db.close()


def test_gel_all_bank_account():
    db = init()
    assert len(db.get_all_current_account()) == 7
    assert len(db.get_all_saving_account()) == 4
    db.close()


def test_get_current_accounts_by_id():
    db = init()
    assert db.get_current_accounts_by_id(3) == (2, 508539.0, -100000.0)
    assert db.get_current_accounts_by_id(-1) is None
    db.close()


def test_get_current_saving_by_id():
    db = init()
    assert db.get_saving_accounts_by_id(3) == (2, 88923.0, 5.0)
    assert db.get_saving_accounts_by_id(-1) is None
    db.close()


def test_transfer_money():
    db = init()
    db.transfer_money(4, 5, 100)
    assert db.get_current_accounts_by_id(4)[1] == 228
    assert db.get_current_accounts_by_id(5)[1] == 1937
    db.close()


def test_delete_account():
    db = init()
    assert db.delete_current_account(6) == True
    assert db.delete_current_account(6) == False
    assert db.get_client_current_accounts(5) == []
    assert db.get_current_accounts_by_id(6) is None
    db.close()


def test_delete_saving_account():
    db = init()
    assert db.delete_saving_account(4) == True
    assert db.delete_saving_account(4) == False
    assert db.get_client_saving_account(5) == []
    assert db.get_saving_accounts_by_id(4) is None
    db.close()


def test_delete_client():
    db = init()
    assert db.delete_client(3) == False
    assert db.delete_current_account(4) == True
    assert db.delete_client(3) == True
    assert db.get_client_by_id(3) is None

    assert db.delete_client(5) == False
    assert db.delete_client(5, forced=True) == True
    assert db.get_client_by_id(5) is None
    assert db.get_client_current_accounts(5) == []
    assert db.get_client_saving_account(5) == []
    db.close()
