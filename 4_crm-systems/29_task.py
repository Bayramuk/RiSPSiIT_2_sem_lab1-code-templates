# Ошибки:
# 1. Неверный расчёт переработки (нет проверки).
# 2. Нет проверки прав доступа.
# 3. Уязвимость к SQL-инъекции.
def add_hours(user_id, hours):
    import sqlite3
    conn = sqlite3.connect("time.db")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO hours VALUES ({user_id}, {hours})")
    conn.commit()