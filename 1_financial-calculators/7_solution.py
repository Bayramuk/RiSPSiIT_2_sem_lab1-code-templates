"""
Модуль для расчёта себестоимости товара.
"""
import os

def calculate_cost(materials: list, labor: float) -> float:
    """
    Рассчитывает себестоимость товара.

    Args:
        materials (list): Список затрат на материалы.
        labor (float): Затраты на рабочую силу.

    Returns:
        float: Себестоимость, округлённая до двух знаков.

    Raises:
        ValueError: Если список материалов пуст или затраты отрицательны.
    """
    if not materials or labor < 0:
        raise ValueError("Материалы не могут быть пустыми, а затраты — отрицательными!")
    api_key = os.getenv("API_KEY")  # Ключ хранится в переменных окружения
    return round(sum(materials) + labor, 2)