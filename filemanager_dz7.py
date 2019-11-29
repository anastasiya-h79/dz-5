
#import sys
#import json

import os
import shutil
from banc_account import buy
from victory import victory

curr_path = os.getcwd()


def create_dir():
    new_path = input('Введите имя папки')

    if os.path.exists(new_path):
        print('Папка уже существует!')
    else:
        os.mkdir(new_path)
        print('Создана папка '+ new_path)
    return new_path


def delete_file_dir():
    while True:
        new_path = input('Введите имя папки/файла для удаления')
        full_path = os.path.join(os.getcwd(), new_path)
        if os.path.exists(full_path):
            if os.path.isfile(full_path):
                try:
                    os.remove(full_path)
                    print('Файл удален')
                    break
                except FileNotFoundError:
                    print('Файл не существует!')
                    continue
            try:
                shutil.rmtree(full_path)
                print('Папка удалена')
                break
            except FileNotFoundError:
                print('Файл не существует!')


def copy_file_dir():
    in_path = input('Введите имя папки/файла для копирования ')
    if not os.path.exists(in_path):
        message = 'Копируемая папка/файл не существует!'
    elif os.path.isdir(in_path):
        shutil.copytree(in_path, os.getcwd())
        message = 'Создана копия папки: '+ in_path
    else:
        os.path.isdir(in_path)
        shutil.copyfile(in_path, os.getcwd())
        message = 'Создана копия файла: '+ in_path
    return message


def show_list():
    print(os.listdir())   #список файлов и директорий в папке

def show_dir():
    #print('Папки: ', list(filter(lambda x: os.path.isdir(x), os.listdir())))
    result = [x for x in os.listdir() if os.path.isdir(x)]
    print(result)

def show_files():
    #print('Файлы:', list(filter(lambda x: os.path.isfile(x), os.listdir())))
    result = [x for x in os.listdir() if os.path.isfile(x)]
    print(result)

def show_os():
    print('Операционная система:', os.name)

def author_info():
    print(os.getlogin())

def victory_game():
    victory()

def banc_acc():
    buy()


def save_content():
    content = os.listdir()
    files = filter(lambda x: os.path.isfile(x), content)
    dirs = filter(lambda x: os.path.isdir(x), content)
    with open('listdir.txt', 'w') as f:
        f.write('files: ')
        for file in files:
            f.write(f'{file}, ')
        f.write('\n')
        f.write('dirs: ')
        for dir in dirs:
            f.write(f'{dir}, ')







