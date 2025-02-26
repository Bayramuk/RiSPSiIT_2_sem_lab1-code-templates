"""
Модуль для получения SQL-отчёта по транзакциям.
"""
import sqlite3

def get_report(user_id: int) -> list:
    """
    Получает отчёт по транзакциям для пользователя.

    Args:
        user_id (int): ID пользователя.

    Returns:
        list: Список транзакций.

    Raises:
        RuntimeError: При ошибке базы данных.
    """
    try:
        with sqlite3.connect("bank.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM transactions WHERE user_id = ?", (user_id,))
            return cursor.fetchall()
    except sqlite3.Error as e:
        raise RuntimeError(f"Ошибка базы данных: {e}")