import random
from decorators import add_separators


def f_random_names(digits):
    return random.sample(digits, 3)


@add_separators
def f_questions(fpn, fpd, fpds, res, c, cr, cf):
    # nonlocal count, count_r, count_f
    for num in res:
        question = input(f'Знаете ли Вы год рождения {fpn[num]}? Введите в формате ХХ.ХХ.XXXX: ')
        if question == fpd[num]:
            cr += 1
            print(f'Ответ правильный')
        else:
            cf += 1
            print(f'Ответ неверный! Правильный ответ - {fpds[num]}')
        c += 1
    return c, cr, cf


@add_separators
def f_calc_answer(pcr, pcf, c, cr, cf):
    # Подсчет правильных, неправильных ответов
    # nonlocal per_count_r, per_count_f
    try:
        pcr = int(cr / c * 100)
        pcf = int(cf / c * 100)
    except ZeroDivisionError:
        print('На ноль делить нельзя. Переменная count имеет нулевое значение')
    print('Количество правильных ответов: ', cr)
    print('Количество ошибок: ', cf)
    print('Процент правильных ответов: ', pcr, ' %')
    print('Процент неправильных ответов: ', pcf, ' %')
    # return pcr, pcf


def victory_game():
    # Имена знаменитых людей
    famous_people_name = {
        1: 'И.Ньютон', 2: 'А.Эйнштейн',
        3: 'Г.Галилео', 4: 'М.Ломоносов',
        5: 'Д.Менделеев', 6: 'А.Фет',
        7: 'Л.Толстой', 8: 'А.Пушкин',
        9: 'С.Есенин', 10: 'В.Маяковский'
    }

    # Даты рождения знаменитых людей
    famous_people_date = {
        1: '04.01.1643', 2: '14.03.1879',
        3: '15.02.1564', 4: '19.11.1749',
        5: '08.02.1834', 6: '09.09.1828',
        7: '05.12.1820', 8: '06.06.1799',
        9: '03.10.1895', 10: '19.07.1893'
    }

    # Даты рождения знаменитых людей в формате букв
    famous_people_date_str = {
        1: 'четвертое января 1643 года', 2: 'четырнадцатое марта 1879 года',
        3: 'пятнадцатое февраля 1564 года', 4: 'девятнадцатое ноября 1749 года',
        5: 'восьмое февраля 1834 года', 6: 'девятое сентября 1828 года',
        7: 'пятое декабря 1820 года', 8: 'шестое июня 1799 года',
        9: 'третье октября 1895 года', 10: 'девятнадцатое июля 1893 года'
    }

    # Запуск цикла программы
    while True:
        # исходные данные
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        count_r = 0  # количество правильных ответов
        per_count_r = 0  # процент правильных ответов
        count_f = 0  # количество неправильных ответов
        per_count_f = 0  # процент неправильных ответов
        count = 0  # количество вопросов

        result = f_random_names(numbers)
        # print(result)
        count, count_r, count_f = f_questions(famous_people_name, famous_people_date, famous_people_date_str, result,
                                              count, count_r, count_f)
        f_calc_answer(per_count_r, per_count_f, count, count_r, count_f)

        rep = input('Хотите ли начать игру сначала (y/n): ')
        if rep == 'y' or rep == 'н':
            count_r = 0
            per_count_r = 0
            count_f = 0
            per_count_f = 0
            count = 0
        else:
            break
