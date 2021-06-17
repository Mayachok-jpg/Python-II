import operator
import timeit
import random


def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


lst_obj = [random.uniform(0.0, 50.0) for _ in range(10)]
print(f'Исходный массив: {lst_obj}')
print(f'Отсортированный массив: {merge_sort(lst_obj[:])}')

orig_list_10 = [random.uniform(0.0, 50.0) for _ in range(10)]
orig_list_100 = [random.uniform(0.0, 50.0) for _ in range(100)]
orig_list_1000 = [random.uniform(0.0, 50.0) for _ in range(1000)]

print(timeit.timeit("merge_sort(orig_list_10[:])",globals=globals(),number=1000))
print(timeit.timeit("merge_sort(orig_list_100[:])",globals=globals(),number=1000))
print(timeit.timeit("merge_sort(orig_list_1000[:])",globals=globals(),number=1000))

