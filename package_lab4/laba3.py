def task3_1(n):
    '''
    Дано натуральное число n. Определить является ли оно автоморфным.
    Автоморфное число равно последним разрядам квадрата этого числа (52 =
    25, 62 = 36, 252= 625)

    :param n: Вводимое число для проверки
    :return: None
    '''

    # Вычисляем квадрат числа
    square = n * n

    # Считаем количество цифр в числе n
    k = len(str(n))

    # Берём последние k цифр из квадрата
    last_digits = square % (10 ** k)

    # Проверяем, совпадают ли последние k цифр с самим числом n
    if last_digits == n:
        print(f"Число {n} является автоморфным")
    else:
        print(f"Число {n} не является автоморфным")




def task3_2(M):
    '''
    Можно ли заданное натуральное число М представить в виде суммы
    квадратов двух натуральных чисел? Написать программу решения этой задачи

    :param M: Вводимое натуральное число
    :return: None
    '''
    found = False

    for a in range(1, int(M ** 0.5) + 1):
        b_squared = M - a ** 2
        if b_squared > 0:
            b = int(b_squared ** 0.5)
            if b ** 2 == b_squared and b > 0:
                print(f"{M} = {a}^2 + {b}^2")
                found = True
                break

    if not found:
        print("Такое представление невозможно.")




def task3_3(x, eps):
    '''
    :param x: Вводимое число
    :param eps: Точность
    :return: Значение косинуса
    '''
    def my_cos(x, eps):
        n = 0
        term = 1  # Перве слагаемое (n=0)
        cos_value = term  # Начальное значение косинуса

        while abs(term) >= eps:
            n += 1
            term = (-1) ** n * (x ** (2 * n)) / factorial(2 * n)  # Вычисление текущего слагаемого
            cos_value += term  # Суммируем

        return cos_value

    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    return my_cos(x, eps)




def task3_3_recursion(x, eps):
    '''
    :param x: Вводимое число
    :param eps: Точность
    :return: Значение косинуса
    '''
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    def my_cos_recursive(x, n=0, eps=1e-10):
        # Вычисляем текущее слагаемое
        term = ((-1) ** n) * (x ** (2 * n)) / factorial(2 * n)

        # Если модуль текущего слагаемого меньше eps, возвращаем 0 (больше не добавляем)
        if abs(term) < eps:
            return 0
        else:
            # Рекурсивно добавляем текущее слагаемое к результату
            return term + my_cos_recursive(x, n + 1, eps)


    result = my_cos_recursive(x, eps=eps)
    return result