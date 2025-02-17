class Wine:
    """
    Базовый класс для представления вина.

    Атрибуты:
        name (str): Название вина.
        grape (str): Сорт винограда.
        year (int): Год производства.
    """

    def __init__(self, name, grape, year):
        self.name = name
        self.grape = grape
        self.year = year

    def serve(self):
        """
        Метод для рекомендации температуры подачи вина.
        Должен быть переопределен в подклассах.
        """
        raise NotImplementedError("Метод serve() должен быть переопределен в подклассе")


class RedWine(Wine):
    """
    Подкласс для представления красного вина.

    Методы:
        serve(): Рекомендация по подаче красного вина.
    """

    def serve(self):
        print(f"Красное вино '{self.name}', сделанное из винограда сорта {self.grape} "
              f"в {self.year} году, рекомендуем подавать комнатной температуры.")


class WhiteWine(Wine):
    """
    Подкласс для представления белого вина.

    Методы:
        serve(): Рекомендация по подаче белого вина.
    """

    def serve(self):
        print(f"Белое вино '{self.name}', сделанное из винограда сорта {self.grape} "
              f"в {self.year} году, рекомендуем подавать хорошо охлажденным.")


class RoseWine(Wine):
    """
    Подкласс для представления розового вина.

    Методы:
        serve(): Рекомендация по подаче розового вина.
    """

    def serve(self):
        print(f"Розовое вино '{self.name}', сделанное из винограда сорта {self.grape} "
              f"в {self.year} году, рекомендуем подавать слегка охлажденным.")


class Winery:
    """
    Класс для управления списком вин.

    Атрибуты:
        wines (list): Список вин.
    """

    def __init__(self):
        self.wines = []

    def add_wine(self, wine):
        """
        Добавляет вино в список.

        Аргументы:
            wine (Wine): Экземпляр вина.
        """
        self.wines.append(wine)

    def serve_wines(self):
        """
        Вызывает метод serve() для каждого вина в списке.
        """
        for wine in self.wines:
            wine.serve()


# Пример использования
winery = Winery()
winery.add_wine(RedWine("Cabernet Sauvignon", "Каберне Совиньон", 2015))
winery.add_wine(WhiteWine("Chardonnay", "Шардоне", 2018))
winery.add_wine(RoseWine("Grenache", "Гренаш", 2020))
winery.serve_wines()