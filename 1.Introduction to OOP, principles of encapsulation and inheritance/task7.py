class Animal:
    """
    Суперкласс, представляющий животное.

    Атрибуты:
        name (str): Кличка животного.
        species (str): Вид животного.
        legs (int): Количество ног животного.

    Методы:
        voice(): Сообщает, что животное подает голос.
        move(): Сообщает, что животное двигается.
    """

    def __init__(self, name, species, legs):
        """
        Инициализирует объект Animal.

        Args:
            name (str): Кличка животного.
            species (str): Вид животного.
            legs (int): Количество ног животного.
        """
        self.name = name
        self.species = species
        self.legs = legs

    def voice(self):
        """
        Сообщает, что животное подает голос.
        """
        print(f"{self.name} подает голос")

    def move(self):
        """
        Сообщает, что животное двигается.
        """
        print(f"{self.name} дергает хвостом")


class Dog(Animal):
    """
    Подкласс, представляющий собаку.

    Атрибуты:
        breed (str): Порода собаки.

    Методы:
        bark(): Сообщает, что собака лает.
    """

    def __init__(self, name, breed, legs):
        """
        Инициализирует объект Dog.

        Args:
            breed (str): Порода собаки.
        """
        super().__init__(name, "собака", legs)
        self.breed = breed

    def bark(self):
        """
        Сообщает, что собака лает.
        """
        print(f"{self.breed} {self.name} лает")


class Bird(Animal):
    """
    Подкласс, представляющий птицу.

    Атрибуты:
        wingspan (int): Размах крыльев птицы.

    Методы:
        fly(): Сообщает, что птица летает.
    """

    def __init__(self, name, species, legs):
        """
        Инициализирует объект Bird.

        Args:
            wingspan (int): Размах крыльев птицы.
        """
        super().__init__(name, species, legs)
        self.wingspan = 2 * legs  # Пример вычисления размаха крыльев

    def fly(self):
        """
        Сообщает, что птица летает.
        """
        print(f"{self.species} {self.name} летает")


# Пример использования
if __name__ == "__main__":
    dog = Dog("Геральт", "доберман", 4)
    bird = Bird("Вася", "попугай", 2)

    dog.voice()
    bird.voice()

    dog.move()
    bird.move()

    dog.bark()
    bird.fly()