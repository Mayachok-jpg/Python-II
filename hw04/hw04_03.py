from cProfile import run
from timeit import timeit
from random import randint

def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    if enter_num // 10 <= 0:
        return str(enter_num)
    return str(enter_num % 10) + revers_4(enter_num//10)

print('timeit test:')
number = randint(10000, 100000)

print(f'revers_1 - {timeit("revers_1(number)", globals=globals())}')
print(f'revers_2 - {timeit("revers_2(number)", globals=globals())}')
print(f'revers_3 - {timeit("revers_3(number)", globals=globals())}')
print(f'revers_4 - {timeit("revers_4(number)", globals=globals())}')

test_str = '''
for i in range(10000):
    revers_'''

print('\ncProfile test:')
for i in range(1, 5):
    print(f'{"-"*30}{i}{"-"*30}')
    run(f'{test_str}{i}(number)')

'''
Самый медленные первая и четвертая, из-за рекурсии.
Самый быстрый вариант — через срез.
cPrоfile показывает, что в четвертой вызовов меньше, чем в первой, но все же она медленнее. 
Видимо из-за преобразований числа в строку.
'''
