"""
Назва завдання: Декоратори для перевірки коду
Опис: Створіть набір декораторів, які автоматично перевірятимуть функції на наявність можливих помилок
під час їх виконання.

Кроки:
1. Створіть декоратор @check_division_error, який перевіряє, чи немає ділення на нуль в функціях.
Якщо при виклику функції сталася помилка ділення на нуль, декоратор повинен вивести повідомлення
про помилку та завершити виконання програми.

2. Створіть декоратор @check_index_error, який перевіряє, чи виходить індекс за межі списку при доступі до елементу.
Якщо при виклику функції сталася помилка індексації, декоратор повинен вивести повідомлення про помилку та
завершити виконання програми.

3. Створіть функцію divide, яка приймає два числа a та b і повертає результат ділення a на b.
Додайте декоратор @check_division_error до цієї функції.

4. Створіть функцію get_element, яка приймає список lst та індекс idx і повертає елемент зі списку за вказаним індексом.
Додайте декоратор @check_index_error до цієї функції.

5. Напишіть кілька тестових випадків для кожної з функцій divide та get_element, включаючи ситуації, де можуть
виникнути помилки.

6. Перевірте роботу декораторів та функцій, запустивши тести.

7. У випадку виявлення помилок, переконайтеся, що декоратори виводять відповідні повідомлення та завершають
виконання програми.

8. Закінчіть завдання, надславши код декораторів та тестів.
"""


def check_division_error(func):
    """ Декоратор для перевірки ділення на нуль.

    :param func: Функція яку обгортаємо
    :return: Результат обгортки
    """
    def wrapper(*args, **kwargs):
        """ Обгортка. Повертає результат функції, перевіряючи на ділення на нуль.
        Якщо стається помилка ділення на нуль - завершую скрипт через SystemExit з кодом виходу 1.

        :return: Результат обгорнутої функції
        """
        try:
            result = func(*args, **kwargs)
        except ZeroDivisionError:
            print("Error: Division by zero.")
            raise SystemExit(1)
        return result

    return wrapper


def check_index_error(func):
    """ Декоратор для перевірки входження індексу в межі списку.

    :param func: Функція яку обгортаємо
    :return: Результат обгортки
    """
    def wrapper(*args, **kwargs):
        """ Обгортка. Повертає результат функції, перевіряючи чи виходить індекс за межі списку.
        Якщо індекс виходить за межі списку - завершую скрипт через SystemExit з кодом виходу 1.

        :return: Результат обгорнутої функції
        """
        try:
            result = func(*args, **kwargs)
        except IndexError:
            print("Error: Index out of range.")
            raise SystemExit(1)
        return result

    return wrapper


@check_division_error
def divide(a: float, b: float) -> float:
    """ Функція ділення.

    :param a: ділене
    :param b: дільник
    :return: частка
    """

    return a / b


@check_index_error
def get_element(lst: list, idx: int):
    """ Функція повернення елементу списку за його індексом.

    :param lst: Список
    :param idx: Індекс елементу
    :return: Елемент
    """
    return lst[idx]


# сomment rows with false to get to the end

# TEST DIVIDE
print(divide(10, 2))    # True
print(divide(5, 0))     # False

# TEST GET ELEMENT
print(get_element([1, 2, 3], 1))    # True
print(get_element([1, 2, 3], 5))    # False
print(get_element([], 0))           # False
