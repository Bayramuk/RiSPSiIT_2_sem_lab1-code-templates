# Ошибки:
# 1. Нет проверки на отрицательный баланс.
# 2. Использует глобальную переменную.
# 3. Отсутствуют аннотации типов.
balance = 1000

def transfer(amount):
    global balance
    balance -= amount
    return balance