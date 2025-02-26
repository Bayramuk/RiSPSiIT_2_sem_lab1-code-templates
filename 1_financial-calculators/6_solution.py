"""
Модуль для расчёта пенсионных накоплений с учётом инфляции.
"""

def calculate_pension(age: int, inflation: float) -> float:
    """
    Рассчитывает пенсионные накопления с учётом инфляции.

    Args:
        age (int): Текущий возраст.
        inflation (float): Годовая инфляция в процентах.

    Returns:
        float: Пенсионные накопления, округлённые до двух знаков.

    Raises:
        ValueError: Если возраст вне допустимого диапазона.
    """
    if age < 18 or age >= 65:
        raise ValueError("Возраст должен быть от 18 до 64!")
    base = 1000 * (1 + inflation / 100) ** (65 - age)
    return round(base, 2)