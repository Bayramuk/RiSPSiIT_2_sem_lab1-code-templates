"""
Модуль для построения графика платежей.
"""
import matplotlib.pyplot as plt

def plot_payments(payments: list) -> None:
    """
    Строит график платежей.

    Args:
        payments (list): Список платежей.

    Raises:
        ValueError: Если список платежей пуст.
    """
    if not payments:
        raise ValueError("Список платежей пуст!")
    plt.figure()
    plt.plot(payments, label="Платежи")
    plt.xlabel("Месяц")
    plt.ylabel("Сумма")
    plt.legend()
    plt.savefig("schedule.png")
    plt.close()