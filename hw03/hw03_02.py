from hashlib import sha256
from uuid import uuid4


def save_pwd():
    salt = uuid4().hex
    pwd = input('Введите пароль: ')
    hash_obj = sha256(salt.encode() + pwd.encode())
    print(salt)
    print(hash_obj.hexdigest())
    # записать в файл
    with open('pwd', 'w', encoding='utf-8') as f:
        f.write(salt + '\n' + hash_obj.hexdigest())


def authorization():  # если файл существует считываем пароль, если нет -- создаем его
    try:
        with open('pwd', 'r', encoding='utf-8') as f:
            salt = f.readline().rstrip("\n")
            hash_contr = f.readline()
            pwd2 = input('Введите пароль для входа: ')
            hash_obj2 = sha256(salt.encode() + pwd2.encode())
            print(salt)
            print(hash_contr)
            print(hash_obj2.hexdigest())
            if hash_contr == hash_obj2.hexdigest():
                print('Вход разрешен')
    except FileNotFoundError:
        print('Файл не существует')
        save_pwd()
        authorization()


authorization()
