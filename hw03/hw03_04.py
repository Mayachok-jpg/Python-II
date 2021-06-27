from hashlib import sha256
from uuid import uuid4


def check_cache(url_obj):
    if cache_dict.get(url_obj) is None:
        cache_dict[url_obj] = sha256(salt.encode() + url_obj.encode())
        print(f'Значение добавлено, {url_obj}, {cache_dict[url_obj]}')
    else:
        print(f'Значение есть в кеше:, {url_obj}, {cache_dict[url_obj]}')


cache_dict = {}
salt = uuid4().hex   # статическая соль

check_cache('ya.ru')
check_cache('vk.com')
check_cache('ya.ru')


url = 'ya.ru'
print(cache_dict.setdefault(url, sha256(salt.encode() + url.encode())))
url = 'sur'
print(cache_dict.setdefault(url, sha256(salt.encode() + url.encode())))

print(cache_dict)

for el in cache_dict.values():
    print(el.hexdigest())

for el in cache_dict.keys():
    print(el, cache_dict[el].hexdigest())

check_cache('ya.ru')




