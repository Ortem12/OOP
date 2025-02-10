class BankAccount:
    """
    Класс, представляющий банковский счет.

    Атрибуты:
        __balance (float): Текущий баланс счета (приватный).
        __interest_rate (float): Процентная ставка (приватный).
        __transactions (list): Список всех операций по счету (приватный).

    Методы:
        deposit(amount): Вносит сумму на счет и регистрирует транзакцию.
        withdraw(amount): Снимает сумму со счета и регистрирует транзакцию.
        add_interest(): Начисляет проценты на счет и регистрирует транзакцию.
        history(): Выводит историю всех операций по счету.
    """

    def __init__(self, balance, interest_rate):
        """
        Инициализирует объект BankAccount.

        Args:
            balance (float): Начальный баланс счета.
            interest_rate (float): Процентная ставка.
        """
        self.__balance = balance
        self.__interest_rate = interest_rate
        self.__transactions = []

    def deposit(self, amount):
        """
        Вносит сумму на счет и регистрирует транзакцию.

        Args:
            amount (float): Сумма для внесения.
        """
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f"Внесение наличных на счет: {amount}")
        else:
            print("Ошибка: Сумма для внесения должна быть положительной.")

    def withdraw(self, amount):
        """
        Снимает сумму со счета и регистрирует транзакцию.

        Args:
            amount (float): Сумма для снятия.
        """
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(f"Снятие наличных: {amount}")
        else:
            print("Ошибка: Недостаточно средств на счете или сумма для снятия некорректна.")

    def add_interest(self):
        """
        Начисляет проценты на счет и регистрирует транзакцию.
        """
        interest = self.__balance * self.__interest_rate
        self.__balance += interest
        self.__transactions.append(f"Начислены проценты по вкладу: {interest}")

    def history(self):
        """
        Выводит историю всех операций по счету.
        """
        for transaction in self.__transactions:
            print(transaction)


# Пример использования
if __name__ == "__main__":
    # Создаем объект счета с балансом 100000 и процентом по вкладу 0.05
    account = BankAccount(100000, 0.05)

    # Вносим 15 тысяч на счет
    account.deposit(15000)

    # Снимаем 7500 рублей
    account.withdraw(7500)

    # Начисляем проценты по вкладу
    account.add_interest()

    # Печатаем историю операций
    account.history()