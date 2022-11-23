import sqlite3

db = sqlite3.connect("data_base.db")
with open("db_init.sql") as f:
    db.executescript(f.read())