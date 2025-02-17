from abc import ABC, abstractmethod

class Starship(ABC):
    """
    Абстрактный класс для представления звездолета.

    Методы:
        warp_speed(): Перемещение на варп-скорости.
        fire_weapon(): Атака оружием.
        self_destruct(): Активация системы самоуничтожения.
    """

    @abstractmethod
    def warp_speed(self):
        """Активировать варп-двигатель."""
        pass

    @abstractmethod
    def fire_weapon(self):
        """Атаковать оружием."""
        pass

    @abstractmethod
    def self_destruct(self):
        """Активировать систему самоуничтожения."""
        pass


class FederationStarship(Starship):
    """
    Подкласс для представления звездолета Федерации.

    Методы:
        warp_speed(): Перемещение на варп-скорости.
        fire_weapon(): Атака фазерами.
        self_destruct(): Активация системы самоуничтожения.
    """

    def warp_speed(self):
        print("Включить варп-двигатели!")

    def fire_weapon(self):
        print("Стрелять из фазеров!")

    def self_destruct(self):
        print("Запускаю систему самоуничтожения...")


class KlingonWarship(Starship):
    """
    Подкласс для представления клингонского боевого корабля.

    Методы:
        warp_speed(): Перемещение на варп-скорости с маскировкой.
        fire_weapon(): Атака фотонными торпедами.
        self_destruct(): Активация протокола самоуничтожения.
    """

    def warp_speed(self):
        print("Включить маскировочное устройство!")

    def fire_weapon(self):
        print("Выпустить фотонные торпеды!")

    def self_destruct(self):
        print("Запускаю протокол самоуничтожения...")


# Пример использования
enterprise = FederationStarship()
bird_of_prey = KlingonWarship()

enterprise.warp_speed()
bird_of_prey.warp_speed()

enterprise.fire_weapon()
bird_of_prey.fire_weapon()

enterprise.self_destruct()
bird_of_prey.self_destruct()