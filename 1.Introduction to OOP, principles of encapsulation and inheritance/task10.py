class Candy:
    """
    Суперкласс, представляющий конфеты.

    Атрибуты:
        name (str): Название конфет.
        price (float): Цена конфет.
        weight (float): Вес конфет.
    """

    def __init__(self, name, price, weight):
        """
        Инициализирует объект Candy.

        Args:
            name (str): Название конфет.
            price (float): Цена конфет.
            weight (float): Вес конфет.
        """
        self.name = name
        self.price = price
        self.weight = weight


class Chocolate(Candy):
    """
    Подкласс, представляющий шоколадные конфеты.

    Атрибуты:
        cocoa_percentage (float): Процент содержания какао.
        chocolate_type (str): Тип шоколада.
    """

    def __init__(self, name, price, weight, cocoa_percentage, chocolate_type):
        """
        Инициализирует объект Chocolate.

        Args:
            cocoa_percentage (float): Процент содержания какао.
            chocolate_type (str): Тип шоколада.
        """
        super().__init__(name, price, weight)
        self.cocoa_percentage = cocoa_percentage
        self.chocolate_type = chocolate_type


class Gummy(Candy):
    """
    Подкласс, представляющий жевательный мармелад.

    Атрибуты:
        flavor (str): Вкус мармелада.
        shape (str): Форма мармелада.
    """

    def __init__(self, name, price, weight, flavor, shape):
        """
        Инициализирует объект Gummy.

        Args:
            flavor (str): Вкус мармелада.
            shape (str): Форма мармелада.
        """
        super().__init__(name, price, weight)
        self.flavor = flavor
        self.shape = shape


class HardCandy(Candy):
    """
    Подкласс, представляющий леденцы.

    Атрибуты:
        flavor (str): Вкус леденца.
        filled (bool): Наличие начинки.
    """

    def __init__(self, name, price, weight, flavor, filled):
        """
        Инициализирует объект HardCandy.

        Args:
            flavor (str): Вкус леденца.
            filled (bool): Наличие начинки.
        """
        super().__init__(name, price, weight)
        self.flavor = flavor
        self.filled = filled


# Пример использования
if __name__ == "__main__":
    chocolate = Chocolate(name="Швейцарские луга", price=325.50, weight=220, cocoa_percentage=40, chocolate_type="молочный")
    gummy = Gummy(name="Жуй-жуй", price=76.50, weight=50, flavor="вишня", shape="медведь")
    hard_candy = HardCandy(name="Crazy Фрукт", price=35.50, weight=25, flavor="манго", filled=True)

    print("Шоколадные конфеты:")
    print(f"Название конфет: {chocolate.name}")
    print(f"Стоимость: {chocolate.price} руб")
    print(f"Вес брутто: {chocolate.weight} г")
    print(f"Процент содержания какао: {chocolate.cocoa_percentage}")
    print(f"Тип шоколада: {chocolate.chocolate_type}")

    print("\nМармелад жевательный:")
    print(f"Название конфет: {gummy.name}")
    print(f"Стоимость: {gummy.price} руб")
    print(f"Вес брутто: {gummy.weight} г")
    print(f"Вкус: {gummy.flavor}")
    print(f"Форма: {gummy.shape}")

    print("\nФруктовые леденцы:")
    print(f"Название конфет: {hard_candy.name}")
    print(f"Стоимость: {hard_candy.price} руб")
    print(f"Вес брутто: {hard_candy.weight} г")
    print(f"Вкус: {hard_candy.flavor}")
    print(f"Начинка: {hard_candy.filled}")