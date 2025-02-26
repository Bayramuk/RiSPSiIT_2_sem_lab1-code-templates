# Ошибки:
# 1. Уязвимость к SQL-инъекции.
# 2. Нет транзакций.
# 3. Пароль в коде (здесь опущен, но подразумевается).
def add_asset(name, value):
    import sqlite3
    conn = sqlite3.connect("collateral.db")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO assets VALUES ('{name}', {value})")
    conn.commit()