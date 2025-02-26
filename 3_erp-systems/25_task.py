# Ошибки:
# 1. Уязвимость к SQL-инъекции.
# 2. Нет транзакций.
# 3. Пароль в коде (здесь опущен, но подразумевается).
def add_order(user_id, product):
    import sqlite3
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO orders VALUES ({user_id}, '{product}')")
    conn.commit()