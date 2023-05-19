import os

# Функция создания папки
def create_folder():
    user_path = input('Введите имя папки: ')
    # проверка на существование
    if not os.path.exists(user_path):
        # сздать папку передаем путь
        os.mkdir(user_path)
    else:
        print(f'Папка с именем {user_path} уже существует')

# Функция удаления папки или файла
def delete_folder_file():
    user_path = input('Введите имя папки или файла: ')
    if os.path.isfile(user_path):
        os.remove(user_path)
    else:
        if os.path.isdir(user_path):
            os.removedirs(user_path)
        else:
            print(f'Папки или файла с именем {user_path} не существует')

# Функция просмотра содержимого рабочей папки
def view_work_dir(choice):
    if choice == '4':
        print(os.listdir())
    elif choice == '5':
        for i in os.listdir():
            if os.path.isdir(i):
                print(i, end=' ')
        print()
    elif choice == '6':
        for i in os.listdir():
            if os.path.isfile(i):
                print(i, end=' ')
        print()

