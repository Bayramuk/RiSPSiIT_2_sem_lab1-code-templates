"""
Модуль для учёта залогового имущества в SQLite.
"""
import sqlite3

def add_asset(name: str, value: float) -> None:
    """
    Добавляет залоговое имущество в базу данных.

    Args:
        name (str): Название имущества.
        value (float): Стоимость имущества.

    Raises:
        ValueError: Если стоимость отрицательная.
        RuntimeError: При ошибке записи.
    """
    if value < 0:
        raise ValueError("Стоимость не может быть отрицательной!")
    try:
        with sqlite3.connect("collateral.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO assets VALUES (?, ?)", (name, value))
            conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        raise RuntimeError(f"Ошибка записи: {e}")