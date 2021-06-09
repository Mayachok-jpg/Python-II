from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    max_elem = max(array, key=array.count)
    count = array.count(max_elem)
    return f'Чаще всего встречается число {max_elem}, ' \
           f'оно появилось в массиве {count} раз(а)'


def func_4():
    max_elem = max(set(array), key=array.count)
    count = array.count(max_elem)
    return f'Чаще всего встречается число {max_elem}, ' \
           f'оно появилось в массиве {count} раз(а)'

print(f'func_1 - {timeit("func_1()", globals=globals())}')
print(f'func_2 - {timeit("func_2()", globals=globals())}')
print(f'func_3 - {timeit("func_3()", globals=globals())}')
print(f'func_4 - {timeit("func_4()", globals=globals())}')

'''
Самое быстрое решение через встроенную функцию. Его можно еще немного ускорить, 
если передать только уникальные значения (и это на коротком массиве, если повторений 
элементов будет больше, то и выигрыш станет более заметным) 
'''