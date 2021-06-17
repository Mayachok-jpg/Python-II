"""Сортировка пузырьком"""

import timeit
import random


def bubble_sort_rev(lst_obj):
    n = len(lst_obj)
    while n > 0:
        for i in range(len(lst_obj)-1, 0, -1):
            if lst_obj[i-1] > lst_obj[i]:
                lst_obj[i-1], lst_obj[i] = lst_obj[i], lst_obj[i-1]
        n -= 1
    return lst_obj


def bubble_sort_rev_1(lst_obj):
    n = len(lst_obj)
    while n > 0:
        no_swap = True
        for i in range(len(lst_obj)-1, 0, -1):
            if lst_obj[i-1] > lst_obj[i]:
                lst_obj[i-1], lst_obj[i] = lst_obj[i], lst_obj[i-1]
                no_swap = False
        if no_swap:
            break
        n -= 1
    return lst_obj


def bubble_sort_rev_2(lst_obj):
    n = 0
    while n < len(lst_obj):
        is_sorted = True
        for i in range(len(lst_obj) - 1, n, -1):  # не просматриваем заново уже отсортированную часть
            if lst_obj[i - 1] > lst_obj[i]:
                lst_obj[i - 1], lst_obj[i] = lst_obj[i], lst_obj[i - 1]
                is_sorted = False
        if is_sorted:
            break
        n += 1
    return lst_obj


orig_list_10 = [random.randint(-100, 100) for _ in range(10)]
orig_list_100 = [random.randint(-100, 100) for _ in range(100)]
orig_list_1000 = [random.randint(-100, 100) for _ in range(1000)]


# замеры 10
def test(lst_name):
    print(
        timeit.timeit(
            f"bubble_sort_rev({lst_name}[:])",
            globals=globals(),
            number=1000))

    print(
        timeit.timeit(
            f"bubble_sort_rev_1({lst_name}[:])",
            globals=globals(),
            number=1000))

    print(
        timeit.timeit(
            f"bubble_sort_rev_2({lst_name}[:])",
            globals=globals(),
            number=1000))


test('orig_list_10')
test('orig_list_100')
test('orig_list_1000')

'''
Первая доработка очень полезна, если переданный список может оказаться уже отсортированным, или даст небольшой прирост 
скорости если он окажется отсортирован раньше, чем отработает алгоритм. 
Вторая доработка дает более существенный и стабилный прирост скорости. 

'''
