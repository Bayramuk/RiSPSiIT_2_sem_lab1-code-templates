"""
Модуль для перевода средств между счетами.
"""

class BankAccount:
    def __init__(self, initial_balance: float):
        """
        Инициализирует банковский счёт.

        Args:
            initial_balance (float): Начальный баланс.
        """
        if initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным!")
        self.balance = initial_balance

    def transfer(self, amount: float) -> float:
        """
        Переводит средства с одного счёта.

        Args:
            amount (float): Сумма перевода.

        Returns:
            float: Новый баланс.

        Raises:
            ValueError: Если недостаточно средств или сумма перевода некорректна.
        """
        if amount <= 0:
            raise ValueError("Сумма перевода должна быть положительной!")
        if amount > self.balance:
            raise ValueError("Недостаточно средств!")
        self.balance -= amount
        return self.balance