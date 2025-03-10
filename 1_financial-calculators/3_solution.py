"""
Модуль для расчёта амортизации оборудования по методу ускоренной амортизации.
"""

def calculate_depreciation(cost: float, lifespan: int) -> float:
    """
    Рассчитывает годовую амортизацию оборудования по методу ускоренной амортизации.

    Args:
        cost (float): Стоимость оборудования.
        lifespan (int): Срок службы в годах.

    Returns:
        float: Годовая амортизация, округлённая до двух знаков.

    Raises:
        ValueError: Если стоимость или срок службы отрицательны или нулевые.
    """
    if cost < 0 or lifespan <= 0:
        raise ValueError("Стоимость и срок службы должны быть положительными!")
    rate = 2 / lifespan  # Коэффициент ускоренной амортизации
    return round(cost * rate, 2)