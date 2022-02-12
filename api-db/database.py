import sqlite3
import pandas as pd
import os

def add_wallet(wallet, user_id, user_name, date):
    try:
        conn = sqlite3.connect("whitelist.db")
        conn.execute('INSERT INTO WHITELIST VALUES (?, ?, ?, ?)', (user_id, user_name, date, wallet))
        conn.commit()
    except:
        return (0)
    return (1)

def get_wallet(user_id):
    conn = sqlite3.connect("whitelist.db")
    return (conn.execute('SELECT WALLET FROM whitelist WHERE USER_ID=?', (user_id,)))

def update_wallet(wallet_address, user_id, date):
    try:
        conn = sqlite3.connect("whitelist.db")
        conn.execute("UPDATE whitelist SET wallet=?, last_updated=? WHERE user_id=?",(wallet_address, date, user_id))
        conn.commit()
    except:
        return (0)
    return (1)

def db_export_excel():
        os.system("bash convert_to_csv.sh")
        read_file = pd.read_csv ("./whitelist.csv")
        read_file.to_excel ('./whitelist.xlsx', index = None, header=True)


