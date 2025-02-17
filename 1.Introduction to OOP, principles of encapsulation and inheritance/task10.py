def character_info_decorator(cls):
    """
    Декоратор для вывода информации о создании персонажа.
    """
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print(f"Создан новый игровой персонаж типа {cls.__name__} с атрибутами: {instance.__dict__}")
        return instance
    return wrapper


@character_info_decorator
class Soldier:
    """
    Класс, представляющий солдата.

    Атрибуты:
        name (str): Имя солдата.
        __rank (str): Воинское звание (приватный).
        __service_number (str): Порядковый номер (приватный).

    Методы:
        get_rank(): Возвращает воинское звание.
        verify_service_number(): Подтверждает порядковый номер.
        promote(): Повышает в звании.
        demote(): Понижает в звании.
    """

    RANKS = ["рядовой", "ефрейтор", "младший сержант", "сержант", "старший сержант"]

    def __init__(self, name, rank, service_number):
        """
        Инициализирует объект Soldier.

        Args:
            name (str): Имя солдата.
            rank (str): Воинское звание.
            service_number (str): Порядковый номер.
        """
        self.name = name
        self.__rank = rank
        self.__service_number = service_number

    def get_rank(self):
        """
        Возвращает воинское звание.

        Returns:
            str: Воинское звание.
        """
        print(f"Персонаж {self.name} имеет звание {self.__rank}")
        return self.__rank

    def verify_service_number(self):
        """
        Подтверждает порядковый номер.

        Returns:
            str: Порядковый номер.
        """
        print(f"Порядковый номер {self.name}: {self.__service_number}")
        return self.__service_number

    def promote(self):
        """
        Повышает солдата в звании.
        """
        current_index = self.RANKS.index(self.__rank)
        if current_index < len(self.RANKS) - 1:
            self.__rank = self.RANKS[current_index + 1]
            print(f"{self.name} повышен в звании, он теперь {self.__rank}")
        else:
            print(f"{self.name} уже имеет высшее звание: {self.__rank}")

    def demote(self):
        """
        Понижает солдата в звании.
        """
        current_index = self.RANKS.index(self.__rank)
        if current_index > 0:
            self.__rank = self.RANKS[current_index - 1]
            print(f"{self.name} понижен в звании, он теперь {self.__rank}")
        else:
            print(f"{self.name} уже имеет низшее звание: {self.__rank}")


# Пример использования
if __name__ == "__main__":
    soldier1 = Soldier("Иван Сусанин", "рядовой", "12345")
    soldier1.get_rank()
    soldier1.promote()
    soldier1.demote()