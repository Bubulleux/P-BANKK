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


def test_get_client_by_id():
    db = init()
    assert db.get_client_by_id(1) == ("Boby", "boby@gmail.com")
    assert db.get_client_by_id(-1) is None


def test_get_client_banks_current_accounts():
    db = init()
    assert db.get_client_banks_current_accounts(1) == {1: (501.01, -2)}
    assert db.get_client_banks_current_accounts(2) == {2: (1763987.0, -2000000.0), 3: (508539.0, -100000.0)}
    assert db.get_client_banks_current_accounts(-1) == {}


def test_get_client_saving_account():
    db = init()
    assert db.get_client_saving_account(2) == {2: (8299, 1.9), 3: (88923, 5)}
    assert db.get_client_saving_account(-1) == {}


def test_gel_all_bank_account():
    db = init()
    assert len(db.get_all_current_account()) == 7
    assert len(db.get_all_saving_account()) == 4


def test_get_current_accounts_by_id():
    db = init()
    assert db.get_current_accounts_by_id(3) == (2, 508539.0, -100000.0)
    assert db.get_current_accounts_by_id(-1) is None


def test_get_current_saving_by_id():
    db = init()
    assert db.get_saving_accounts_by_id(3) == (2, 88923.0, 5.0)
    assert db.get_saving_accounts_by_id(-1) is None


