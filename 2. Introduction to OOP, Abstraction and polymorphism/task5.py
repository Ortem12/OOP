from abc import ABC, abstractmethod

class Instrument(ABC):
    """
    Абстрактный класс, представляющий музыкальный инструмент.
    Все подклассы должны реализовать методы:
    - get_name(): Возвращает название инструмента.
    - get_type(): Возвращает тип инструмента.
    - get_sound(): Возвращает звук инструмента.
    - play(): Воспроизводит звук инструмента.
    """

    @abstractmethod
    def get_name(self):
        """Абстрактный метод для получения названия инструмента."""
        pass

    @abstractmethod
    def get_type(self):
        """Абстрактный метод для получения типа инструмента."""
        pass

    @abstractmethod
    def get_sound(self):
        """Абстрактный метод для получения звука инструмента."""
        pass

    @abstractmethod
    def play(self):
        """Абстрактный метод для воспроизведения звука инструмента."""
        pass

class StringedInstrument(Instrument):
    """
    Класс, представляющий струнный инструмент.
    Наследует абстрактный класс Instrument.
    """

    def __init__(self, name, instrument_type, sound):
        """
        Инициализация объекта StringedInstrument.

        Параметры:
        - name (str): Название инструмента.
        - instrument_type (str): Тип инструмента.
        - sound (str): Звук, издаваемый инструментом.
        """
        self.name = name
        self.instrument_type = instrument_type
        self.sound = sound

    def get_name(self):
        """Возвращает название инструмента."""
        return self.name

    def get_type(self):
        """Возвращает тип инструмента."""
        return self.instrument_type

    def get_sound(self):
        """Возвращает звук инструмента."""
        return self.sound

    def play(self):
        """Воспроизводит звук струнного инструмента."""
        return f"Звучит струнный инструмент {self.name}"

class PercussionInstrument(Instrument):
    """
    Класс, представляющий ударный инструмент.
    Наследует абстрактный класс Instrument.
    """

    def __init__(self, name, instrument_type, sound):
        """
        Инициализация объекта PercussionInstrument.

        Параметры:
        - name (str): Название инструмента.
        - instrument_type (str): Тип инструмента.
        - sound (str): Звук, издаваемый инструментом.
        """
        self.name = name
        self.instrument_type = instrument_type
        self.sound = sound

    def get_name(self):
        """Возвращает название инструмента."""
        return self.name

    def get_type(self):
        """Возвращает тип инструмента."""
        return self.instrument_type

    def get_sound(self):
        """Возвращает звук инструмента."""
        return self.sound

    def play(self):
        """Воспроизводит звук ударного инструмента."""
        return f"Звучит ударный инструмент {self.name}"

class Orchestra:
    """
    Класс для управления списком музыкальных инструментов в оркестре.
    """

    def __init__(self):
        """Инициализация объекта Orchestra."""
        self.instruments = []

    def add_instrument(self, instrument):
        """
        Добавляет инструмент в оркестр.

        Параметры:
        - instrument (Instrument): Экземпляр Instrument для добавления.
        """
        self.instruments.append(instrument)

    def list_instruments(self):
        """
        Возвращает список всех инструментов.

        Возвращает:
        - list: Список названий всех инструментов.
        """
        return [instrument.get_name() for instrument in self.instruments]

    def list_stringed_instruments(self):
        """
        Возвращает список струнных инструментов.

        Возвращает:
        - list: Список названий струнных инструментов.
        """
        return [
            instrument.get_name()
            for instrument in self.instruments
            if instrument.get_type() == "струнный инструмент"
        ]

    def list_percussion_instruments(self):
        """
        Возвращает список ударных инструментов.

        Возвращает:
        - list: Список названий ударных инструментов.
        """
        return [
            instrument.get_name()
            for instrument in self.instruments
            if instrument.get_type() == "ударный инструмент"
        ]

# Пример использования
if __name__ == "__main__":
    chello = StringedInstrument("виолончель", "струнный инструмент", "Strum")
    maracas = PercussionInstrument("маракасы", "ударный инструмент", "Maracas")
    violin = StringedInstrument("скрипка", "струнный инструмент", "Virtuso")
    drums = PercussionInstrument("барабан", "ударный инструмент", "Beat")

    orchestra = Orchestra()
    orchestra.add_instrument(chello)
    orchestra.add_instrument(maracas)
    orchestra.add_instrument(violin)
    orchestra.add_instrument(drums)

    print("В оркестре есть инструменты:", ', '.join(orchestra.list_instruments()))
    print("Струнные инструменты:", ', '.join(orchestra.list_stringed_instruments()))
    print("Ударные инструменты:", ', '.join(orchestra.list_percussion_instruments()))

    print(chello.play())
    print(drums.play())