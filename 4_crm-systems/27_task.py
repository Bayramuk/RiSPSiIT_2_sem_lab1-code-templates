# Ошибки:
# 1. Неверная формула ROI.
# 2. Нет обработки деления на ноль.
# 3. Логирование конфиденциальных данных.
def calculate_roi(revenue, cost):
    roi = (revenue / cost) * 100
    print(f"ROI для revenue={revenue}, cost={cost}: {roi}%")
    return roi