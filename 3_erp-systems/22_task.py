# Ошибки:
# 1. Неверный расчёт НДФЛ (без учёта вычетов).
# 2. Нет проверки на отрицательную зарплату.
# 3. Пароль в коде (здесь опущен, но подразумевается).
TAX_RATE = 0.13
DB_PASSWORD = "admin123"

def calculate_salary(gross):
    tax = gross * TAX_RATE
    return gross - tax