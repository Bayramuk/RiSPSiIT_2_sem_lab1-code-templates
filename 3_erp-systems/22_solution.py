"""
Модуль для расчёта зарплаты с учётом налогов.
"""
from decimal import Decimal, ROUND_HALF_UP

def calculate_salary(gross: float, deduction: float = 0) -> float:
    """
    Рассчитывает зарплату с учётом НДФЛ и вычетов.

    Args:
        gross (float): Зарплата до налогообложения.
        deduction (float): Налоговый вычет.

    Returns:
        float: Зарплата после налогообложения.

    Raises:
        ValueError: Если зарплата или вычет некорректны.
    """
    if gross < 0 or deduction < 0:
        raise ValueError("Зарплата и вычет не могут быть отрицательными!")
    taxable = max(gross - deduction, 0)
    tax = Decimal(taxable * 0.13).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return float(Decimal(gross) - tax)