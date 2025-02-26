"""
Модуль для расчёта комиссий за перевод.
"""

def calculate_fee(amount: float, is_urgent: bool) -> float:
    """
    Рассчитывает комиссию за перевод.

    Args:
        amount (float): Сумма перевода.
        is_urgent (bool): Флаг срочного перевода.

    Returns:
        float: Комиссия, округлённая до двух знаков.

    Raises:
        ValueError: Если сумма ≤ 0.
    """
    if amount <= 0:
        raise ValueError("Сумма должна быть положительной!")
    fee_rate = 0.03 if is_urgent else 0.01
    return round(amount * fee_rate, 2)