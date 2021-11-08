import os
import PyInstaller.__main__
from tkinter import *
from tkinter import filedialog
from cryptography.fernet import Fernet


def getKey():
    key = Fernet.generate_key()
    return key


def encrypt(key, content):
    f = Fernet(key)
    encrypted = f.encrypt(content)
    return encrypted


def getContents():
    window = Tk()
    window.withdraw()
    file_path = filedialog.askopenfilename()
    with open(file_path, 'rb') as file:
        content = file.read()
        file.close()
        return content


def generate(key, content):
    with open(os.path.join('main.py'), 'w') as file:
        file.write('from cryptography.fernet import Fernet\n')
        file.write(f'f2 = Fernet({key})\n')
        file.write(f'decrypted = f2.decrypt({content})\n')
        file.write(f'exec(decrypted)')
        file.close()




content = getContents()
key = getKey()
encrypted = encrypt(key, content)
generate(key, encrypted)
#create exe from PyInstaller
PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    '--hidden-import=keyboard',
    '--noconsole'
])