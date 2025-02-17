from abc import ABC, abstractmethod

class Ingredient(ABC):
    """
    Абстрактный класс, представляющий ингредиент.
    Этот класс должен быть унаследован подклассами, которые представляют конкретные ингредиенты.
    """

    @abstractmethod
    def get_name(self):
        """
        Абстрактный метод для получения названия ингредиента.
        """
        pass

    @abstractmethod
    def get_quantity(self):
        """
        Абстрактный метод для получения количества ингредиента.
        """
        pass

class Vegetable(Ingredient):
    """
    Класс, представляющий овощ. Наследует абстрактный класс Ingredient.
    """

    def __init__(self, name, quantity):
        """
        Инициализация объекта Vegetable.

        Параметры:
        - name (str): Название овоща.
        - quantity (int): Количество овоща в килограммах.
        """
        self.name = name
        self.quantity = quantity

    def get_name(self):
        """
        Возвращает название овоща.

        Возвращает:
        - str: Название овоща.
        """
        return self.name

    def get_quantity(self):
        """
        Возвращает количество овоща.

        Возвращает:
        - str: Количество овоща в килограммах.
        """
        return f"{self.quantity} кг"

class Fruit(Ingredient):
    """
    Класс, представляющий фрукт. Наследует абстрактный класс Ingredient.
    """

    def __init__(self, name, quantity):
        """
        Инициализация объекта Fruit.

        Параметры:
        - name (str): Название фрукта.
        - quantity (int): Количество фрукта в килограммах.
        """
        self.name = name
        self.quantity = quantity

    def get_name(self):
        """
        Возвращает название фрукта.

        Возвращает:
        - str: Название фрукта.
        """
        return self.name

    def get_quantity(self):
        """
        Возвращает количество фрукта.

        Возвращает:
        - str: Количество фрукта в килограммах.
        """
        return f"{self.quantity} кг"

# Пример использования
carrot = Vegetable("Морковь", 5)
apple = Fruit("Яблоки", 10)

print(carrot.get_name())
print(carrot.get_quantity())

print(apple.get_name())
print(apple.get_quantity())