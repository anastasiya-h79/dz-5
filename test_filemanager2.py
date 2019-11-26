import shutil
import os
import sys


def filenames():
    result = []
    for item in os.listdir():
        if os.path.isfile(item):
            result.append(item)
    return result
    assert filenames() == ['.gitignore', 'LICENSE', 'banc_account.py', 'choose_one.py', 'filemanager.py', 'test_bill.py', 'test_filemanager2.py', 'test_python.py', 'victory.py', 'victory2.py']


def author_info():
    assert author_info() == 'anastasiahonak'


def quit():
    sys.exit(0)
    assert quit() == sys.exit(0)



