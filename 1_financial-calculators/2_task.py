# Ошибки:
# 1. Нет проверки на отрицательную сумму.
# 2. Курс hardcoded, что нарушает гибкость.
# 3. Отсутствует документация.
def convert_currency(amount, rate):
    return amount * 75  # Курс USD/RUB