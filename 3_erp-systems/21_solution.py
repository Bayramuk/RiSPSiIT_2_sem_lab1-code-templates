"""
Модуль для учёта товаров на складе.
"""

items = set()

def add_item(sku: str) -> None:
    """
    Добавляет товар на склад.

    Args:
        sku (str): Уникальный код товара.

    Raises:
        ValueError: Если SKU уже существует или пустой.
    """
    if not sku:
        raise ValueError("SKU не может быть пустым!")
    if sku in items:
        raise ValueError(f"SKU {sku} уже существует!")
    items.add(sku)