# Ошибки:
# 1. Использует устаревшую модель (линейная регрессия).
# 2. Нет обработки выбросов.
# 3. Данные в открытом CSV без проверки.
import pandas as pd
from sklearn.linear_model import LinearRegression

def predict_sales(file):
    data = pd.read_csv(file)
    model = LinearRegression()
    model.fit(data[["year"]], data["sales"])
    return model.predict([[2024]])