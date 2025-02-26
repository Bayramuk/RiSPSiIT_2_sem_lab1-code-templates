"""
Модуль для управления заказами в SQLite.
"""
import sqlite3

def add_order(user_id: int, product: str) -> None:
    """
    Добавляет заказ в систему.

    Args:
        user_id (int): ID пользователя.
        product (str): Название продукта.

    Raises:
        ValueError: Если продукт пустой.
        RuntimeError: При ошибке записи.
    """
    if not product:
        raise ValueError("Название продукта не может быть пустым!")
    try:
        with sqlite3.connect("orders.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO orders VALUES (?, ?)", (user_id, product))
            conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        raise RuntimeError(f"Ошибка записи: {e}")