# Ошибки:
# 1. Неправильный формат JSON (строка вместо объекта).
# 2. Нет обработки пустого списка.
transactions = [{"id": 1, "amount": 100}]
def generate_report():
    return "{'transactions': transactions}"