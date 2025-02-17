from abc import ABC, abstractmethod

class Dinosaur(ABC):
    """
    Абстрактный класс, представляющий динозавра.
    Все подклассы должны реализовать методы:
    - get_personal_name(): Возвращает имя динозавра.
    - get_breed(): Возвращает вид динозавра.
    - get_height(): Возвращает рост динозавра.
    - get_weight(): Возвращает вес динозавра.
    - get_diet(): Возвращает рацион питания динозавра.
    """

    @abstractmethod
    def get_personal_name(self):
        """Абстрактный метод для получения имени динозавра."""
        pass

    @abstractmethod
    def get_breed(self):
        """Абстрактный метод для получения вида динозавра."""
        pass

    @abstractmethod
    def get_height(self):
        """Абстрактный метод для получения роста динозавра."""
        pass

    @abstractmethod
    def get_weight(self):
        """Абстрактный метод для получения веса динозавра."""
        pass

    @abstractmethod
    def get_diet(self):
        """Абстрактный метод для получения рациона питания динозавра."""
        pass

class Carnivore(Dinosaur):
    """
    Класс, представляющий плотоядного динозавра.
    Наследует абстрактный класс Dinosaur.
    """

    def __init__(self, breed, personal_name, weight, height):
        """
        Инициализация объекта Carnivore.

        Параметры:
        - breed (str): Вид динозавра.
        - personal_name (str): Имя динозавра.
        - weight (int): Вес динозавра в кг.
        - height (int): Рост динозавра в см.
        """
        self.breed = breed
        self.personal_name = personal_name
        self.weight = weight
        self.height = height

    def get_personal_name(self):
        """Возвращает имя динозавра."""
        return self.personal_name

    def get_breed(self):
        """Возвращает вид динозавра."""
        return self.breed

    def get_height(self):
        """Возвращает рост динозавра."""
        return self.height

    def get_weight(self):
        """Возвращает вес динозавра."""
        return self.weight

    def get_diet(self):
        """Возвращает рацион питания динозавра."""
        return "Плотоядный"

class Herbivore(Dinosaur):
    """
    Класс, представляющий травоядного динозавра.
    Наследует абстрактный класс Dinosaur.
    """

    def __init__(self, breed, personal_name, weight, height):
        """
        Инициализация объекта Herbivore.

        Параметры:
        - breed (str): Вид динозавра.
        - personal_name (str): Имя динозавра.
        - weight (int): Вес динозавра в кг.
        - height (int): Рост динозавра в см.
        """
        self.breed = breed
        self.personal_name = personal_name
        self.weight = weight
        self.height = height

    def get_personal_name(self):
        """Возвращает имя динозавра."""
        return self.personal_name

    def get_breed(self):
        """Возвращает вид динозавра."""
        return self.breed

    def get_height(self):
        """Возвращает рост динозавра."""
        return self.height

    def get_weight(self):
        """Возвращает вес динозавра."""
        return self.weight

    def get_diet(self):
        """Возвращает рацион питания динозавра."""
        return "Травоядный"

class DinosaurPark:
    """
    Класс для управления списком динозавров.
    """

    def __init__(self):
        """Инициализация объекта DinosaurPark."""
        self.dinosaurs = []

    def add_dinosaur(self, dinosaur):
        """
        Добавляет динозавра в парк.

        Параметры:
        - dinosaur (Dinosaur): Экземпляр Dinosaur для добавления.
        """
        self.dinosaurs.append(dinosaur)

    def list_dinosaurs(self):
        """
        Возвращает список всех динозавров.

        Возвращает:
        - list: Список кортежей с информацией о каждом динозавре.
        """
        return [
            (
                dinosaur.get_personal_name(),
                dinosaur.get_breed(),
                dinosaur.get_weight(),
                dinosaur.get_height(),
                dinosaur.get_diet(),
            )
            for dinosaur in self.dinosaurs
        ]

    def list_carnivores(self):
        """
        Возвращает список плотоядных динозавров.

        Возвращает:
        - list: Список кортежей с информацией о плотоядных динозаврах.
        """
        return [
            (
                dinosaur.get_personal_name(),
                dinosaur.get_breed(),
                dinosaur.get_weight(),
                dinosaur.get_height(),
                dinosaur.get_diet(),
            )
            for dinosaur in self.dinosaurs
            if dinosaur.get_diet() == "Плотоядный"
        ]

    def list_herbivores(self):
        """
        Возвращает список травоядных динозавров.

        Возвращает:
        - list: Список кортежей с информацией о травоядных динозаврах.
        """
        return [
            (
                dinosaur.get_personal_name(),
                dinosaur.get_breed(),
                dinosaur.get_weight(),
                dinosaur.get_height(),
                dinosaur.get_diet(),
            )
            for dinosaur in self.dinosaurs
            if dinosaur.get_diet() == "Травоядный"
        ]

# Пример использования
if __name__ == "__main__":
    t_rex = Carnivore('Тираннозавр', 'Рекс', 4800, 560)
    velociraptor = Carnivore('Велоцираптор', 'Зубастик', 30, 70)
    stegosaurus = Herbivore('Стегозавр', 'Стегга', 7100, 420)
    triceratops = Herbivore('Трицератопс', 'Трипси', 8000, 290)

    park = DinosaurPark()

    park.add_dinosaur(t_rex)
    park.add_dinosaur(velociraptor)
    park.add_dinosaur(stegosaurus)
    park.add_dinosaur(triceratops)

    for dinosaur in park.list_dinosaurs():
        print(f'Имя: {dinosaur[0]}\n'
              f'Вид: {dinosaur[1]}\n'
              f'Вес: {dinosaur[2]} кг\n'
              f'Рост: {dinosaur[3]} см\n'
              f'Рацион: {dinosaur[4]}\n')