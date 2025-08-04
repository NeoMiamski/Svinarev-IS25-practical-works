# Приложение ВЫДАЧА КРЕДИТОВ для некоторой организации. БД должна
# содержать таблицу Клиент со следующей структурой записи: ФИО клиента, ФИО сотрудника банка,
# срок кредита, процент кредитаа, сумма кредита.

import sqlite3 as sq


with sq.connect('Debts.db') as con:
    cur = con.cursor()
    con.execute("""create table if not exists clients(
    id integer primary key,
    client text not null,
    bank_employee text not null,
    term date not null,
    percent integer not null,
    sum integer not null
    )""")