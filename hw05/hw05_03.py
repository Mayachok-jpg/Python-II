from collections import deque
from timeit import timeit
from random import randint


def filling_list(nums):
    return [elem for elem in range(nums)]


def filling_deque(nums):
    return deque([elem for elem in range(nums)])


number_100 = 100
print(f'Заполнение списка (100 элементов):'
      f' {timeit("filling_list(number_100)", globals=globals(), number=1000)}')
print(f'Заполнение списка deque (100 элементов):'
      f' {timeit("filling_deque(number_100)", globals=globals(), number=1000)}')

number_1000 = 1000
print(f'Заполнение списка, (1000 элементов): '
      f'{timeit("filling_list(number_1000)", globals=globals())}')
print(f'Заполнение списка deque, (1000 элементов): '
      f'{timeit("filling_deque(number_1000)", globals=globals())}')


# appendleft и insert

def insert_list(my_list: list, nums: int):
    for _ in range(nums):
        my_list.insert(0, randint(0, 10))
    return my_list


def append_left_deque(my_deque, nums: int):
    for _ in range(nums):
        my_deque.appendleft(randint(0, 10))
    return my_deque


simple_list = filling_list(number_100)
deque_list = filling_deque(number_100)

print('-' * 100)
print(f'Вставка в начало списка:'
      f' {timeit("insert_list(simple_list, 100)", globals=globals(), number=1000)}')
print(f'Вставка в начало deque:'
      f' {timeit("append_left_deque(deque_list, 100)", globals=globals(), number=1000)}')


def pop_out_list_1(my_list: list, nums: int):
    for _ in range(nums):
        my_list.pop()
    return my_list


def pop_out_deque_1(my_deque, nums: int):
    for _ in range(nums):
        my_deque.pop()
    return my_deque


def pop_out_list_2(my_list: list, nums: int):
    for _ in range(nums):
        my_list.pop(0)
    return my_list


def pop_out_deque_2(my_deque, nums: int):
    for _ in range(nums):
        my_deque.popleft()
    return my_deque


print('-' * 100)
print(f'Извлечение с конца списка 100 элементов:'
      f' {timeit("pop_out_list_1(simple_list, 100)", globals=globals(), number=1000)}')
print(f'Извлечение с конца deque 100 элементов:'
      f' {timeit("pop_out_deque_1(deque_list, 100)", globals=globals(), number=1000)}')


def append_list(my_list: list, nums: int):
    for _ in range(nums):
        my_list.append(randint(0, 10))
    return my_list


def append_deque(my_deque, nums: int):
    for _ in range(nums):
        my_deque.append(randint(0, 10))
    return my_deque


print('-' * 100)
print(f'Вставка в обычный список 100 элементов:'
      f' {timeit("append_list(simple_list, 100)", globals=globals(), number=1000)}')
print(f'Вставка в deque 100 элементов:'
      f' {timeit("append_deque(deque_list, 100)", globals=globals(), number=1000)}')

print('-' * 100)
print(f'Извлечение с начала обычного списка 100 элементов:'
      f' {timeit("pop_out_list_2(simple_list, 100)", globals=globals(), number=1000)}')
print(f'Извлечение с начала deque 100 элементов:'
      f' {timeit("pop_out_deque_2(deque_list, 100)", globals=globals(), number=1000)}')

"""
Заполнение списка (100 элементов): 0.009111999999999995
Заполнение списка deque (100 элементов): 0.0093086
Заполнение списка, (1000 элементов): 67.0646668
Заполнение списка deque, (1000 элементов): 79.96732080000001
----------------------------------------------------------------------------------------------------
Вставка в начало списка: 6.788621199999994
Вставка в начало deque: 0.16535840000000235
----------------------------------------------------------------------------------------------------
Извлечение с конца списка 100 элементов: 0.009611500000005435
Извлечение с конца deque 100 элементов: 0.009568299999983765
----------------------------------------------------------------------------------------------------
Вставка в обычный список 100 элементов: 0.17641170000001694
Вставка в deque 100 элементов: 0.17013350000001992
----------------------------------------------------------------------------------------------------
Извлечение с начала обычного списка 100 элементов: 4.233778700000016
Извлечение с начала deque 100 элементов: 0.011265099999974382

Самая большая разница по времени при вставке в начало списка и извлечении с начала списка. Если часто нужен такой доступ
имеет смысл использовать deque 
"""