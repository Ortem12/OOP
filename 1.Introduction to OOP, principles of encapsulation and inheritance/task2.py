class Student:
    """
    Класс, представляющий студента.

    Атрибуты:
        name (str): Имя студента.
        age (int): Возраст студента.
        grade (str): Класс, в котором учится студент.
        scores (list): Список оценок студента.

    Методы:
        average_score(): Вычисляет средний балл успеваемости.
    """

    def __init__(self, name, age, grade, scores):
        """
        Инициализирует объект Student.

        Args:
            name (str): Имя студента.
            age (int): Возраст студента.
            grade (str): Класс, в котором учится студент.
            scores (list): Список оценок студента.
        """
        self.name = name
        self.age = age
        self.grade = grade
        self.scores = scores

    def average_score(self):
        """
        Вычисляет средний балл успеваемости.

        Returns:
            float: Средний балл студента.
        """
        return sum(self.scores) / len(self.scores)


# Пример использования
if __name__ == "__main__":
    student2 = Student("Егор Данилов", 12, "5B", [5, 4, 4, 5])
    print("Имя:", student2.name)
    print("Возраст:", student2.age)
    print("Класс:", student2.grade)
    print("Оценки:", *student2.scores)
    print("Средний балл:", student2.average_score())
    