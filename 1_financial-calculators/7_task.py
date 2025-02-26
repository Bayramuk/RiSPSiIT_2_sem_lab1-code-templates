# Ошибки:
# 1. Утечка данных в логах (выводит API_KEY).
# 2. Нет обработки нулевых значений.
# 3. Секретный ключ в коде.
API_KEY = "sk_12345"

def calculate_cost(materials, labor):
    print(f"Расчёт для API_KEY={API_KEY}")
    return sum(materials) + labor