class Recipe:
    """
    Класс, представляющий рецепт блюда.

    Атрибуты:
        name (str): Название блюда.
        ingredients (list): Список ингредиентов.

    Методы:
        print_ingredients(): Выводит список ингредиентов.
        cook(): Сообщает о приготовлении блюда.
    """

    def __init__(self, name, ingredients):
        """
        Инициализирует объект Recipe.

        Args:
            name (str): Название блюда.
            ingredients (list): Список ингредиентов.
        """
        self.name = name
        self.ingredients = ingredients

    def print_ingredients(self):
        """
        Выводит список ингредиентов для блюда.
        """
        print(f"Ингредиенты для {self.name}:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")

    def cook(self):
        """
        Сообщает о приготовлении блюда.
        """
        print(f"Сегодня мы готовим {self.name}.")
        print(f"Выполняем инструкцию по приготовлению блюда {self.name}...")
        print(f"Блюдо {self.name} готово!")


# Пример использования
if __name__ == "__main__":
    # Создаем рецепт спагетти болоньезе
    spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])
    spaghetti.print_ingredients()
    spaghetti.cook()

    # Создаем рецепт для кекса
    cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])
    cake.print_ingredients()
    cake.cook()