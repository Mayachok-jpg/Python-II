from time import perf_counter_ns

dict_obj = {}
lst_obj = []

def timing(func):
    def wrapped(*args):
        begin_time = perf_counter_ns()
        res = func(*args)
        func_time = perf_counter_ns() - begin_time
        return res, func_time
    return wrapped

@timing
def fill_dict(n):                           # O(N)
    return {a: a for a in range (n)}        # добавление элемента O(1), перебор O(N).

@timing
def fill_lst(n):                            # O(N)
    return [a for a in range (n)]           # добавление элемента O(1), перебор O(N).

n = 100000
lst_obj, lst_time = fill_lst(n)
dict_obj, dict_time = fill_dict(n)


print(f'Время сознания словаря {dict_time}')
print(f'Время сознания списка {lst_time}')


time = perf_counter_ns()
len(dict_obj)                                              #O(1)
print(f'Длина словаря: {perf_counter_ns() - time}')

time = perf_counter_ns()
len(lst_obj)                                               #O(1)
print(f'Длина списка: {perf_counter_ns() - time}')

time = perf_counter_ns()
for el in dict_obj: pass                                   #O(N)
print(f'Перебор словаря: {perf_counter_ns() - time}')

time = perf_counter_ns()
for el in lst_obj: pass
print(f'Перебр списка: {perf_counter_ns() - time}')         #O(N)

time = perf_counter_ns()
el = dict_obj[5]                                            #O(1)
print(f'Получение элемента словаря: {perf_counter_ns() - time}')

time = perf_counter_ns()
el = lst_obj[5]                                             #O(1)
print(f'Получение элемента списка: {perf_counter_ns() - time}')

time = perf_counter_ns()
if el in dict_obj.values(): pass                            #O(N)
print(f'Проверка наличия элемента: {perf_counter_ns() - time}')

time = perf_counter_ns()
if el in lst_obj: pass                                      #O(N)
print(f'Проверка наличия элемента: {perf_counter_ns() - time}')

'''По времени все операции со словарем оказались более затратными. Видимо, из-за хеша'''