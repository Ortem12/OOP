import math

class Shape:
    """
    Суперкласс, представляющий геометрическую фигуру.

    Атрибуты:
        name (str): Название фигуры.
        color (str): Цвет фигуры.

    Методы:
        describe(): Описывает фигуру.
    """

    def __init__(self, color):
        """
        Инициализирует объект Shape.

        Args:
            color (str): Цвет фигуры.
        """
        self.color = color

    def describe(self):
        """
        Описывает фигуру.
        """
        print(f"Это геометрическая фигура, цвет - {self.color}.")


class Circle(Shape):
    """
    Подкласс, представляющий окружность.

    Атрибуты:
        radius (float): Радиус окружности.

    Методы:
        area(): Вычисляет площадь окружности.
        describe(): Описывает окружность.
    """

    def __init__(self, color, radius):
        """
        Инициализирует объект Circle.

        Args:
            radius (float): Радиус окружности.
        """
        super().__init__(color)
        self.radius = radius

    def area(self):
        """
        Вычисляет площадь окружности.

        Returns:
            float: Площадь окружности.
        """
        return round(math.pi * self.radius**2, 1)

    def describe(self):
        """
        Описывает окружность.
        """
        print(f"Это окружность. Радиус - {self.radius} см, цвет - {self.color}.")


class Rectangle(Shape):
    """
    Подкласс, представляющий прямоугольник.

    Атрибуты:
        length (float): Длина прямоугольника.
        width (float): Ширина прямоугольника.

    Методы:
        area(): Вычисляет площадь прямоугольника.
        describe(): Описывает прямоугольник.
    """

    def __init__(self, color, length, width):
        """
        Инициализирует объект Rectangle.

        Args:
            length (float): Длина прямоугольника.
            width (float): Ширина прямоугольника.
        """
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Returns:
            float: Площадь прямоугольника.
        """
        return self.length * self.width

    def describe(self):
        """
        Описывает прямоугольник.
        """
        print(f"Это {self.color} прямоугольник. Длина - {self.length} см, ширина - {self.width} см.")


class Triangle(Shape):
    """
    Подкласс, представляющий треугольник.

    Атрибуты:
        base (float): Основание треугольника.
        height (float): Высота треугольника.

    Методы:
        area(): Вычисляет площадь треугольника.
        describe(): Описывает треугольник.
    """

    def __init__(self, color, base, height):
        """
        Инициализирует объект Triangle.

        Args:
            base (float): Основание треугольника.
            height (float): Высота треугольника.
        """
        super().__init__(color)
        self.base = base
        self.height = height

    def area(self):
        """
        Вычисляет площадь треугольника.

        Returns:
            float: Площадь треугольника.
        """
        return (self.base * self.height) / 2

    def describe(self):
        """
        Описывает треугольник.
        """
        print(f"Это {self.color} треугольник с основанием {self.base} см и высотой {self.height} см.")


# Пример использования
if __name__ == "__main__":
    circle = Circle("красный", 5)
    rectangle = Rectangle("синий", 3, 4)
    triangle = Triangle("фиолетовый", 6, 8)

    circle.describe()
    rectangle.describe()
    triangle.describe()

    print(f"Площадь треугольника {triangle.area()}, окружности {circle.area()}, прямоугольника {rectangle.area()} см.")