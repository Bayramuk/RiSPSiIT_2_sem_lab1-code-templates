"""
Модуль для конвертации валют.
"""

def convert_currency(amount: float, rate: float) -> float:
    """
    Конвертирует сумму из одной валюты в другую.

    Args:
        amount (float): Сумма для конвертации.
        rate (float): Курс обмена (например, USD/RUB).

    Returns:
        float: Сумма в целевой валюте, округлённая до двух знаков.

    Raises:
        ValueError: Если сумма или курс отрицательны.
    """
    if amount < 0 or rate < 0:
        raise ValueError("Сумма и курс должны быть неотрицательными!")
    return round(amount * rate, 2)