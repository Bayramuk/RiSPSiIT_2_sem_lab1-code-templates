"""
Модуль для генерации и проверки OTP-кодов.
"""
import secrets
import time

def generate_otp() -> str:
    """
    Генерирует OTP-код с тайм-аутом.

    Returns:
        str: OTP-код и время истечения в формате "code:expiry".
    """
    code = secrets.token_hex(3)  # 6-значный HEX-код
    expiry = int(time.time()) + 300  # 5 минут действия
    return f"{code}:{expiry}"

def verify_otp(user_input: str, stored_code: str) -> bool:
    """
    Проверяет OTP-код.

    Args:
        user_input (str): Введённый пользователем код.
        stored_code (str): Сохранённый код с временем истечения.

    Returns:
        bool: True, если код верен и не истёк.
    """
    code, expiry = stored_code.split(":")
    return user_input == code and int(expiry) > time.time()