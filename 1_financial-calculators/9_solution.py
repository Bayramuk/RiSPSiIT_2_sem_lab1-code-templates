"""
Модуль для расчёта бонусов сотрудников с учётом KPI.
"""

def calculate_bonus(salary: float, kpi: float) -> float:
    """
    Рассчитывает бонус сотрудника на основе KPI.

    Args:
        salary (float): Зарплата сотрудника.
        kpi (float): KPI сотрудника (от 0 до 1).

    Returns:
        float: Бонус, округлённый до двух знаков.

    Raises:
        ValueError: Если KPI вне диапазона [0, 1] или зарплата отрицательная.
    """
    if kpi < 0 or kpi > 1 or salary < 0:
        raise ValueError("KPI должен быть от 0 до 1, а зарплата — положительной!")
    return round(salary * 0.1 * kpi, 2)