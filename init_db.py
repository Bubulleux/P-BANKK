import sqlite3


def init():
    db = sqlite3.connect("data_base.db")
    with open("db_init.sql") as f:
        db.executescript(f.read())


if __name__ == "__main__":
    init()