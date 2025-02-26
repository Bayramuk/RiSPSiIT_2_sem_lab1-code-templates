"""
Модуль для интеграции с платежным шлюзом.
"""
import requests

def process_payment(amount: float) -> dict:
    """
    Обрабатывает платёж через шлюз.

    Args:
        amount (float): Сумма платежа.

    Returns:
        dict: Ответ от шлюза в формате JSON.

    Raises:
        ValueError: Если сумма некорректна.
        ConnectionError: При ошибке запроса.
    """
    if amount <= 0:
        raise ValueError("Сумма платежа должна быть положительной!")
    try:
        response = requests.post("https://api.pay.com", json={"amount": amount}, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise ConnectionError(f"Ошибка запроса к шлюзу: {e}")