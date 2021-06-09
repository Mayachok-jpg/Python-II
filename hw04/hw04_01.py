from timeit import Timer

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

t1 = Timer('func_1(nums)', 'from __main__ import func_1, nums')
print ('func_1', t1.timeit(), 'milliseconds')
t2 = Timer('func_2(nums)', 'from __main__ import func_2, nums')
print ('func_2', t2.timeit(), 'milliseconds')

'''
Цифры не слишком отличаются, но ничего поинтереснее не смогла придумать.
В одной из статей прочитала следующее:
List comprehension быстрее for-циклов, которые он и заменяет. Это один из первых пунктов при рефакторинге Python-кода. 
'''
