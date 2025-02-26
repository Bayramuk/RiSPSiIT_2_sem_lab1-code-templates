# Ошибки:
# 1. Утечка данных в графике (нет очистки).
# 2. Нет легенды и подписей осей.
# 3. Не закрывает файл/график.
import matplotlib.pyplot as plt

def plot_payments(payments):
    plt.plot(payments)
    plt.savefig("schedule.png")