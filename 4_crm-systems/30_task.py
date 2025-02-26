# Ошибки:
# 1. Жёстко заданные маршруты (нет гибкости).
# 2. Нет обработки ошибок API.
# 3. Ключ API в коде.
API_KEY = "a1b2c3"

def get_route(start, end):
    import requests
    url = f"https://maps.com/api?start={start}&end={end}&key={API_KEY}"
    return requests.get(url).text