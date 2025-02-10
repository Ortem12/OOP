class Employee:
    """
    Класс, представляющий сотрудника.

    Атрибуты:
        __name (str): Имя сотрудника (приватный).
        __age (int): Возраст сотрудника (приватный).
        __salary (float): Оклад сотрудника (приватный).
        __bonus (float): Премия сотрудника (приватный).

    Методы:
        get_name(): Возвращает имя сотрудника.
        get_age(): Возвращает возраст сотрудника.
        get_salary(): Возвращает оклад сотрудника.
        set_bonus(bonus): Устанавливает премию сотрудника.
        get_bonus(): Возвращает премию сотрудника.
        get_total_salary(): Возвращает общую зарплату (оклад + премия).
    """

    def __init__(self, name, age, salary):
        """
        Инициализирует объект Employee.

        Args:
            name (str): Имя сотрудника.
            age (int): Возраст сотрудника.
            salary (float): Оклад сотрудника.
        """
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__bonus = 0  # Премия по умолчанию равна 0

    def get_name(self):
        """
        Возвращает имя сотрудника.

        Returns:
            str: Имя сотрудника.
        """
        return self.__name

    def get_age(self):
        """
        Возвращает возраст сотрудника.

        Returns:
            int: Возраст сотрудника.
        """
        return self.__age

    def get_salary(self):
        """
        Возвращает оклад сотрудника.

        Returns:
            float: Оклад сотрудника.
        """
        return self.__salary

    def set_bonus(self, bonus):
        """
        Устанавливает премию сотрудника.

        Args:
            bonus (float): Премия сотрудника.
        """
        if bonus >= 0:
            self.__bonus = bonus
        else:
            print("Ошибка: Премия не может быть отрицательной.")

    def get_bonus(self):
        """
        Возвращает премию сотрудника.

        Returns:
            float: Премия сотрудника.
        """
        return self.__bonus

    def get_total_salary(self):
        """
        Возвращает общую зарплату сотрудника (оклад + премия).

        Returns:
            float: Общая зарплата.
        """
        return self.__salary + self.__bonus


# Пример использования
if __name__ == "__main__":
    # Создаем сотрудника с именем, возрастом и зарплатой
    employee = Employee("Марина Арефьева", 30, 90000)

    # Устанавливаем бонус для сотрудника
    employee.set_bonus(15000)

    # Выводим имя, возраст, зарплату, бонус и общую зарплату сотрудника
    print("Имя:", employee.get_name())
    print("Возраст:", employee.get_age())
    print("Зарплата:", employee.get_salary())
    print("Бонус:", employee.get_bonus())
    print("Итого начислено:", employee.get_total_salary())