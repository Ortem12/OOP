class Book:
    """Класс, представляющий книгу в библиотеке.

    Attributes:
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания.
        is_available (bool): Статус доступности книги.
    """

    def __init__(self, title, author, year):
        """Инициализирует объект книги.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания.
        """
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def borrow(self):
        """Выдает книгу читателю, если она доступна."""
        if self.is_available:
            self.is_available = False
            print(f"Книга '{self.title}' выдана.")
        else:
            print(f"Книга '{self.title}' уже выдана.")

    def return_book(self):
        """Возвращает книгу в библиотеку."""
        if not self.is_available:
            self.is_available = True
            print(f"Книга '{self.title}' возвращена.")
        else:
            print(f"Книга '{self.title}' уже в библиотеке.")


class Reader:
    """Класс, представляющий читателя библиотеки.

    Attributes:
        name (str): Имя читателя.
        borrowed_books (list): Список взятых книг.
    """

    def __init__(self, name):
        """Инициализирует объект читателя.

        Args:
            name (str): Имя читателя.
        """
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        """Читатель берет книгу.

        Args:
            book (Book): Книга, которую берет читатель.
        """
        if book.is_available:
            self.borrowed_books.append(book)
            book.borrow()
        else:
            print(f"Книга '{book.title}' недоступна.")

    def return_book(self, book):
        """Читатель возвращает книгу.

        Args:
            book (Book): Книга, которую возвращает читатель.
        """
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
        else:
            print(f"Книга '{book.title}' не была взята этим читателем.")


class Library:
    """Класс, представляющий библиотеку.

    Attributes:
        books (list): Список книг в библиотеке.
        readers (list): Список читателей.
    """

    def __init__(self):
        """Инициализирует объект библиотеки."""
        self.books = []
        self.readers = []

    def add_book(self, book):
        """Добавляет книгу в библиотеку.

        Args:
            book (Book): Книга для добавления.
        """
        self.books.append(book)
        print(f"Книга '{book.title}' добавлена в библиотеку.")

    def add_reader(self, reader):
        """Добавляет читателя в библиотеку.

        Args:
            reader (Reader): Читатель для добавления.
        """
        self.readers.append(reader)
        print(f"Читатель '{reader.name}' добавлен в библиотеку.")

    def borrow_book_to_reader(self, reader, book):
        """Выдает книгу читателю.

        Args:
            reader (Reader): Читатель, который берет книгу.
            book (Book): Книга, которую выдают.
        """
        if book in self.books:
            reader.borrow_book(book)
        else:
            print(f"Книга '{book.title}' отсутствует в библиотеке.")

    def return_book_from_reader(self, reader, book):
        """Принимает книгу от читателя.

        Args:
            reader (Reader): Читатель, который возвращает книгу.
            book (Book): Книга, которую возвращают.
        """
        if book in self.books:
            reader.return_book(book)
        else:
            print(f"Книга '{book.title}' не принадлежит библиотеке.")


# Пример использования
if __name__ == "__main__":
    # Создаем книги
    book1 = Book("1984", "George Orwell", 1949)
    book2 = Book("The plague", "Camus Albert", 1947)

    # Создаем читателей
    reader1 = Reader("Alice")
    reader2 = Reader("Bob")

    # Создаем библиотеку
    library = Library()

    # Добавляем книги и читателей в библиотеку
    library.add_book(book1)
    library.add_book(book2)
    library.add_reader(reader1)
    library.add_reader(reader2)

    # Выдача и возврат книг
    library.borrow_book_to_reader(reader1, book1)
    library.borrow_book_to_reader(reader2, book2)
    library.return_book_from_reader(reader1, book1)
    library.return_book_from_reader(reader2, book2)