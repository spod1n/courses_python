"""
Назва завдання: Декоратори для перевірки коду
Опис: Створіть набір декораторів, які автоматично перевірятимуть функції на наявність можливих помилок
під час їх виконання.

Кроки:
1. Створіть декоратор @check_division_error, який перевіряє, чи немає ділення на
нуль в функціях. Якщо при виклику функції сталася помилка ділення на нуль,
декоратор повинен вивести повідомлення про помилку та завершити
виконання програми.

2. Створіть декоратор @check_index_error, який перевіряє, чи виходить індекс за
межі списку при доступі до елементу. Якщо при виклику функції сталася
помилка індексації, декоратор повинен вивести повідомлення про помилку та
завершити виконання програми.

3. Створіть функцію divide , яка приймає два числа a та b і повертає результат
ділення a на b. Додайте декоратор @check_division_error до цієї функції.

4. Створіть функцію get_element , яка приймає список lst та індекс idx і повертає
елемент зі списку за вказаним індексом. Додайте декоратор @check_index_error
до цієї функції.

5. Напишіть кілька тестових випадків для кожної з функцій divide та get_element ,
включаючи ситуації, де можуть виникнути помилки.

6. Перевірте роботу декораторів та функцій, запустивши тести.

7. У випадку виявлення помилок, переконайтеся, що декоратори виводять
відповідні повідомлення та завершають виконання програми.

8. Закінчіть завдання, надславши код декораторів та тестів.
"""
