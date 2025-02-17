class Movie:
    """
    Базовый класс для представления фильма.
    
    Атрибуты:
        title (str): Название фильма.
        director (str): Режиссер фильма.
    """
    
    def __init__(self, title: str, director: str):
        self.title = title
        self.director = director
        
    def play(self) -> str:
        """
        Возвращает строку с информацией о воспроизведении фильма.
        Должен быть переопределен в дочерних классах.
        """
        raise NotImplementedError("Метод play() должен быть переопределен в подклассах")


class Horror(Movie):
    """Класс для фильмов ужасов."""
    def play(self) -> str:
        return f"Включаем фильм ужасов '{self.title}' реж. {self.director}."


class Action(Movie):
    """Класс для боевиков."""
    def play(self) -> str:
        return f"Включаем боевик '{self.title}' реж. {self.director}."


class Romance(Movie):
    """Класс для мелодрам."""
    def play(self) -> str:
        return f"Включаем мелодраму '{self.title}' реж. {self.director}."


class Drama(Movie):
    """Класс для драм."""
    def play(self) -> str:
        return f"Включаем драму '{self.title}' реж. {self.director}."


class Comedy(Movie):
    """Класс для комедий."""
    def play(self) -> str:
        return f"Включаем комедию '{self.title}' реж. {self.director}."


class FilmCatalogue:
    """
    Каталог для управления коллекцией фильмов.
    
    Методы:
        add_movie(movie: Movie) -> None: Добавляет фильм в каталог.
        play_all_movies() -> None: Воспроизводит все фильмы.
        search_movies_by_genre(genre: type) -> list[Movie]: Ищет фильмы по жанру.
        play_movies_by_genre(genre: type) -> None: Воспроизводит фильмы определенного жанра.
    """
    
    def __init__(self):
        self.movies = []
        
    def add_movie(self, movie: Movie) -> None:
        """Добавляет фильм в каталог."""
        self.movies.append(movie)
        
    def play_all_movies(self) -> None:
        """Последовательно воспроизводит все фильмы."""
        for movie in self.movies:
            print(movie.play())
            
    def search_movies_by_genre(self, genre: type) -> list[Movie]:
        """Возвращает список фильмов указанного жанра."""
        return [movie for movie in self.movies if isinstance(movie, genre)]
    
    def play_movies_by_genre(self, genre: type) -> None:
        """Воспроизводит фильмы указанного жанра."""
        for movie in self.search_movies_by_genre(genre):
            print(movie.play())


# Пример использования
my_catalogue = FilmCatalogue()

my_catalogue.add_movie(Drama("Крестный отец", "Френсис Ф. Коппола"))
my_catalogue.add_movie(Comedy("Ночные игры", "Джон Фрэнсис Дейли, Джонатан М. Голдштейн"))
my_catalogue.add_movie(Horror("Дракула Брэма Стокера", "Френсис Ф. Коппола"))
my_catalogue.add_movie(Action("Крушение", "Жан-Франсуа Рише"))
my_catalogue.add_movie(Romance("Честная куртизанка", "Маршалл Херсковиц"))

my_catalogue.play_all_movies()

print("\nНайдены фильмы ужасов:")
for movie in my_catalogue.search_movies_by_genre(Horror):
    print(movie.title)

print("\nЗапускаем фильм из жанра 'Мелодрамы':")
my_catalogue.play_movies_by_genre(Romance)