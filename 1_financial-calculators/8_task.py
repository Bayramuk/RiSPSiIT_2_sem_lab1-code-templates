# Ошибки:
# 1. Уязвимость к SQL-инъекции.
# 2. Нет транзакций для атомарности.
# 3. Хранение пароля в коде (здесь опущено, но подразумевается).
def add_expense(user_id, amount):
    import sqlite3
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO expenses VALUES ({user_id}, {amount})")
    conn.commit()