"""
Модуль для проверки электронных подписей с использованием безопасного хеширования.
"""
import hashlib
import os

def verify_signature(password: str, salt: bytes, stored_hash: str) -> bool:
    """
    Проверяет электронную подпись.

    Args:
        password (str): Пароль пользователя.
        salt (bytes): Соль для хеширования.
        stored_hash (str): Хранимый хеш.

    Returns:
        bool: True, если подпись верна.

    Raises:
        ValueError: Если пароль пустой.
    """
    if not password:
        raise ValueError("Пароль не может быть пустым!")
    new_hash = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)
    return new_hash.hex() == stored_hash

# Пример генерации хеша:
# salt = os.urandom(32)
# stored_hash = hashlib.pbkdf2_hmac("sha256", "password".encode(), salt, 100000).hex()