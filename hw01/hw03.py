def max_profit_1(dict_obj):     # O(N LOG N)
    return [next(k for k in firms_dict if firms_dict[k] == v) for v in sorted(firms_dict.values(), reverse=True)[:3]]


def max_profit_2(dict_obj):     #O(N) вариант эффективнее
    res = [0, 0, 0]
    for i in dict_obj.values():
        if i > res[-1]:
            res.pop()
            res.append(i)
            res.sort(reverse=True)
    return [next(k for k in firms_dict if firms_dict[k] == v) for v in res]


firms_dict = {'firm_1': 100500, 'firm_2': 100600, 'firm_3': 500500, 'firm_4': 200500, 'firm_5': 100}

for el in max_profit_1(firms_dict):
    print(f'{el}, {firms_dict[el]}')

print('\nВариант два:')

for el in max_profit_2(firms_dict):
    print(f'{el}, {firms_dict[el]}')

"""
Второй вариант эффективнее, количество операций с ростом количества элементов растет медленее
(сортировать весь объем данных ради поиска трех максимуммов не эффективно)
"""




