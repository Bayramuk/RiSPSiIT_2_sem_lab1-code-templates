"""
Модуль для учёта рабочего времени в SQLite.
"""
import sqlite3

def add_hours(user_id: int, hours: float, role: str) -> None:
    """
    Добавляет отработанные часы.

    Args:
        user_id (int): ID сотрудника.
        hours (float): Количество часов.
        role (str): Роль сотрудника.

    Raises:
        ValueError: Если часы некорректны.
        PermissionError: Если нет прав на переработку.
        RuntimeError: При ошибке записи.
    """
    if hours < 0:
        raise ValueError("Часы не могут быть отрицательными!")
    if role != "manager" and hours > 8:
        raise PermissionError("Только менеджеры могут вносить переработку!")
    try:
        with sqlite3.connect("time.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO hours VALUES (?, ?)", (user_id, hours))
            conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        raise RuntimeError(f"Ошибка записи: {e}")