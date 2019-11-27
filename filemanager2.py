"""
Программа для сохранения покупок
Название + Цена
"""
import os
import pickle

FILE_NAME = 'orders_pickle.data'

bill_sum = 0
orders = []
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'rb') as f:
        orders = pickle.load(f)

while True:
    print('1. пополнение счета')
    print('2. Добавить покупку')
    print('3. История покупок')
    print('4. Выход')
    print(f'Ваш счет {bill_sum}')
    choise = input('Введите номер операции: ')
    if choise == '1':
        cost = int(input('Введите сумму пополнения счета: '))
        bill_sum += cost
    elif choise == '2':
        name = input('Введите название покупки: ')
        buy = int(input('Введите цену покупки: '))
        if buy > bill_sum:
            print('Недостаточно средств')
        else:
            bill_sum -= buy
            order = (name, buy)
            orders.append(order)
    elif choise == '3':
        for order in orders:
            print(order)
    elif choise == '4':
        with open(FILE_NAME, 'wb') as f:
            pickle.dump(orders, f)
        break
    else:
        print('Неправильно введены даные')