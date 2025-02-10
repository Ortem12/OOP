import random

class MusicAlbum:
    """
    Класс, представляющий музыкальный альбом.

    Атрибуты:
        title (str): Название альбома.
        artist (str): Исполнитель.
        release_year (int): Год выпуска альбома.
        genre (str): Жанр.
        tracklist (list): Список треков.

    Методы:
        play_random_track(): Воспроизводит случайный трек из альбома.
    """

    def __init__(self, title, artist, release_year, genre, tracklist):
        """
        Инициализирует объект MusicAlbum.

        Args:
            title (str): Название альбома.
            artist (str): Исполнитель.
            release_year (int): Год выпуска альбома.
            genre (str): Жанр.
            tracklist (list): Список треков.
        """
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.genre = genre
        self.tracklist = tracklist

    def play_random_track(self):
        """
        Воспроизводит случайный трек из списка треков.

        Выводит название случайного трека и его номер в списке.
        """
        random_track_index = random.randint(0, len(self.tracklist) - 1)
        random_track = self.tracklist[random_track_index]
        print(f"Воспроизводится трек {random_track_index + 1}: {random_track}")


class LiveAlbum(MusicAlbum):
    """
    Класс, представляющий концертный альбом. Наследует от MusicAlbum.

    Атрибуты:
        location (str): Место проведения концерта.

    Методы:
        display_location(): Выводит место проведения концерта.
        play_random_track(): Переопределяет метод для воспроизведения трека с учетом особенностей живого альбома.
    """

    def __init__(self, title, artist, release_year, genre, tracklist, location):
        """
        Инициализирует объект LiveAlbum.

        Args:
            location (str): Место проведения концерта.
        """
        super().__init__(title, artist, release_year, genre, tracklist)
        self.location = location

    def display_location(self):
        """
        Выводит место проведения концерта.
        """
        print(f"Концерт записан в: {self.location}")

    def play_random_track(self):
        """
        Воспроизводит случайный трек с учетом особенностей живого альбома.

        Выводит название трека и добавляет аплодисменты.
        """
        print("В живом альбоме треки воспроизводятся в случайном порядке, но с аплодисментами!")
        random_track = random.choice(self.tracklist)
        print(f"Воспроизводится трек: {random_track} (аплодисменты)")


# Пример использования
if __name__ == "__main__":
    album = MusicAlbum("Deutschland", "Rammstein", 2019, "Neue Deutsche Härte",
                       ["Deutschland", "Radio", "Zeig dich", "Ausländer", "Sex",
                        "Puppe", "Was ich liebe", "Diamant", "Weit weg", "Tattoo",
                        "Hallomann"])
    print("Название:", album.title)
    print("Исполнитель:", album.artist)
    print("Год:", album.release_year)
    print("Жанр:", album.genre)
    print("Треки:", album.tracklist)
    album.play_random_track()

    live_album = LiveAlbum("Live in Paris", "Rammstein", 2020, "Neue Deutsche Härte",
                           ["Deutschland", "Radio", "Zeig dich"], "Paris, France")
    live_album.display_location()
    live_album.play_random_track()