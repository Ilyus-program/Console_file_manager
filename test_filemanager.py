import shutil
import random
import os
from os_func import create_folder, delete_folder_file, view_work_dir, file_dir_write
from shutil_func import copy_folder_file
from sys_func import os_info, change_path
from victory import victory_game
from bank_account import add_money, file_read, file_write
# from decorators import add_separators
import json


# Тест функций из викторины
def test_f_random_names():  # не совсем чистая функция из-за random
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def f_random_names(digits):
        return random.sample(digits, 3)

    # длина возвращаемого списка случайных числе должна быть 3
    assert len(f_random_names(numbers)) == 3

    # тип возвращаемых случайных чисел должен быть целым
    for i in f_random_names(numbers):
        assert type(i) is int


def test_f_questions():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    count_r = 0  # количество правильных ответов
    per_count_r = 0  # процент правильных ответов
    count_f = 0  # количество неправильных ответов
    per_count_f = 0  # процент неправильных ответов
    count = 0  # количество вопросов

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

    result = random.sample(numbers, 3)

    def f_questions(fpn, fpd, fpds, res):
        nonlocal count, count_r, count_f
        for num in res:
            question = '14.03.1879'  # input(f'Знаете ли Вы год рождения {fpn[num]}? Введите в формате ХХ.ХХ.XXXX: ')
            if question == fpd[num]:
                count_r += 1
                print(f'Ответ правильный')
            else:
                count_f += 1
                print(f'Ответ неверный! Правильный ответ - {fpds[num]}')
            count += 1
        return count, count_r, count_f

    f_questions(famous_people_name, famous_people_date, famous_people_date_str, result)
    assert count == len(result)  # проверка счетчика вопросов количеству случайных чисел
    assert (count_f + count_r) == len(result)  # проверка суммы прав. и неправ. вопросов количеству случайных чисел
    assert (count_f + count_r) == count  # проверка суммы прав. и неправ. вопросов счетчику вопросов

    def f_calc_answer(c, cr, cf):
        # Подсчет правильных, неправильных ответов
        nonlocal per_count_r, per_count_f
        per_count_r = int(cr / c * 100)
        per_count_f = int(cf / c * 100)
        print('Количество правильных ответов: ', count_r)
        print('Количество ошибок: ', count_f)
        print('Процент правильных ответов: ', per_count_r, ' %')
        print('Процент неправильных ответов: ', per_count_f, ' %')
        return per_count_r, per_count_f

    f_calc_answer(count, count_r, count_f)
    assert per_count_r + per_count_f >= 99  # проверка процентного соотношения


# Тест функций из программы "Мой счет"
def test_add_money():
    assert type(add_money(money=0, en_ment=50)) is int
    assert add_money(0, 25.6) >= 0


def test_shop():
    wall = 50
    pokup = {'Вода': 20, 'Хлеб': 10}

    def shop(wallet, pokupki):
        thing = 50
        if thing <= wallet:
            name_thing = 'Тетрадь'
            wallet -= thing
            pokupki[name_thing] = thing
        else:
            print('На счете недостаточно средств')
        return wallet, pokupki

    shop(wall, pokup)
    assert type(wall) is int
    assert wall >= 0
    assert len(pokup) >= 0


# проверка правильности записи и чтения
def test_read_write_file():
    files = 'files/test_rd_wr_f.txt'
    file_write(files, 100)
    r = file_read(files)
    assert r == 100


# Тест функции копирования файлов
def test_copy_folder_file():
    file = 'new_word.txt'

    def copy_folder_file():
        user_path = 'text_new.txt'
        user_new_path = file
        shutil.copy(user_path, user_new_path)

    if file in os.listdir():
        os.remove(os.path.abspath(file))
    else:
        copy_folder_file()
        assert file in os.listdir()


# Проверка наличия названия файла listdir.txt
def test_file_dir_write():
    FILE_NAME = 'files/listdir.txt'
    fl = 'bank_account.py'
    with open(FILE_NAME, 'r') as f:
        os_files = f.readlines()
        for i in os_files:
            k = i.find(fl)
            if k != -1:
                res = True
                break
            else:
                res = False
    assert res == True


def test_add_separators():
    def add_separators(func):
        def inner(arg, kwarg):
            print('<' + ('-' * 50) + '>')
            result = func(arg, kwarg)
            print('<' + ('-' * 50) + '>')
            return result
        res = inner(0, 50)
        return res

    assert add_separators(add_money) == add_money(0, 50)
