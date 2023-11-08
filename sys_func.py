import platform
import os
import pathlib
from decorators import add_separators


# информация об операционной системе
@add_separators
def os_info():
    print(f'ОС: {platform.system()}')
    print(f'Имя компьютера: {platform.node()}')
    print(f'Тип машины: {platform.machine()}')
    print(f'Платформа: {platform.platform()}')
    print(f'Процессор: {platform.processor()}')


def change_path():
    user_path = input('Введите имя папки: ')
    user_path = user_path.split('\\')
    path_1 = str(pathlib.Path(os.getcwd()))
    path_1 = path_1.split('\\')
    path_2 = []
    # print(user_path)
    # print(path_1)
    # path_2 = [path_2.append(i) for i in user_path if not i in path_1]
    for i in user_path:
        if not (i in path_1):
            path_2.append(i)
    print(path_2)
    try:
        os.chdir(path_2[0])
        print(os.getcwd())
    except FileNotFoundError:
        print(f'Не удается найти указанный файл: {user_path}')
        print('Если хотите вернуться в директорию выше, наберите ../')


if __name__ == '__main__':
    # os_info()
    change_path()
