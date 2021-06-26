def sum_of_row(n):
    res = 1
    if n == 0:
        return n
    res += sum_of_row(n-1)*(-0.5)
    return res

number = int(input('Число? '))
print(sum_of_row(number))
