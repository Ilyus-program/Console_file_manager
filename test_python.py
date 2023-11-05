from math import pi, sqrt, pow, hypot


def test_filter():
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num_2 = [1.5, 2, 3, 4.8, 5, 6, 7.0, 8, 9.3]

    # фильтр четных и нечетных чисел
    def filter_odd_num(n):  # проверка на нечетность
        if (n % 2) > 0:
            return True
        else:
            return False

    def filter_even_num(n):  # проверка на четность
        if (n % 2) == 0:
            return True
        else:
            return False

    odd_num = filter(filter_odd_num, num)  # фильтруем нечетные числа
    for i in odd_num:
        assert i % 2 != 0  # проверка odd_num на нечетные числа

    even_num = filter(filter_even_num, num)  # фильтруем четные числа
    for i in even_num:
        assert i % 2 == 0  # проверка even_num на четные числа

    # фильтр целых чисел
    f = filter(lambda x: type(x) is int, num_2)
    for i in f:
        assert type(i) is int


def test_map():
    names = ['Sammy', 'Ashley', 'Jo', 'Max', 'Jackie', 'Charlie']
    x = [1, 2, 4, 6]
    y = [3, 2, 7, 6]

    # вычисление длины элемента списка
    length = list(map(len, names))
    for i in range(len(length)):
        assert length[i] == len(names[i])  # проверка полученных длин

    # вычисление степени для каждого элемента списка Х
    p = list(map(pow, x, y))
    for i in range(len(p)):
        assert p[i] == (x[i] ** y[i])  # проверка результатов


def test_sorted():
    names = ['Sammy', 'Ashley', 'Jo', 'Max', 'Jackie', 'Charlie']

    # сортировка по возрастанию
    name_sort = sorted(names)
    for i in range(len(name_sort)):
        if i > 0:
            assert name_sort[i] > name_sort[i - 1]  # проверка отсортированных элементов по возрастанию


def test_sqrt():
    n = [4, 9, 16, 25]
    assert sqrt(4) == 2
    assert sqrt(9) == 3
    n_sqr = map(sqrt, n)
    n_sqr = [int(i) for i in n_sqr]
    for j in range(len(n_sqr)):
        assert n_sqr[j] == sqrt(n[j])


def test_pow():
    assert pow(3, 2) == 9
    assert pow(10, 3) == 1000

def test_hypot():
    assert hypot(3, 2) == sqrt(3*3 + 2*2)
    assert hypot(6, 9) == sqrt(6 * 6 + 9 * 9)
    assert hypot(0.8, 3.4) == sqrt(0.8 ** 2 + 3.4 ** 2)
