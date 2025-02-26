"""
Модуль для прогнозирования продаж.
"""
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def predict_sales(file: str) -> float:
    """
    Прогнозирует продажи на 2024 год.

    Args:
        file (str): Путь к CSV-файлу с данными (столбцы: year, sales).

    Returns:
        float: Прогноз продаж, округлённый до двух знаков.

    Raises:
        ValueError: Если данные некорректны.
    """
    data = pd.read_csv(file)
    if data.empty:
        raise ValueError("Данные отсутствуют!")
    data = data[(data["sales"] > 0) & (data["sales"] < 1e6)]  # Удаление выбросов
    X_train, _, y_train, _ = train_test_split(data[["year"]], data["sales"], test_size=0.2)
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    return round(model.predict([[2024]])[0], 2)