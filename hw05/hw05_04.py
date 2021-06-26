from collections import OrderedDict
from timeit import timeit


def dict_insert(new_dict):
    for i in range(10000):
        new_dict[i] = i
    return new_dict


def dict_search(some_dict):
    return some_dict.get(99)


def dict_pop(my_dict):
    some_dict = dict_insert(my_dict)
    for i in range(1, 50):
        some_dict.pop(i)
    return some_dict


dict_obj = {}
ord_dict = OrderedDict()
dict_obj = dict_insert(dict_obj)
ord_dict = dict_insert(ord_dict)

print(timeit('dict_insert(dict_obj)', globals=globals(), number=10000))
print(timeit('dict_insert(ord_dict)', globals=globals(), number=10000))

print(timeit('dict_search(dict_obj)', globals=globals(), number=100000))
print(timeit('dict_search(ord_dict)', globals=globals(), number=100000))

print(timeit('dict_pop(dict_obj)', globals=globals(), number=10000))
print(timeit('dict_pop(ord_dict)', globals=globals(), number=10000))

"""
14.658546500000002
20.765127600000003
0.020966900000004784
0.021866000000002828
14.169031799999999
20.071426799999998

По результатам моих замеров (Python 3.9) обычный словарь оказался даже быстрее. Так что, видимо, в последних версиях 
нет смысла использовать OrderDict.
"""