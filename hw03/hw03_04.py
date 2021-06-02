from hashlib import sha256
from uuid import uuid4


def check_cache(url_obj):
    return cache_dict.setdefault(url_obj, sha256(salt.encode() + url_obj.encode()))


cache_dict = {}
salt = uuid4().hex   # статическая соль

check_cache('ya.ru')
check_cache('vk.com')
check_cache('ya.ru')
check_cache('https://pythonworld.ru/')

print(check_cache('sur'))

for el in cache_dict.keys():
    print(el, cache_dict[el].hexdigest())




