# Ошибки:
# 1. Уязвимость к SQL-инъекциям.
# 2. Нет обработки ошибок базы данных.
import sqlite3
def get_report(user_id):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM transactions WHERE user_id = {user_id}")
    return cursor.fetchall()