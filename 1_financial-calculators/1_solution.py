"""
Модуль для расчёта доходности вклада по сложным процентам.
"""

def calculate_profit(principal: float, rate: float, years: int) -> float:
    """
    Рассчитывает доходность вклада по формуле сложных процентов.

    Args:
        principal (float): Начальная сумма вклада.
        rate (float): Годовая процентная ставка в процентах.
        years (int): Срок вклада в годах.

    Returns:
        float: Доходность вклада, округлённая до двух знаков.

    Raises:
        ValueError: Если сумма, ставка или срок отрицательны.
    """
    if principal < 0 or rate < 0 or years <= 0:
        raise ValueError("Сумма, ставка и срок должны быть положительными!")
    return round(principal * (1 + rate / 100) ** years - principal, 2)