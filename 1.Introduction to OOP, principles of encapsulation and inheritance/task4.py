class Publisher:
    """
    Суперкласс, представляющий издательство.

    Атрибуты:
        name (str): Название издательства.
        location (str): Расположение издательства.

    Методы:
        get_info(): Возвращает информацию о названии и расположении издательства.
        publish(message): Выводит информацию об издании, которое находится в печати.
    """

    def __init__(self, name, location):
        """
        Инициализирует объект Publisher.

        Args:
            name (str): Название издательства.
            location (str): Расположение издательства.
        """
        self.name = name
        self.location = location

    def get_info(self):
        """
        Возвращает информацию о названии и расположении издательства.

        Returns:
            str: Информация о издательстве.
        """
        return f"{self.name} ({self.location})"

    def publish(self, message):
        """
        Выводит информацию об издании, которое находится в печати.

        Args:
            message (str): Название издания.
        """
        print(f'Готовим "{message}" к публикации в {self.get_info()}')


class BookPublisher(Publisher):
    """
    Подкласс, представляющий книжное издательство.

    Атрибуты:
        num_authors (int): Количество авторов.

    Методы:
        publish(title, author): Выводит информацию о книге, которая находится в печати.
    """

    def __init__(self, name, location, num_authors):
        """
        Инициализирует объект BookPublisher.

        Args:
            num_authors (int): Количество авторов.
        """
        super().__init__(name, location)
        self.num_authors = num_authors

    def publish(self, title, author):
        """
        Выводит информацию о книге, которая находится в печати.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
        """
        print(f'Передаем рукопись "{title}", написанную автором {author} в издательство {self.get_info()}')


class NewspaperPublisher(Publisher):
    """
    Подкласс, представляющий газетное издательство.

    Атрибуты:
        num_pages (int): Количество страниц в газете.

    Методы:
        publish(article): Выводит информацию о газете, которая находится в печати.
    """

    def __init__(self, name, location, num_pages):
        """
        Инициализирует объект NewspaperPublisher.

        Args:
            num_pages (int): Количество страниц в газете.
        """
        super().__init__(name, location)
        self.num_pages = num_pages

    def publish(self, article):
        """
        Выводит информацию о газете, которая находится в печати.

        Args:
            article (str): Название статьи.
        """
        print(f'Печатаем свежий номер со статьей "{article}" на главной странице в издательстве {self.get_info()}')


# Пример использования
if __name__ == "__main__":
    publisher = Publisher("АБВГД Пресс", "Москва")
    publisher.publish("Справочник писателя")

    book_publisher = BookPublisher("Важные Книги", "Самара", 52)
    book_publisher.publish("Приключения Чебурашки", "В.И. Пупкин")

    newspaper_publisher = NewspaperPublisher("Московские вести", "Москва", 12)
    newspaper_publisher.publish("Новая версия Midjourney будет платной")