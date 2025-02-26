"""
Модуль для учёта личных расходов в SQLite.
"""
import sqlite3

def add_expense(user_id: int, amount: float) -> None:
    """
    Добавляет запись о расходе в базу данных.

    Args:
        user_id (int): ID пользователя.
        amount (float): Сумма расхода.

    Raises:
        ValueError: Если сумма отрицательная.
        RuntimeError: При ошибке записи в БД.
    """
    if amount < 0:
        raise ValueError("Сумма не может быть отрицательной!")
    try:
        with sqlite3.connect("expenses.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO expenses VALUES (?, ?)", (user_id, amount))
            conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        raise RuntimeError(f"Ошибка записи в базу данных: {e}")