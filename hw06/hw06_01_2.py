from random import randint
from memory_profiler import memory_usage
from timeit import default_timer

def decor(func):
    def wrapper(*args):
        m1 = memory_usage()
        start_time = default_timer()
        res = func(*args)
        m2 = memory_usage()
        mem_usage = m2[0] - m1[0]
        run_time = default_timer() - start_time
        return res, mem_usage, run_time
    return wrapper

@decor
def check_1(test_list):
    new_list_1 = [elem for elem in test_list if test_list.count(elem) == 1]
    return new_list_1


@decor
def check_2(test_list):
    new_list = [elem for num, elem in enumerate(test_list) if elem not in test_list[num + 1:]
                and elem not in test_list[:num]]
    return new_list


@decor
def check_3(test_list):
    for num, elem in enumerate(test_list):
        if elem not in test_list[num + 1:] and elem not in test_list[:num]:
            yield elem


if __name__ == '__main__':

    lst_obj = [randint(1, 1000) for i in range(10000)]

    res_1, mem_diff, runtime = check_1(lst_obj)
    print(f"Выполнение заняло {mem_diff} Mib и {runtime} секунд")

    res_2, mem_diff, runtime = check_2(lst_obj)
    print(f"Выполнение заняло {mem_diff} Mib и {runtime} секунд")

    my_generator, mem_diff, runtime = check_3(lst_obj)
    print(f"Выполнение заняло {mem_diff} Mib и {runtime} секунд")

'''
Выполнение заняло 0.01171875 Mib и 2.9242943 секунд   (list comprehension)
Выполнение заняло 0.30859375 Mib и 0.8574760000000001 секунд   (срезы)
Выполнение заняло 0.0 Mib и 0.10550990000000038 секунд  (генератор)

Через срезы получается гораздо быстрее, но памяти тратится больше. List comprehension экономит память, но тратит время.
Генератору нужен минимум памяти, а время чуть больше, чем у срезов. 

'''