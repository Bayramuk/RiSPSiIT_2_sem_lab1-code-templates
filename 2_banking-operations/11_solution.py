"""
Модуль для генерации JSON-отчёта по транзакциям.
"""
import json

def generate_report(transactions: list) -> str:
    """
    Генерирует JSON-отчёт по транзакциям.

    Args:
        transactions (list): Список транзакций.

    Returns:
        str: JSON-отчёт.

    Raises:
        ValueError: Если список транзакций пуст.
    """
    if not transactions:
        raise ValueError("Список транзакций пуст!")
    return json.dumps({"transactions": transactions}, indent=4)