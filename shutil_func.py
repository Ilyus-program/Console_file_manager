import shutil


# Скопировать папку или файл
def copy_folder_file():
    user_path = input('Введите имя папки или файла: ')
    user_new_path = input('Введите имя папки или файла: ')
    try:
        shutil.copy(user_path, user_new_path)
    except FileNotFoundError:
        print(f'Не удается найти указанный файл: {user_path}')
