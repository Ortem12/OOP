from abc import ABC, abstractmethod

def validatesoldier(method):
    """
    Декоратор для проверки, что объект является экземпляром класса Soldier.
    
    Аргументы:
        method (callable): Метод, к которому применяется декоратор.
        
    Возвращает:
        callable: Обёрнутый метод с проверкой типа.
        
    Вызывает:
        TypeError: Если объект не является экземпляром Soldier.
    """
    def wrapper(self, *args, **kwargs):
        if not isinstance(self, Soldier):
            raise TypeError("Объект не является солдатом")
        return method(self, *args, **kwargs)
    return wrapper

class Soldier(ABC):
    """
    Абстрактный класс, представляющий солдата.
    
    Все подклассы должны реализовать методы:
    - move(): Способ передвижения
    - attack(): Способ атаки
    - defend(): Способ защиты
    """
    
    @abstractmethod
    def move(self):
        """Абстрактный метод для передвижения солдата."""
        pass
    
    @abstractmethod
    def attack(self):
        """Абстрактный метод для атаки солдата."""
        pass
    
    @abstractmethod
    def defend(self):
        """Абстрактный метод для защиты солдата."""
        pass

class Infantry(Soldier):
    """
    Класс пехоты. Реализует методы движения, атаки и защиты.
    
    Методы:
    - move(): Передвижение в пешем порядке
    - attack(): Ближний бой
    - defend(): Удержание строя
    """
    
    @validatesoldier
    def move(self):
        """Передвигается пешком."""
        print("Пехота передвигается в пешем порядке")
    
    @validatesoldier
    def attack(self):
        """Атакует в ближнем бою."""
        print("Пехота участвует в ближнем бою")
    
    @validatesoldier
    def defend(self):
        """Защищает позицию."""
        print("Пехота держит строй")

class Cavalry(Soldier):
    """
    Класс кавалерии. Реализует методы движения, атаки и защиты.
    
    Методы:
    - move(): Передвижение верхом
    - attack(): Атака с коня
    - defend(): Защита флангов
    """
    
    @validatesoldier
    def move(self):
        """Передвигается верхом."""
        print("Кавалерия передвигается верхом")
    
    @validatesoldier
    def attack(self):
        """Атакует с использованием коня."""
        print("Кавалерия переходит в атаку")
    
    @validatesoldier
    def defend(self):
        """Защищает фланги армии."""
        print("Кавалерия защищает фланги")

class Army:
    """
    Класс для управления армией солдат.
    
    Методы:
    - add_soldier(soldier): Добавляет солдата в армию
    - attack(): Координирует атаку всех солдат
    - defend(): Организует защиту всех солдат
    """
    
    def __init__(self):
        """Инициализирует армию с пустым списком солдат."""
        self.soldiers = []
    
    def add_soldier(self, soldier):
        """
        Добавляет солдата в армию.
        
        Аргументы:
            soldier (Soldier): Экземпляр Soldier для добавления.
            
        Вызывает:
            TypeError: Если объект не является Soldier.
        """
        if not isinstance(soldier, Soldier):
            raise TypeError("Можно добавлять только солдат")
        self.soldiers.append(soldier)
    
    def attack(self):
        """Организует последовательную атаку всех солдат."""
        for soldier in self.soldiers:
            soldier.move()
            soldier.attack()
    
    def defend(self):
        """Организует последовательную защиту всех солдат."""
        for soldier in self.soldiers:
            soldier.move()
            soldier.defend()

# Пример использования
if __name__ == "__main__":
    army = Army()
    army.add_soldier(Infantry())
    army.add_soldier(Cavalry())
    army.add_soldier(Infantry())
    army.add_soldier(Cavalry())

    army.attack()
    army.defend()