"""
Модуль для генерации налогового отчёта в формате CSV.
"""
import csv

def generate_tax_report(data: list) -> None:
    """
    Генерирует CSV-отчёт по налогам.

    Args:
        data (list): Список кортежей (user_id, income).

    Raises:
        ValueError: Если данные пусты.
    """
    if not data:
        raise ValueError("Нет данных для отчёта!")
    with open("report.csv", "w", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["User", "Income", "Tax"])
        for row in data:
            writer.writerow([row[0], row[1], round(row[1] * 0.13, 2)])