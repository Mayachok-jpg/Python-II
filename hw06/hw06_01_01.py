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
def even_1(nums):
    new_list = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_list.append(i)
    return new_list


@decor
def even_2(nums):
    new_list = list(map(lambda x: x % 2 == 0, nums))
    return new_list


if __name__ == '__main__':
    list_obj_1 = [randint(0, 10000) for _ in range(10000)]
    list_obj_2 = [randint(0, 10000) for _ in range(10000000)]
    res_1, mem_diff_1, runtime_1 = even_1(list_obj_1)
    res_2, mem_diff_2, runtime_2 = even_2(list_obj_1)

    print('10000')
    print(f"append: {mem_diff_1} Mib и {runtime_1} секунд")
    print(f"map: {mem_diff_2} Mib и {runtime_2} секунд")

    res_1, mem_diff_1, runtime_1 = even_1(list_obj_2)
    res_2, mem_diff_2, runtime_2 = even_2(list_obj_2)
    print('1000000')
    print(f"append: {mem_diff_1} Mib и {runtime_1} секунд")
    print(f"map: {mem_diff_2} Mib и {runtime_2} секунд")

"""
Как и сказано в лекции, map позволяет существенно памать.

10000
append: 0.1875 Mib и 0.12117579999999961 секунд
map: 0.08203125 Mib и 0.11259799999999842 секунд

1000000
append: 193.5234375 Mib и 2.3070406000000006 секунд
map: 76.75 Mib и 2.612612200000001 секунд

"""
