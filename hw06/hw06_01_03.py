from random import randint
from pympler import asizeof

class Matrix():
    def __init__(self, ll):
        self.nums = ll

    def __str__(self):
        res = ''
        max_len = len(str(max(map(max, self.nums))))
        for el_str in self.nums:
            for el_st in el_str:
                res += f'{el_st:^{max_len}} '
            res += '\n'
        return res[:-2]

    def __add__(self, other):
        if type(other) == Matrix:
            try:
                res = self.nums
                for i in range(len(self.nums)):
                    for j in range(len(self.nums[0])):
                        res[i][j] = self.nums[i][j] + other.nums[i][j]
                return Matrix(res)
            except IndexError:
                print('Размер матриц не совпадает')

        else:
            raise ValueError


class MatrixSlots():

    __slots__ = ['nums']

    def __init__(self, ll):
        self.nums = ll

    def __str__(self):
        res = ''
        max_len = len(str(max(map(max, self.nums))))
        for el_str in self.nums:
            for el_st in el_str:
                res += f'{el_st:^{max_len}} '
            res += '\n'
        return res[:-2]

    def __add__(self, other):
        if type(other) == MatrixSlots:
            try:
                res = self.nums
                for i in range(len(self.nums)):
                    for j in range(len(self.nums[0])):
                        res[i][j] = self.nums[i][j] + other.nums[i][j]
                return MatrixSlots(res)
            except IndexError:
                print('Размер матриц не совпадает')

        else:
            raise ValueError


row = 100
column = 100

m1 = Matrix([[randint(100, 1000) for j in range(column)] for i in range(row)])
m2 = MatrixSlots([[randint(100, 1000) for j in range(column)] for i in range(row)])

print('Размер экземпляра класса:', asizeof.asizeof(m1))
print('Размер экземпляра класса со слотами:', asizeof.asizeof(m2))

'''
На одном экземпляре класса экономия не очень существеннная, но тем не менее она есть, и при ипользовании  нескольких 
экземпляров будет уже заметна. К тому же экономия увеличивается при увеличении размера матрицы. 

10:
Размер экземпляра класса: 5368
Размер экземпляра класса со слотами: 5264

100:
Размер экземпляра класса: 362536
Размер экземпляра класса со слотами: 359104
'''
