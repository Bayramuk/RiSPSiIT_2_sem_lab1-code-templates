# Ошибки:
# 1. Генерация слабого 4-значного кода.
# 2. Нет тайм-аута действия кода.
# 3. Код выводится в логи.
import random

def generate_otp():
    code = random.randint(1000, 9999)
    print(f"Ваш код: {code}")
    return code