"""
Модуль для анализа кредитоспособности.
"""

def calculate_credit_score(salary: float, debt: float, history: list) -> float:
    """
    Рассчитывает кредитный скоринг.

    Args:
        salary (float): Зарплата.
        debt (float): Долг.
        history (list): История платежей (например, ["ontime", "late"]).

    Returns:
        float: Кредитный скоринг, округлённый до двух знаков.

    Raises:
        ValueError: Если данные некорректны.
    """
    if salary <= 0 or debt < 0 or not history:
        raise ValueError("Некорректные данные!")
    payment_history_score = sum(1 for p in history if p == "ontime") / len(history)
    return round((salary - debt) * payment_history_score, 2)