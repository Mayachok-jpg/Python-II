def sum_of_row(n):
    return 1 if n == 1 else sum_of_row(n-1)*(-0.5)


number = int(input('Число? '))
print(sum_of_row(number))
