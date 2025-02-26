"""
Модуль для проверки валидности IBAN.
"""

def validate_iban(iban: str) -> bool:
    """
    Проверяет валидность IBAN.

    Args:
        iban (str): IBAN-код.

    Returns:
        bool: True, если IBAN валиден.

    Raises:
        ValueError: Если IBAN пустой.
    """
    if not iban:
        raise ValueError("IBAN не может быть пустым!")
    iban = iban.upper().replace(" ", "")
    if len(iban) != 20 or not iban.startswith("RU"):
        return False
    # Здесь должна быть полная проверка контрольной суммы IBAN
    return True