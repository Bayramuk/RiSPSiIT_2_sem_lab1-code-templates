"""
Модуль для расчёта аннуитетного платежа по кредиту.
"""

def calculate_payment(principal: float, rate: float, months: int) -> float:
    """
    Рассчитывает ежемесячный аннуитетный платёж по кредиту.

    Args:
        principal (float): Сумма кредита.
        rate (float): Годовая процентная ставка в процентах.
        months (int): Срок кредита в месяцах.

    Returns:
        float: Ежемесячный платёж, округлённый до двух знаков.

    Raises:
        ValueError: Если сумма, ставка или срок некорректны.
    """
    if principal < 0 or rate <= 0 or months <= 0:
        raise ValueError("Сумма, ставка и срок должны быть положительными!")
    monthly_rate = rate / 100 / 12
    payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** -months)
    return round(payment, 2)