# Ошибки:
# 1. Использует простые проценты вместо сложных.
# 2. Нет проверки на отрицательный срок.
# 3. Не округляет результат.
def calculate_profit(principal, rate, years):
    return principal * rate * years