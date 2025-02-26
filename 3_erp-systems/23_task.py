# Ошибки:
# 1. Нет обработки таймаута.
# 2. Возвращает текст вместо JSON.
import requests
def process_payment(amount):
    response = requests.post("https://api.pay.com", json={"amount": amount})
    return response.text