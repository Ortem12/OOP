class Aircraft:
    """
    Базовый класс для представления воздушного судна.

    Атрибуты:
        model (str): Модель самолета.
        manufacturer (str): Производитель самолета.
        capacity (int): Вместимость (для пассажирских) или грузоподъемность (для грузовых).
    """

    def __init__(self, model, manufacturer, capacity):
        self.model = model
        self.manufacturer = manufacturer
        self.capacity = capacity

    def fly(self):
        """
        Метод для имитации взлета самолета.
        Должен быть переопределен в подклассах.
        """
        raise NotImplementedError("Метод fly() должен быть переопределен в подклассе")


class PassengerAircraft(Aircraft):
    """
    Подкласс для представления пассажирского самолета.

    Методы:
        fly(): Имитация взлета пассажирского самолета.
    """

    def fly(self):
        print(f"Пассажирский самолет '{self.model}' вместимостью {self.capacity} человек, "
              f"произведенный компанией {self.manufacturer}, поднимается в воздух с пассажирами на борту.")


class CargoAircraft(Aircraft):
    """
    Подкласс для представления грузового самолета.

    Методы:
        fly(): Имитация взлета грузового самолета.
    """

    def fly(self):
        print(f"Грузовой самолет '{self.model}' с грузоподъемностью {self.capacity} т, "
              f"произведенный компанией {self.manufacturer}, поднимается в воздух с грузом на борту.")


class Airport:
    """
    Класс для управления списком самолетов.

    Атрибуты:
        aircrafts (list): Список самолетов.
    """

    def __init__(self):
        self.aircrafts = []

    def add_aircraft(self, aircraft):
        """
        Добавляет самолет в список.

        Аргументы:
            aircraft (Aircraft): Экземпляр самолета.
        """
        self.aircrafts.append(aircraft)

    def takeoff(self):
        """
        Вызывает метод fly() для каждого самолета в списке.
        """
        for aircraft in self.aircrafts:
            aircraft.fly()


# Пример использования
airport = Airport()
airport.add_aircraft(PassengerAircraft("Boeing 747", "Боинг", 416))
airport.add_aircraft(CargoAircraft("Airbus A330", "Эйрбас", 70))
airport.add_aircraft(PassengerAircraft("Boeing 777", "Боинг", 396))
airport.takeoff()