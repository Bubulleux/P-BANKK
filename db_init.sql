DROP TABLE IF EXISTS "clients";
DROP TABLE IF EXISTS "currents_accounts";
DROP TABLE IF EXISTS "savings_accounts";

CREATE TABLE "clients" (
  "id_client"  INTEGER NOT NULL,
  "name"  TEXT NOT NULL,
  "email"  TEXT NOT NULL,
  PRIMARY KEY("id_client" AUTOINCREMENT)
);

CREATE TABLE "currents_accounts" (
  "id_account" INTEGER NOT NULL,
  "client_id" INTEGER,
  "sold"  FLOAT NOT NULL,
  "overdraft" FLOAT NOT NULL,
  PRIMARY KEY("id_account" AUTOINCREMENT)
);

CREATE TABLE "savings_accounts" (
  "id_account"  INTEGER NOT NULL,
  "client_id" INTEGER,
  "sold" FLOAT NOT NULL,
  "rate" FLOAT NOT NULL,
  PRIMARY KEY("id_account" AUTOINCREMENT)
);

INSERT INTO clients(id_client, name, email) VALUES
    (1, "Boby", "boby@gmail.com"),
    (2, "François", "notre_belle_france@gmail.com"),
    (3, "Amed", "amed@gmail.com"),
    (4, "Jackson", "america@gmail.com"),
    (5, "Noname", "personne@gmail.com");

INSERT INTO currents_accounts(client_id, sold, overdraft) VALUES
    (1, 501.01, -2),
    (1, -20, -50),
    (2, 1763987, -2000000),
    (2, 508539, -100000),
    (3, -100, -500),
    (4, 1837, -1),
    (5, 3, 0),
    (4, 158, 0);

INSERT INTO savings_accounts(client_id, sold, rate) VALUES
    (1, 3, 5),
    (2, 8299, 1.9),
    (2, 88923, 5),
    (5, 1, 1.01),
    (1, 0, 5),
    (1, 5, 0);
