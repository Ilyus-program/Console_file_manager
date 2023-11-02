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


def bill():
    amount = 0
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
            break
        else:
            print('Неверный пункт меню')
