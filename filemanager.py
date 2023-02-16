import os
import shutil
import sys
import platform
import choose_one
import victory
import banc_account


my_choice = True
while my_choice == True:
    choose = choose_one.choose_one()
    # 1. после выбора пользователь вводит название папки, создаем её в рабочей директории
    if choose == 1:
        new_dir = input('Введите название папки ')
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
            print('Папка создана')
        else:
            print('Такая папка уже существует')
    # 2. удалить файл/папку. после выбора пользователь вводит название папки или файла, удаляем из рабочей директории, если такой есть
    if choose == 2:
        dir_or_file_del = input('Введите название папки или файла для удаления ')
        if os.path.exists(dir_or_file_del):
            os.rmdir(dir_or_file_del)
            print('Папка/файл удалены с компьтера')
        else:
            print('Такой папки/файла не существует')

    # 3. копировать файл/папку. после выбора пользователь вводит название папки/файла и новое название папки/файла. копируем
    if choose == 3:
        dir_to_copy = input('Введите имя папки или файла для копирования: ')
        if os.path.exists(dir_to_copy):
            dir_new_name = input('Введите новое имя папки или файла: ')
            shutil.copy(dir_to_copy, dir_new_name)
            print('Новая папка/файл создана')
        else:
            print('Такой папки/файла не существует')

    # 4. просмотр содержимого рабочей директории. вывод всех объектов в рабочей папке
    if choose == 4:
        print(os.listdir())

    # 5. посмотреть только папки. вывод только папок которые находятся в рабочей папке
    if choose == 5:
        only_dirs = [f for f in os.listdir() if os.path.isdir(f)]
        print(only_dirs)

    # 6. вывод только файлов которые находятся в рабочей папке
    if choose == 6:
        only_files = [f for f in os.listdir() if os.path.isfile(f)]
        print(only_files)

    # 7. вывести информацию об операционной системе (можно использовать пример из 1-го урока)
    if choose == 7:
        print(platform.uname())

    # 8. вывод информации о создателе программы
    if choose == 8:
        print(os.getlogin())

    # 9. запуск игры викторина из предыдущего дз
    if choose == 9:
        victory.victory()

    # 10. запуск программы для работы с банковским счетом из предыдущего дз (задание учебное, после выхода из программы управлением счетом в главной программе сумму и историю покупок можно не запоминать)
    if choose == 10:
       banc_account.buy()


    # 11. выход из программы
    if choose == 12:
        break




