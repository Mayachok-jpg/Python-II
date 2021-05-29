def sum_of_row(n):
    return n if n == 1 else n + sum_of_row(n-1)


number = int(input('Число? '))
print(f'Сумма, вычисленная рукурсивно: {sum_of_row(number)}, сумма вычисленная по формуле {number*(number+1)/2}')