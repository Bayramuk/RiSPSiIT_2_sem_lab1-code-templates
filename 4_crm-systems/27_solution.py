"""
Модуль для анализа рентабельности инвестиций (ROI).
"""

def calculate_roi(revenue: float, cost: float) -> float:
    """
    Рассчитывает ROI (рентабельность инвестиций).

    Args:
        revenue (float): Выручка.
        cost (float): Затраты.

    Returns:
        float: ROI в процентах, округлённый до двух знаков.

    Raises:
        ValueError: Если затраты ≤ 0 или выручка отрицательная.
    """
    if cost <= 0 or revenue < 0:
        raise ValueError("Затраты должны быть > 0, выручка — неотрицательной!")
    roi = ((revenue - cost) / cost) * 100
    return round(roi, 2)