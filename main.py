from os_func import create_folder, delete_folder_file, view_work_dir
from shutil_func import copy_folder_file
from sys_func import os_info, change_path
from victory import victory_game
from bank_account import bill

# Цикл программы, создание меню программы
while True:
    print(' 1. создать папку')
    print(' 2. удалить (файл/папку)')
    print(' 3. копировать (файл/папку)')
    print(' 4. просмотр содержимого рабочей директории')
    print(' 5. посмотреть только папки')
    print(' 6. посмотреть только файлы')
    print(' 7. просмотр информации об операционной системе')
    print(' 8. создатель программы')
    print(' 9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. выход')

    choice = input('Выберите пункт меню ')
    if choice == '1':
        create_folder()
    elif choice == '2':
        delete_folder_file()
    elif choice == '3':
        copy_folder_file()
    elif choice == '4':
        view_work_dir(choice)
    elif choice == '5':
        view_work_dir(choice)
    elif choice == '6':
        view_work_dir(choice)
    elif choice == '7':
        os_info()
    elif choice == '8':
        print('ФИО: Каримов Илюс Ришатович','Возраст: 42 года', 'Профессия: Инженер АСУТП', sep='\n')
    elif choice == '9':
        victory_game()
    elif choice == '10':
        bill()
    elif choice == '11':
        change_path()
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')