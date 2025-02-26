# Ошибки:
# 1. Использует простые проценты вместо аннуитетной формулы.
# 2. Нет проверки на нулевую ставку.
# 3. Отсутствует документация.
def calculate_payment(principal, rate, months):
    return (principal * rate / 100) / months