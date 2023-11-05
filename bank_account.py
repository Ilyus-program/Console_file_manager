import json
import os


FOLDER = 'files'
FILE_WALLET = f'{FOLDER}/bank_account.json'
FILE_HIST = f'{FOLDER}/orders_hist.json'


def add_money(money, en_ment):
    money += int(en_ment)
    return money


def shop(wallet, pokupki):
    thing = int(input('Цена покупки '))
    if thing <= wallet:
        name_thing = input('Введите название покупки ')
        wallet -= thing
        pokupki[name_thing] = thing
    else:
        print('На счете недостаточно средств')
    return wallet, pokupki


def show_hist(goods):
    print('Куплены следующие товары:')
    for key, val in goods.items():
        print(f'{key} по цене {val} рублей')


def file_read(file):
    with open(file, 'r') as f:
        am = json.load(f)
    return am


def file_write(file, am):
    with open(file, 'w') as f:
        json.dump(am, f)


def bill():
    # amount = 0
    if not os.path.exists(FOLDER):
        # сздать папку передаем путь
        os.mkdir(FOLDER)
    if os.path.exists(FILE_WALLET):
        amount = file_read(FILE_WALLET)
    else:
        amount = 0

    if os.path.exists(FILE_HIST):
        hist = file_read(FILE_HIST)
    else:
        hist = {}
    while True:
        print(f'На счете {amount} рублей')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню ')
        if choice == '1':
            enrollment = input('Пополните счет ')
            amount = add_money(amount, enrollment)
        elif choice == '2':
            amount, hist = shop(amount, hist)
        elif choice == '3':
            show_hist(hist)
        elif choice == '4':
            file_write(FILE_WALLET, amount)
            file_write(FILE_HIST, hist)
            break
        else:
            print('Неверный пункт меню')


# bill()
