"""
Модуль для расчёта логистических маршрутов через API.
"""
import requests
import os

def get_route(start: str, end: str) -> dict:
    """
    Получает оптимальный маршрут через API.

    Args:
        start (str): Начальная точка.
        end (str): Конечная точка.

    Returns:
        dict: Данные маршрута в формате JSON.

    Raises:
        ValueError: Если точки пустые.
        ConnectionError: При ошибке API.
    """
    if not start or not end:
        raise ValueError("Точки маршрута не могут быть пустыми!")
    api_key = os.getenv("MAPS_API_KEY")
    try:
        response = requests.get(
            "https://maps.com/api",
            params={"start": start, "end": end, "key": api_key},
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise ConnectionError(f"Ошибка API: {e}")