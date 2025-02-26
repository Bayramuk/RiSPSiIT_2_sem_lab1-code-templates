# Ошибки:
# 1. Жёсткая упрощённая логика.
# 2. Нет нормализации данных.
# 3. Возвращает int вместо float.
def calculate_credit_score(salary, debt):
    return salary - debt