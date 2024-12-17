"""
Главный модуль программы
Осуществляет выполнение выбранной из меню задачи, посредством вызова
соответствующей подпрограммы
Перед вызовом запрашивает нужные исходные данные подпрограммы
"""

from package_lab4.laba2 import task2_1, task2_2, task2_3, task2_4
from package_lab4.laba3 import task3_1, task3_2, task3_3, task3_3_recursion

def menu():
    """
    Функция предлагает выбор номера задания и номера лабораторной работы\n
    :param : нет передаваемых параметров
    :return: choice_task - выбранный номер задания
             choice_lab - выбранный номер лабы
    """
    choice_lab = int(input('Выберите 2 или 3 лабороторная: '))
    choice_task = int(input('Выберите номер задания в лабораторной работе: '))

    return choice_lab, choice_task

if __name__ == '__main__':
    while True:
        choice = menu()
        if choice[0] == 2:

            match choice[1]:

                case 1:
                    a = float(input("Введите длину стороны a: "))
                    b = float(input("Введите длину стороны b: "))
                    task2_1(a, b)
                case 2:
                    x = float(input("Введите значение x: "))
                    print(task2_2(x))
                case 3:
                    x = float(input("Введите значение x: "))
                    print(task2_3(x))
                case 4:
                    age = int(input("Введите ваш возраст: "))
                    task2_4(age)
                case _:
                    break

        else:
            match choice[1]:

                case 1:
                    n = int(input("Введите число: "))
                    task3_1(n)
                case 2:
                    M = int(input("Введите натуральное число M: "))
                    task3_2(M)
                case 3:
                    x = float(input('Введите значение для косинуса: '))
                    eps = float(input('Введите точность: '))
                    print(task3_3(x, eps))
                case 4:
                    x = float(input('Введите x: '))  # Значение, для которого вычисляем косинус
                    eps = float(input('Введите точность: '))  # Точность
                    print(task3_3_recursion(x, eps))

                case _:
                    break
        if input('Продолжить? Да/Нет: ') == 'Нет'.lower(): break

