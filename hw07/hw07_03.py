import random
from statistics import median
import timeit

orig_list_11 = [random.randint(0, 10) for _ in range(11)]
orig_list_101 = [random.randint(0, 10) for _ in range(101)]
#test = [1, 1, 1, 1, 1, 1, 11]
test = [5, 3, 4, 3, 3, 3, 3]

def median_search(lst_obj):
    for _ in range(len(lst_obj) // 2):
        lst_obj.remove(max(lst_obj))
    return max(lst_obj)

print(test)
print('Медиана: ', median_search(test[:]))
print('Медиана, найденная с помощью встроенной функции:', median(test[:]))

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
