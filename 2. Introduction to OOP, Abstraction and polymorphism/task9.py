def performance_test_decorator(func):
    """
    Декоратор для вывода сообщений о начале и завершении теста производительности.
    
    Аргументы:
        func (callable): Метод, который нужно обернуть.
        
    Возвращает:
        callable: Обёрнутый метод с выводом сообщений.
    """
    def wrapper(*args, **kwargs):
        print("Начинаем тест производительности...")
        result = func(*args, **kwargs)
        print("Тест производительности завершен.")
        return result
    return wrapper

class Computer:
    """
    Базовый класс для представления компьютера.
    
    Атрибуты:
        model (str): Модель компьютера.
        processor (str): Процессор компьютера.
        memory (str): Объем оперативной памяти.
    """
    
    def __init__(self, model: str, processor: str, memory: str):
        self.model = model
        self.processor = processor
        self.memory = memory
    
    @performance_test_decorator
    def run(self):
        """
        Метод для запуска теста производительности.
        Должен быть переопределен в подклассах.
        """
        raise NotImplementedError("Метод run() должен быть переопределен в подклассах")

class Desktop(Computer):
    """
    Класс для настольных компьютеров.
    Наследует атрибуты и методы класса Computer.
    """
    
    def run(self):
        """
        Запускает тест производительности для настольного компьютера.
        """
        print(f"Запускаем настольный компьютер '{self.model}' с процессором {self.processor} и {self.memory} RAM.")

class Laptop(Computer):
    """
    Класс для ноутбуков.
    Наследует атрибуты и методы класса Computer.
    """
    
    def run(self):
        """
        Запускает тест производительности для ноутбука.
        """
        print(f"Запускаем ноутбук '{self.model}' с процессором {self.processor} и {self.memory} RAM.")

class ComputerStore:
    """
    Класс для управления коллекцией компьютеров.
    
    Методы:
        add_computer(computer: Computer) -> None: Добавляет компьютер в коллекцию.
        run_tests() -> None: Запускает тесты производительности для всех компьютеров.
    """
    
    def __init__(self):
        self.computers = []
    
    def add_computer(self, computer: Computer) -> None:
        """
        Добавляет компьютер в коллекцию.
        
        Аргументы:
            computer (Computer): Экземпляр класса Computer или его подклассов.
        """
        self.computers.append(computer)
    
    def run_tests(self) -> None:
        """
        Запускает тесты производительности для всех компьютеров в коллекции.
        """
        for computer in self.computers:
            computer.run()

# Пример использования
store = ComputerStore()
store.add_computer(Desktop("HP Legion", "Intel Core i9-10900K", "64 Гб"))
store.add_computer(Laptop("Dell Xtra", "Intel Core i5 13600K", "32 Гб"))
store.add_computer(Desktop("Lenovo SuperPad", "AMD Ryzen 7 2700X", "16 Гб"))

store.run_tests()