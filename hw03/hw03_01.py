from time import perf_counter_ns, time

dict_obj = {}
lst_obj = []


def timing(func):
    def wrapped(*args):
        begin_time = time()
        res = func(*args)
        func_time = time() - begin_time
        print(f'Время выполнения функции {func.__name__}: {func_time}')
        return res
    return wrapped


@timing
def fill_dict_compl(n):                           # O(N)
    return {a: a for a in range (n)}        # добавление элемента O(1), перебор O(N).


@timing
def fill_lst_compl(n):                            # O(N)
    return [a for a in range (n)]           # добавление элемента O(1), перебор O(N).


@timing
def fill_list_append(lst_obj, n):
    for i in range(n):
        lst_obj.append(i)  # Вставка в конец списка, O(1)


@timing
def fill_list_insert(lst_obj, n):
    for i in range(n):
        lst_obj.insert(0, i)  # Вставка в начало списка, O(N)


@timing
def fill_dict(dict_obj, n):
    for i in range(n):
        dict_obj[i] = i      # O(1)

@timing
def change_list(lst_obj, n):
    for i in range (n):
        lst_obj[i] = lst_obj[i * 2]    # O(N)

@timing
def change_dict(dict_obj, n):
    for i in range (n):
        dict_obj[i] = i    # O(1)


@timing
def del_from_list(lst_obj, n):
    for i in range (n):
        lst_obj.pop(i)    # O(N)


@timing
def del_from_dict(dict_obj, n):
    for i in range (n):
        dict_obj.pop(i)    # O(1)


n = 100000
lst_obj = fill_lst_compl(n)
dict_obj = fill_dict_compl(n)

fill_list_append(lst_obj, n)
fill_list_insert(lst_obj, n)

fill_dict(dict_obj, n)

change_list(lst_obj, n)
change_dict(dict_obj, n)

del_from_list(lst_obj, n)
del_from_dict(dict_obj, n)





'''
Время выполнения функции fill_lst_compl: 0.008997201919555664
Время выполнения функции fill_dict_compl: 0.021010160446166992

Время выполнения функции fill_list_append: 0.015990257263183594
Время выполнения функции fill_list_insert: 81.7020092010498
Время выполнения функции fill_dict: 0.017991304397583008

Время заполнение словаря сопоставимо со временем заполнения списка при использовании append, insert же намного медленее 

Время выполнения функции change_list: 0.018999099731445312
Время выполнения функции change_dict: 0.04400300979614258

Время выполнения функции del_from_list: 61.113001585006714
Время выполнения функции del_from_dict: 0.023004531860351562

Удаление из словаря намного быстрее, константная сложность против линейной.
'''