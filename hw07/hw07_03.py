import random
from statistics import median
import timeit


def create_list(m):
    return [random.randint(0, 100) for _ in range(2*m + 1)]


orig_list_11 = create_list(5)
orig_list_101 = create_list(50)

def median_search(lst_obj):
    for _ in range(len(lst_obj) // 2):
        lst_obj.remove(max(lst_obj))
    return max(lst_obj)

try:
    m = int(input('Введите m: '))
except ValueError:
    print('Вы ввели не число')
else:
    test = create_list(m)
    print(test)
    print('Медиана: ', median_search(test[:]))
    print('Медиана, найденная с помощью встроенной функции:', median(test[:]))
    print('='*50)

print(orig_list_11)
sort_lst = orig_list_11[:]
sort_lst.sort()
print(sort_lst)

print('Медиана: ', median_search(orig_list_11[:]))
print('Медиана, найденная с помощью встроенной функции:', median(orig_list_11[:]))


print('Замеры:')
print(timeit.timeit("median_search(orig_list_11[:])",globals=globals(),number=1000))
print(timeit.timeit("median_search(orig_list_101[:])",globals=globals(),number=1000))
print('Встроенная')
print(timeit.timeit("median(orig_list_11[:])",globals=globals(),number=1000))
print(timeit.timeit("median(orig_list_101[:])",globals=globals(),number=1000))
